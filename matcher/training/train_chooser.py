"""Train the set-level chooser on the development sets (reference; this is how the shipped choosers were made).

Per (string, candidate) features (decider.Features): the candidate's p (student or Jev); its rank in each generator;
whether one of its names or acronyms appears in the string, and how long that match is; whether another candidate the
model likes (p >= 0.5) is its lineage ancestor or descendant; whether its matched name sits inside another liked
candidate's matched name; works count; how many candidates are liked; string length; and (feature set "ror") the ROR
parent, child and related links among liked candidates. Label = the candidate is in the labelled set.
Trained on dev_v1 + dev_v2; test_v1 and test_v2 are held out and only predicted.

    python matcher/training/train_chooser.py --fset ror --save chooser.pkl --json chooser.json --out preds/chooser.jsonl
    python matcher/training/train_chooser.py --p jev_p --fset ror ...      # the Jev chooser
    python matcher/training/train_chooser.py --no-model ...               # the fallback without any model

Needs scikit-learn and numpy. The shipped choosers were trained with scikit-learn 1.9.1 and numpy 2.5; with those
versions this script rebuilds them exactly. Writes the dev sets' out-of-fold predictions and the test sets'
predictions (for matcher.score), a pickle, and the JSON export that matcher.gbt loads.
"""
import argparse
import gzip
import hashlib
import json
import os
import pickle
import sys
from collections import defaultdict

import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from matcher.decider import FEATURES, NO_P, POOL, ROR_FEATURES, ROR_NO_P, Features  # noqa: E402
from matcher.gbt import to_json  # noqa: E402
from matcher.retrieve import Index  # noqa: E402

SETS = ["test_v1", "dev_v1", "dev_v2", "test_v2"]  # the order the shipped choosers saw (it fixes the row order)


def jsonl(path):
    return map(json.loads, gzip.open(path, "rt") if path.endswith(".gz") else open(path))


ap = argparse.ArgumentParser()
ap.add_argument("--t", type=float, default=0.5)
ap.add_argument("--train", default="dev_v1,dev_v2")
ap.add_argument("--p", default="student_p", help="p source under benchmarks/data/: student_p or jev_p")
ap.add_argument("--no-model", action="store_true", help="no p feature; 'liked' = every pooled candidate")
ap.add_argument("--fset", default="v1", choices=["v1", "ror"], help="ror = v1 + ROR parent/child/related features")
ap.add_argument("--out", default=os.path.join(ROOT, "preds", "chooser.jsonl"))
ap.add_argument("--save", help="pickle the dev-trained chooser here")
ap.add_argument("--json", help="also write its JSON export here (for matcher.gbt.load_decider)")
ap.add_argument("--name", default="chooser")
ap.add_argument("--data", default=os.path.join(ROOT, "benchmarks", "data"))
ap.add_argument("--models", default=os.path.join(ROOT, "models"))
a = ap.parse_args()

ror_rel = os.path.join(a.models, "ror_rel.jsonl.gz")
F = Features(Index(os.path.join(a.models, "institutions.jsonl.gz")), os.path.join(a.models, "lineage.jsonl.gz"),
             ror_rel=ror_rel if a.fset == "ror" else None)
Q, J, C = [], defaultdict(dict), {}
for s in SETS:
    for d in jsonl(os.path.join(a.data, f"{s}.jsonl.gz")):
        Q.append({"set": s, "key": d["id"], "string": d["string"], "gold": d["institutions"]})
    for d in jsonl(os.path.join(a.data, a.p, f"{s}.jsonl.gz")):
        for i, p in d["p"]:
            J[d["id"]][i] = p
    for d in jsonl(os.path.join(a.data, "pools", f"{s}.jsonl.gz")):
        C[d["id"]] = {g: d.get(g, []) for g, _ in POOL}

train = set(a.train.split(","))
X, y, meta = [], [], []
for q in Q:
    G = set(q["gold"])
    for i, f in F.rows(q["string"], J.get(q["key"], {}), C[q["key"]], a.no_model, a.fset):
        X.append(f); y.append(i in G); meta.append((q["set"], q["key"], i))
X, y = np.array(X, dtype=float), np.array(y)
tr = np.array([m[0] in train for m in meta])
clf = HistGradientBoostingClassifier(max_iter=400, learning_rate=0.05, max_leaf_nodes=31, random_state=1363)
clf.fit(X[tr], y[tr])
# out-of-fold predictions for the training sets, so their per-stratum scores are honest
p = np.zeros(len(y))
p[~tr] = clf.predict_proba(X[~tr])[:, 1]
keys = np.array([int(m[1]) % 5 for m in meta])  # deterministic folds by string id
for f in range(5):
    m = tr & (keys == f)
    c = HistGradientBoostingClassifier(max_iter=400, learning_rate=0.05, max_leaf_nodes=31, random_state=1363)
    c.fit(X[tr & (keys != f)], y[tr & (keys != f)])
    p[m] = c.predict_proba(X[m])[:, 1]
out = defaultdict(set)
for (st, k, i), pp in zip(meta, p):
    out[(st, k)]
    if pp >= a.t:
        out[(st, k)].add(i)
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
with open(a.out, "w") as f:
    for q in Q:  # strings with no candidates get an empty answer
        f.write(json.dumps({"set": q["set"], "id": q["key"], "ids": sorted(out.get((q["set"], q["key"]), set()))}) + "\n")
frozen = {"clf": clf, "t": a.t, "no_p": a.no_model, "pool": POOL,
          "features": ([FEATURES[j] for j in NO_P] if a.no_model else FEATURES) +
          (([ROR_FEATURES[j] for j in ROR_NO_P] if a.no_model else ROR_FEATURES) if a.fset == "ror" else []),
          "fset": a.fset, "train": sorted(train), "decider": a.name, "sklearn": __import__("sklearn").__version__}
if a.fset == "ror":
    frozen["ror_rel_sha256"] = hashlib.sha256(open(ror_rel, "rb").read()).hexdigest()
if a.save:
    pickle.dump(frozen, open(a.save, "wb"))
if a.json:
    json.dump(to_json(frozen), open(a.json, "w"))
print(f"{len(y):,} (string, candidate) rows, {tr.sum():,} train; wrote {a.out}")
