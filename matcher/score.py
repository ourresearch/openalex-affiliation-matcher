"""Score predictions against the labelled benchmark sets.

    python -m matcher.score test_v2 --conf high --pred new_matcher=preds/test_v2.jsonl
    python -m matcher.score dev_v1 --strata --pred preds/dev_v1.jsonl

A prediction file has one JSON line per string: {"id": ..., "ids": [OpenAlex institution ids]} (.jsonl or .jsonl.gz).
The 2023 system (OpenAlex's answers before the switch) is always scored beside it, from the set file.

Each predicted id is: correct | over_general (a lineage ancestor of a labelled id, or the known parent of a unit
that has no record) | context (the labeller saw it only in an email domain or in text that is not an affiliation) |
sibling (shares a lineage with a labelled id; still counted as hallucinated) | hallucinated. Precision and recall count
only `correct`; "P lenient" also accepts over_general. Exact set = the predicted set equals the labelled set.
"Strings with a hallucination" = strings with at least one hallucinated id.
"""
import argparse
import gzip
import json
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def jsonl(path):
    return map(json.loads, gzip.open(path, "rt") if path.endswith(".gz") else open(path))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("set", help="test_v1, test_v2, dev_v1 or dev_v2")
    ap.add_argument("--conf", help="high = only strings whose label confidence is high")
    ap.add_argument("--strata", action="store_true", help="dev sets: exact / P / R per stratum")
    ap.add_argument("--pred", action="append", default=[], help="[name=]path; repeatable")
    ap.add_argument("--data", default=os.path.join(ROOT, "benchmarks", "data"))
    ap.add_argument("--lineage", default=os.path.join(ROOT, "models", "lineage.jsonl.gz"))
    a = ap.parse_args()

    anc = defaultdict(set)
    for d in jsonl(a.lineage):
        anc[d["id"]] = set(d["lineage"]) - {d["id"]}
    SUCC = {int(k): v for k, v in json.load(open(os.path.join(a.data, "successors.json"))).items()}

    def succ_of(G):
        """All successors (transitively) of the labelled ids, from ROR successor/predecessor relationships."""
        out, todo = set(), list(G)
        while todo:
            for s in SUCC.get(todo.pop(), []):
                if s not in out:
                    out.add(s); todo.append(s)
        return out

    gold = {d["id"]: d for d in jsonl(os.path.join(a.data, f"{a.set}.jsonl.gz"))}
    systems = {"system_2023": {k: set(d["system_2023"]) for k, d in gold.items()}}
    for p in a.pred:
        name, path = p.split("=", 1) if "=" in p else (os.path.basename(p).split(".")[0], p)
        systems[name] = {d["id"]: set(d["ids"]) for d in jsonl(path)}
        missing = sum(k not in systems[name] for k in gold)
        if missing:
            print(f"warning: {name} has no line for {missing:,} of {len(gold):,} strings (scored as empty)")

    def tally(keys):
        tot = {w: defaultdict(lambda: defaultdict(float)) for w in ("strings", "works")}
        for k in keys:
            g = gold[k]
            G, ms = set(g["institutions"]), g["mentions"]
            up = set().union(*[anc[x] for x in G]) if G else set()
            up |= {m["institution_id"] for m in ms if m["kind"] == "unit_no_record" and m.get("institution_id")}
            up |= {f for m in ms for f in m.get("fallback_ids", [])}  # literal-name fallback
            up |= succ_of(G)  # a predecessor's successor (ROR): low stakes, lineage carries works there
            ctx = {m["institution_id"] for m in ms if m["kind"] in ("email_domain", "not_affiliation") and m.get("institution_id")}
            for name, S in systems.items():
                P = S.get(k, set())
                c = defaultdict(float)
                fam = set().union(*[anc[x] | {x} for x in G]) if G else set()
                for p in P:
                    kind = ("correct" if p in G else "over_general" if p in up else "context" if p in ctx else
                            "sibling" if (anc[p] | {p}) & fam else "hallucinated")
                    c[kind] += 1
                    if kind == "sibling":
                        c["hallucinated"] += 1  # a sibling is still wrong; reported apart as a softer share
                c.update(pred=len(P), gold=len(G), exact=float(P == G), n=1, none_n=float(not G),
                         none_ok=float(not G and not P), any_halluc=float(c["hallucinated"] > 0))
                for w, wt in (("strings", 1), ("works", max(int(g["works_count"] or 0), 1))):
                    for kk, v in c.items():
                        tot[w][name][kk] += v * wt
        return tot

    def table(tot, w, title):
        out = [f"\n{title} (weighted by {w})",
               "| System | n | Exact set | P | P lenient | R | F1 | Hallucinated / predicted | of which sibling | Strings with a hallucination | Over-general / predicted | None correct |",
               "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for name, c in tot[w].items():
            P = c["correct"] / c["pred"] if c["pred"] else 0
            PL = (c["correct"] + c["over_general"]) / c["pred"] if c["pred"] else 0
            R = c["correct"] / c["gold"] if c["gold"] else 0
            F = 2 * P * R / (P + R) if P + R else 0
            n = int(tot["strings"][name]["n"])
            none = f"{c['none_ok']/c['none_n']:.1%}" if c["none_n"] else "-"
            out.append(f"| {name} | {n:,} | {c['exact']/c['n']:.1%} | {P:.1%} | {PL:.1%} | {R:.1%} | {F:.1%} | "
                       f"{c['hallucinated']/max(c['pred'],1):.1%} | {c['sibling']/max(c['pred'],1):.1%} | {c['any_halluc']/c['n']:.1%} | {c['over_general']/max(c['pred'],1):.1%} | {none} |")
        return "\n".join(out)

    keys = [k for k in gold if not a.conf or gold[k]["confidence"] == a.conf]
    if not a.strata:
        tot = tally(keys)
        print(f"{a.set}: {len(keys):,} strings{' (label confidence ' + a.conf + ')' if a.conf else ''}")
        print(table(tot, "strings", "Systems"))
        print(table(tot, "works", "Systems"))
    else:
        by = defaultdict(list)
        for k in keys:
            for s in gold[k].get("strata", []):
                by[s].append(k)
        print("| Stratum | n | " + " | ".join(f"{b} exact / P / R" for b in systems) + " |")
        print("|---|---:|" + "---|" * len(systems))
        for s in sorted(by):
            t = tally(by[s])["strings"]
            cells = []
            for b in systems:
                c = t[b]
                P = c["correct"] / c["pred"] if c["pred"] else 0
                R = c["correct"] / c["gold"] if c["gold"] else 0
                cells.append(f"{c['exact']/c['n']:.0%} / {P:.0%} / {R:.0%}")
            print(f"| {s} | {len(by[s])} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    main()
