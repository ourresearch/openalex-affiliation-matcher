"""Score every (string, candidate) pair in a benchmark set's pools with the student, and compare with the shipped p.

    python scripts/student_scores.py test_v2 --model student_model --out preds/student_p_test_v2.jsonl.gz
    python scripts/student_scores.py test_v2 --model student_model --limit 300     # a quick check on a CPU

The pairs are the pool (decider.pool over the four generators' ranked lists) restricted to institutions with a card,
the same pairs as benchmarks/data/student_p/<set>.jsonl.gz. Output has that file's format, p rounded to 4 decimals
(the chooser was trained on rounded p), so it can go straight to scripts/decide.py --p.

The student's base architecture is intfloat/multilingual-e5-base, fetched from the Hugging Face Hub at the pinned
revision below (model.pt then overwrites every weight). Needs torch, transformers, sentencepiece, huggingface_hub.
Speed: about 1,000 pairs/s on an L4, 4,000 or more on an H100 (test v2 has 376,065 pairs); a CPU does tens per second.
On a CUDA GPU the student runs with bf16 autocast, as when the shipped p were made (H100); on a CPU it runs in fp32 and
p differ slightly (mean |dp| about 0.0004).
"""
import argparse
import gzip
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from matcher.candidates import candidates  # noqa: E402
from matcher.decider import POOL  # noqa: E402
from matcher.retrieve import Index  # noqa: E402

BASE = "intfloat/multilingual-e5-base"
BASE_REVISION = "d128750597153bb5987e10b1c3493a34e5a4502a"


def jsonl(path):
    return map(json.loads, gzip.open(path, "rt") if path.endswith(".gz") else open(path))


ap = argparse.ArgumentParser()
ap.add_argument("set")
ap.add_argument("--model", default=os.path.join(ROOT, "student_model"), help="the unpacked student_model.tar.gz")
ap.add_argument("--out", help="default preds/student_p_<set>.jsonl.gz")
ap.add_argument("--limit", type=int, default=0, help="only the first N strings (a quick check)")
ap.add_argument("--workers", type=int, default=8 if sys.platform.startswith("linux") else 0,
                help="tokenizer processes (DataLoader workers); 0 = tokenize in the main process. Workers need Linux "
                     "(on macOS and Windows the DataLoader spawns, and predict()'s collate function cannot be pickled)")
ap.add_argument("--data", default=os.path.join(ROOT, "benchmarks", "data"))
ap.add_argument("--models", default=os.path.join(ROOT, "models"))
a = ap.parse_args()
out = a.out or os.path.join(ROOT, "preds", f"student_p_{a.set}.jsonl.gz")
os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)

from huggingface_hub import snapshot_download  # noqa: E402
from matcher import student  # noqa: E402

t0 = time.time()
ix = Index(os.path.join(a.models, "institutions.jsonl.gz"))
S = {d["id"]: d["string"] for d in jsonl(os.path.join(a.data, f"{a.set}.jsonl.gz"))}
R = {d["id"]: {g: d.get(g, []) for g, _ in POOL} for d in jsonl(os.path.join(a.data, "pools", f"{a.set}.jsonl.gz"))}
keys = list(S)[:a.limit] if a.limit else list(S)
pairs = [(k, S[k], i) for k in keys for i in candidates(ix, R[k])]
base_dir = snapshot_download(BASE, revision=BASE_REVISION, allow_patterns=["config.json", "model.safetensors"])
st = student.load(a.model, base_dir)
print(f"{len(keys):,} strings, {len(pairs):,} pairs; student on {st[2]}; setup {time.time() - t0:.0f}s", flush=True)
t1 = time.time()
P = student.p_for(st, ix, pairs, workers=a.workers, log=lambda x: print(x, flush=True))
print(f"scored {len(pairs):,} pairs in {time.time() - t1:.0f}s ({len(pairs) / max(time.time() - t1, 1e-6):,.0f} pairs/s)")

with gzip.open(out, "wt") as f:
    for k in keys:
        f.write(json.dumps({"id": k, "p": [[i, P[(k, i)]] for i in candidates(ix, R[k])]}) + "\n")
print(f"wrote {out}")

shipped = os.path.join(a.data, "student_p", f"{a.set}.jsonl.gz")
if os.path.exists(shipped):
    ref = {d["id"]: dict((i, p) for i, p in d["p"]) for d in jsonl(shipped)}
    same_pairs = sum(set(ref.get(k, {})) == {i for i in candidates(ix, R[k])} for k in keys)
    d = [abs(P[(k, i)] - ref[k][i]) for k, _, i in pairs if i in ref.get(k, {})]
    cross = sum((P[(k, i)] >= 0.5) != (ref[k][i] >= 0.5) for k, _, i in pairs if i in ref.get(k, {}))
    print(f"vs shipped p: same pairs on {same_pairs:,} / {len(keys):,} strings; |dp| mean {sum(d) / max(len(d), 1):.5f}, "
          f"max {max(d, default=0):.4f}; {cross:,} of {len(d):,} pairs on the other side of 0.5")
