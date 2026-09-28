"""Train the student (reference; this is how the shipped student was made) and score pairs with it.

The student is a cross-encoder: input = tokenizer(string, card), truncated longest-first at 192 tokens (a card can be
longer than the string); mean-pooled multilingual-e5-base -> one logit; loss = binary cross-entropy to Jev's p for the
pair (a soft target). Multi-GPU with accelerate (DDP), bf16 autocast.

Training data = train_v1_jev_labels.jsonl.gz from the GitHub release: 3,763,631 (string, card) pairs from 200,000
affiliation strings drawn at random from OpenAlex, each candidate pool built as for the benchmark, each pair judged by
Jev (TypeSafe's decision model, jev-1.13.0, the question in jev_teacher.py). Row = {set, k (string id), i (institution
id), s (string, first 1,500 characters), c (card, retrieve.Index.card), p (Jev's p), split}; split "val" = strings
with id % 50 == 0 (74,900 pairs). The shipped student: 2 epochs, batch 64 per GPU on 8 H100s, lr 4e-5, the default seed,
torch 2.6.0, transformers 4.x.

    accelerate launch --multi_gpu --num_processes 8 --mixed_precision bf16 matcher/training/student_xenc.py train \
        --train train_v1_jev_labels.jsonl.gz --out student_retrained --base intfloat/multilingual-e5-base
    python matcher/training/student_xenc.py infer --model student_retrained --input pairs.jsonl.gz --out preds.jsonl

train also writes <out>/val.json: Pearson r, MAE and AUC against Jev on the val split. The shipped student scored
Pearson 0.953, AUC 0.991, and agrees with Jev at 0.5 on 97.6% of val pairs. infer reads rows with s and c (and p, set,
k, i) and writes {set, key, inst, noul = student p rounded to 4 decimals, jev = the row's p}.
"""
import argparse, gzip, json, math, os, random, time
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer


class XEnc(nn.Module):
    def __init__(self, base):
        super().__init__()
        self.enc = AutoModel.from_pretrained(base, torch_dtype=torch.float32, add_pooling_layer=False)  # unused pooler breaks DDP
        self.drop = nn.Dropout(0.1)
        self.head = nn.Linear(self.enc.config.hidden_size, 1)

    def forward(self, ids, mask):
        h = self.enc(input_ids=ids, attention_mask=mask).last_hidden_state
        m = mask.unsqueeze(-1).to(h.dtype)
        return self.head(self.drop((h * m).sum(1) / m.sum(1).clamp_min(1.0))).squeeze(-1)


def rows(path, split=None):
    out = []
    for l in (gzip.open(path, "rt") if path.endswith(".gz") else open(path)):
        r = json.loads(l)
        if split is None or r["split"] in split:
            out.append(r)
    return out


def enc(tok, batch, maxlen):
    return tok([r["s"] for r in batch], [r["c"] for r in batch], padding=True, truncation="longest_first",
               max_length=maxlen, return_tensors="pt")


class _Batches(torch.utils.data.Dataset):
    """Length-sorted batches, tokenized in DataLoader workers (the GPU waits on the tokenizer otherwise)."""

    def __init__(self, tok, R, order, bs, maxlen):
        self.tok, self.R, self.maxlen = tok, R, maxlen
        self.b = [order[s:s + bs] for s in range(0, len(order), bs)]

    def __len__(self):
        return len(self.b)

    def __getitem__(self, j):
        return self.b[j], enc(self.tok, [self.R[i] for i in self.b[j]], self.maxlen)


@torch.no_grad()
def predict(m, tok, R, dev, maxlen, bs=512, log=None, workers=0):
    """Same batches and math with or without workers (workers only move tokenization off the main thread)."""
    m.eval()
    order = sorted(range(len(R)), key=lambda i: len(R[i]["s"]) + len(R[i]["c"]))
    out, t0 = [0.0] * len(R), time.time()
    D = _Batches(tok, R, order, bs, maxlen)
    it = torch.utils.data.DataLoader(D, batch_size=None, num_workers=workers, prefetch_factor=8 if workers else None,
                                     collate_fn=lambda x: x) if workers else (D[j] for j in range(len(D)))
    for n, (idx, e) in enumerate(it):
        s = n * bs
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=dev.type == "cuda"):
            z = m(e["input_ids"].to(dev), e["attention_mask"].to(dev))
        for j, p in zip(idx, torch.sigmoid(z.float()).cpu().tolist()):
            out[j] = p
        if log and (s // bs) % 200 == 0:
            log(f"  infer {s + len(idx):,}/{len(R):,} {time.time() - t0:.0f}s")
    return out


def agreement(R, P):
    """Student vs Jev: Pearson r, MAE, AUC of student p for Jev's p >= 0.5, and agreement at 0.5."""
    import numpy as np
    from sklearn.metrics import roc_auc_score
    y, p = np.array([r["p"] for r in R]), np.array(P)
    lab = y >= 0.5
    return {"n": len(R), "pearson": float(np.corrcoef(y, p)[0, 1]), "mae": float(np.abs(y - p).mean()),
            "auc": float(roc_auc_score(lab, p)) if 0 < lab.sum() < len(lab) else None,
            "agree_at_0.5": float(((p >= 0.5) == lab).mean()), "jev_pos_share": float(lab.mean())}


def train(a):
    from accelerate import Accelerator
    acc = Accelerator(mixed_precision="bf16")
    log = lambda *x: acc.print(*x, flush=True)
    torch.manual_seed(a.seed)
    R = rows(a.train, {"train"})
    if a.limit:
        R = R[:a.limit]
    V = rows(a.train, {"val"})[:a.val_limit]
    log(f"{len(R):,} train pairs, {len(V):,} val pairs, {acc.num_processes} procs")
    tok = AutoTokenizer.from_pretrained(a.base)
    m = XEnc(a.base)
    opt = torch.optim.AdamW(m.parameters(), lr=a.lr, weight_decay=0.01)
    per_step = a.bs * acc.num_processes
    steps_ep = len(R) // per_step
    total = int(steps_ep * a.epochs)
    warm = max(1, int(0.05 * total))
    sched = torch.optim.lr_scheduler.LambdaLR(opt, lambda s: min((s + 1) / warm, max(0.0, (total - s) / max(1, total - warm))))
    m, opt = acc.prepare(m, opt)  # not sched: accelerate steps a prepared scheduler once per process, ending it 8x early
    step, t0, run, nrun = 0, time.time(), 0.0, 0
    m.train()
    while step < total:
        ep = step // steps_ep
        if step % steps_ep == 0:
            order = list(range(len(R)))
            random.Random(a.seed + ep).shuffle(order)
        base = (step % steps_ep) * per_step + acc.process_index * a.bs
        batch = [R[j] for j in order[base:base + a.bs]]
        e = enc(tok, batch, a.maxlen)
        y = torch.tensor([float(r["p"]) for r in batch], device=acc.device)
        z = m(e["input_ids"].to(acc.device), e["attention_mask"].to(acc.device))
        loss = F.binary_cross_entropy_with_logits(z.float(), y)
        acc.backward(loss)
        acc.clip_grad_norm_(m.parameters(), 1.0)
        opt.step(); sched.step(); opt.zero_grad(set_to_none=True)
        step += 1; run += loss.item(); nrun += 1
        if step % a.log_every == 0 or step == total:
            el = time.time() - t0
            log(f"step {step}/{total} ep {ep} loss {run / nrun:.4f} lr {sched.get_last_lr()[0]:.2e} "
                f"{step * per_step / el:.0f} pairs/s eta {(total - step) * el / step / 60:.1f} min")
            run, nrun = 0.0, 0
    acc.wait_for_everyone()
    if acc.is_main_process:
        os.makedirs(a.out, exist_ok=True)
        mm = acc.unwrap_model(m)
        torch.save(mm.state_dict(), f"{a.out}/model.pt")
        tok.save_pretrained(a.out)
        json.dump({"base": a.base, "maxlen": a.maxlen, "steps": total, "n_train": len(R), "args": vars(a)},
                  open(f"{a.out}/student.json", "w"), indent=1)
        P = predict(mm, tok, V, acc.device, a.maxlen)
        v = agreement(V, P)
        json.dump(v, open(f"{a.out}/val.json", "w"), indent=1)
        log(f"saved {a.out}; val vs Jev {json.dumps(v)}; {time.time() - t0:.0f}s")


def infer(a):
    dev = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    meta = json.load(open(f"{a.model}/student.json"))
    m = XEnc(meta["base"])
    m.load_state_dict(torch.load(f"{a.model}/model.pt", map_location="cpu"))
    m.to(dev)
    tok = AutoTokenizer.from_pretrained(a.model)
    R = rows(a.input, set(a.split.split(",")) if a.split else None)
    if a.limit:
        R = R[:a.limit]
    t0 = time.time()
    P = predict(m, tok, R, dev, meta["maxlen"], log=lambda x: print(x, flush=True), workers=a.workers)
    with open(a.out, "w") as f:
        for r, p in zip(R, P):
            f.write(json.dumps({"set": r["set"], "key": r["k"], "inst": r["i"], "ok": True, "noul": round(p, 4),
                                "jev": r["p"]}) + "\n")
    print(f"wrote {a.out}: {len(R):,} pairs, {len(R) / max(time.time() - t0, 1e-6):.0f} pairs/s on {dev}; "
          f"vs Jev {json.dumps(agreement(R, P))}", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["train", "infer"])
    ap.add_argument("--train"); ap.add_argument("--out"); ap.add_argument("--base", default="intfloat/multilingual-e5-base")
    ap.add_argument("--epochs", type=float, default=2.0); ap.add_argument("--bs", type=int, default=64)
    ap.add_argument("--maxlen", type=int, default=192); ap.add_argument("--lr", type=float, default=4e-5)
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--val-limit", type=int, default=100000)
    ap.add_argument("--log-every", type=int, default=100); ap.add_argument("--seed", type=int, default=1363)
    ap.add_argument("--model"); ap.add_argument("--input"); ap.add_argument("--split", default="")
    ap.add_argument("--workers", type=int, default=0, help="infer: DataLoader workers for tokenization")
    a = ap.parse_args()
    train(a) if a.cmd == "train" else infer(a)
