"""The chooser over many strings with one predict_proba call per chunk. Same ids and probabilities as calling
Decider.decide string by string (checked on test v2: 20,000 of 20,000), about 8 times faster."""
import numpy as np


def decide_many(dec, items):
    """items: [(s, js, ranks)] -> [(ids, probs)]. dec = a decider.Decider (or gbt.load_decider)."""
    rows, spans = [], []
    for s, js, ranks in items:
        R = dec.F.rows(s, js, ranks, dec.m["no_p"], getattr(dec, "fset", "v1"))
        spans.append((len(rows), len(rows) + len(R), R))
        rows.extend(f for _, f in R)
    P = dec.m["clf"].predict_proba(np.asarray(rows, dtype=float))[:, 1] if rows else []
    out = []
    for a, b, R in spans:
        probs = {i: float(p) for (i, _), p in zip(R, P[a:b])}
        out.append((sorted(i for i, p in probs.items() if p >= dec.m["t"]), probs))
    return out
