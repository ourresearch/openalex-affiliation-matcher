"""Run a frozen chooser over a benchmark set's candidate pools and write its answers.

    python scripts/decide.py test_v2                      # student chooser, shipped student p -> preds/test_v2.jsonl
    python scripts/decide.py test_v2 --p preds/student_p_test_v2.jsonl.gz --out preds/test_v2_gpu.jsonl
    python scripts/decide.py test_v2 --chooser models/chooser_no_model.json --out preds/test_v2_no_model.jsonl

Inputs: benchmarks/data/<set>.jsonl.gz (strings), benchmarks/data/pools/<set>.jsonl.gz (each generator's ranked ids),
a p file ({"id", "p": [[institution id, p], ...]}; default benchmarks/data/student_p/<set>.jsonl.gz), a chooser JSON
and the cards, lineage and ROR relationship files in models/. Output: one line per string, {"id", "ids"}.
CPU only, numpy only; 20,000 strings take well under a minute.
"""
import argparse
import gzip
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from matcher.batch import decide_many  # noqa: E402
from matcher.decider import POOL, Features  # noqa: E402
from matcher.gbt import load_decider  # noqa: E402
from matcher.retrieve import Index  # noqa: E402


def jsonl(path):
    return map(json.loads, gzip.open(path, "rt") if path.endswith(".gz") else open(path))


ap = argparse.ArgumentParser()
ap.add_argument("set")
ap.add_argument("--chooser", default=os.path.join(ROOT, "models", "chooser_student.json"))
ap.add_argument("--p", help="p file; default benchmarks/data/student_p/<set>.jsonl.gz")
ap.add_argument("--out", help="default preds/<set>.jsonl")
ap.add_argument("--data", default=os.path.join(ROOT, "benchmarks", "data"))
ap.add_argument("--models", default=os.path.join(ROOT, "models"))
a = ap.parse_args()
pfile = a.p or os.path.join(a.data, "student_p", f"{a.set}.jsonl.gz")
out = a.out or os.path.join(ROOT, "preds", f"{a.set}.jsonl")
os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)

t0 = time.time()
fset = json.load(open(a.chooser)).get("fset", "v1")
F = Features(Index(os.path.join(a.models, "institutions.jsonl.gz")), os.path.join(a.models, "lineage.jsonl.gz"),
             ror_rel=os.path.join(a.models, "ror_rel.jsonl.gz") if fset == "ror" else None)
dec = load_decider(a.chooser, F)
print(f"loaded cards and chooser {os.path.basename(a.chooser)} in {time.time() - t0:.0f}s", flush=True)

S = {d["id"]: d["string"] for d in jsonl(os.path.join(a.data, f"{a.set}.jsonl.gz"))}
R = {d["id"]: {g: d.get(g, []) for g, _ in POOL} for d in jsonl(os.path.join(a.data, "pools", f"{a.set}.jsonl.gz"))}
P = {d["id"]: {i: p for i, p in d["p"]} for d in jsonl(pfile)}
keys = list(S)
n = 0
with open(out, "w") as f:
    for st in range(0, len(keys), 2000):
        chunk = keys[st:st + 2000]
        for k, (ids, _) in zip(chunk, decide_many(dec, [(S[k], P.get(k, {}), R[k]) for k in chunk])):
            f.write(json.dumps({"id": k, "ids": ids}) + "\n")
            n += 1
print(f"wrote {out}: {n:,} strings in {time.time() - t0:.0f}s")
