"""Candidate generators: the four ranked lists the pool is built from (decider.POOL).

Copied from the production nightly with the logic unchanged, so a new string gets the same kind of candidates the
benchmark scored. Each generator returns institution ids in rank order.

    lex2        lexical coverage of the institution's names + acronyms (retrieve.Index). Needs only the cards file.
    dense_me5b_chunks
                multilingual-e5-base embeddings of the whole string and of its comma-separated pieces, against every
                name variant as "name, city, country"; an institution scores its best match. Needs the cards file and
                the public base model from the Hugging Face Hub. A GPU helps; a CPU works for small batches.
    neighbour   the institutions of the 30 most similar other strings in OpenAlex's Elasticsearch index of raw
                affiliation strings. Needs such an index (not public); see neighbour_all() for the query.
    top5        the 2023 model's stored top 5 for the string. Only strings OpenAlex saw before 2026 have one.

A generator that is missing for a string is simply an empty list: the chooser then sees rank 99 for it, as it did in
training whenever a generator had nothing.

    from matcher.retrieve import Index
    from matcher import candidates as cg
    ix = Index("models/institutions.jsonl.gz")
    ranks = {"lex2": cg.lex2(ix, s), "dense_me5b_chunks": cg.dense_chunks_all([s], cg.names_for_dense(ix))[0][0],
             "neighbour": [], "top5": []}
    pool = cg.candidates(ix, ranks)       # the ids the student scores
"""
import json
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

from .decider import pool


def names_for_dense(ix):
    """Every name variant as "name, city, country" (the dense generator's targets)."""
    out = []
    for iid, d in ix.inst.items():
        place = ", ".join(x for x in (d["city"], d["country"]) if x)
        for n in dict.fromkeys([d["name"]] + d["alts"]):
            out.append((iid, f"{n}, {place}" if place else n))
    return out


def lex2(ix, s):
    """Lexical top 100 + acronyms (up to 10 per acronym) at 0.4."""
    seen = dict(ix.lexical(s, k=100))
    for iid in ix.acronyms(s, per=10):
        seen.setdefault(iid, 0.4)
    return [i for i, _ in sorted(seen.items(), key=lambda x: -x[1])][:100]


def neighbour_all(strings, es_url, threads=32):
    """Elasticsearch index raw-affiliation-strings-v3: the 30 nearest other strings with works, each hit's
    institution_ids_final voted with weight (score/top)^4. None = the search failed after retries.
    Reference only: the index is OpenAlex's own. One could build a similar index from the OpenAlex snapshot
    (raw affiliation strings with the institutions assigned to them)."""
    import requests
    url = es_url.rstrip("/") + "/raw-affiliation-strings-v3/_search"
    S = requests.Session()

    def one(s):
        body = {"size": 30, "_source": ["institution_ids_final", "works_count"],
                "query": {"bool": {"must": {"match": {"raw_affiliation_string": s[:1000]}},
                                   "must_not": {"term": {"raw_affiliation_string.keyword": s}},
                                   "filter": {"range": {"works_count": {"gt": 0}}}}}}
        for a in range(5):
            try:
                r = S.post(url, json=body, timeout=60)
                r.raise_for_status()
                hits = r.json()["hits"]["hits"]
                break
            except Exception:
                time.sleep(2 ** a)
        else:
            return None
        if not hits:
            return []
        top = hits[0]["_score"]
        sc = defaultdict(float)
        for h in hits:
            w = (h["_score"] / top) ** 4
            for i in h["_source"].get("institution_ids_final") or []:
                i = int(str(i).lstrip("I"))
                if i > 0:
                    sc[i] += w
        return [i for i, _ in sorted(sc.items(), key=lambda x: -x[1])][:100]

    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(one, strings))


def pieces(s):
    """1-2 consecutive ; , ( ) segments, at most 16."""
    parts = [p.strip() for p in re.split(r"[;,()\n|]|\s-\s", s) if len(p.strip()) >= 3]
    wins = parts + [parts[i] + ", " + parts[i + 1] for i in range(len(parts) - 1)]
    return list(dict.fromkeys(w for w in wins if w != s))[:16]


def dense_chunks_all(strings, names, model_name="intfloat/multilingual-e5-base", prefix="query: ", maxlen=128,
                     device=None, name_emb=None, batch_size=256):
    """Whole string + pieces, exact inner product against every name variant, institution score = max over its
    variants and the string's pieces; top 100 ids per string. Returns (ranks, name_emb) so the caller can cache the
    name embeddings (about 266K names)."""
    import numpy as np
    import torch
    from sentence_transformers import SentenceTransformer
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    m = SentenceTransformer(model_name, device=device)
    m.max_seq_length = maxlen
    if device == "cuda":
        m.half()
    enc = lambda xs: m.encode([prefix + x for x in xs], batch_size=batch_size, normalize_embeddings=True,
                              convert_to_tensor=True, show_progress_bar=False)
    nid = np.array([i for i, _ in names])
    N = name_emb if name_emb is not None else enc([t for _, t in names])
    N = N.to(device)
    texts, owner = [], []
    for qi, s in enumerate(strings):
        for p in [s[:2000]] + pieces(s):
            texts.append(p)
            owner.append(qi)
    E = enc(texts)
    if device != "cuda":
        E, N = E.float(), N.float()
    best = [dict() for _ in strings]
    K = 200
    for st in range(0, E.shape[0], 4096):
        v, ix = (E[st:st + 4096] @ N.T).topk(K, dim=1)
        v, ix = v.float().cpu().numpy(), ix.cpu().numpy()
        for r in range(v.shape[0]):
            b = best[owner[st + r]]
            for sc, k in zip(v[r], ix[r]):
                iid = int(nid[k])
                if sc > b.get(iid, -9):
                    b[iid] = float(sc)
    return [sorted(b, key=lambda i: -b[i])[:100] for b in best], N.cpu()


def top5_from_model_response(mr):
    """The 2023 model's stored top 5 (ids > 0)."""
    if not mr:
        return []
    if isinstance(mr, str):
        mr = json.loads(mr)
    return [int(x["id"]) for x in mr if int(x["id"]) > 0]


def candidates(ix, ranks):
    """The pool (decider.pool) restricted to institutions with a card: the pairs the student scores."""
    return [i for i in pool(ranks) if i in ix.inst]
