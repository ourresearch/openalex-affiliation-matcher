"""Score the 2023 system, the new matcher and ROR's matcher on the external benchmark sets.

    python3 scripts/score_external.py

Reads benchmarks/data/external/ and prints the external rows of benchmarks/README.md. Standard library only.

How each number is defined:

- Judged scores ("Results by set") use OpenAlex ids. Truth for a string is the set's labels plus every institution
  any of the three systems named that the blind judge said the string names (verdict "names_it"). A named
  institution counts as right when it is in the labels or the judge confirmed it; "names_unit_of_it", "unsure", "no"
  and an institution with no OpenAlex record count as wrong. Precision = right links / links named. Recall = label
  links named / label links. F-score = the harmonic mean of the two. Exact match = the answer equals the truth set.
- Precision and recall count every item in a set; exact match counts each distinct string once (Springer Nature 2023
  lists one string twice). "Pooled" adds up the three sets.
- ROR's metric (Crossref Marple, crossref_matcher/evaluation/evaluation.py): micro precision, recall, F1 and F0.5
  over (item, ROR id) pairs, labels as given, every item counted. An item with no labels and no answer adds nothing.
- ROR's 2023 metric (ror-community/affiliation-matching-experimental, f-scores/calculate_f_score.py): one id per
  string. A right id is a true positive, a wrong id a false positive, no id a false negative, or a true negative
  when the labels say no match.
"""
import gzip
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT = os.path.join(ROOT, "benchmarks", "data", "external")
SYSTEMS = [("system_2023", "2023 system"), ("new_matcher", "New matcher"), ("ror_matcher", "ROR's matcher")]
JUDGED_SETS = [("crossref_2024", "Crossref 2024"), ("springer_nature_2023", "Springer Nature 2023"), ("cwts", "CWTS")]


def jsonl(path):
    with (gzip.open(path, "rt", encoding="utf-8") if path.endswith(".gz") else open(path, encoding="utf-8")) as f:
        return [json.loads(line) for line in f]


def load(name):
    return jsonl(os.path.join(EXT, name, "strings.jsonl.gz"))


def ids(answers, space):
    """The ids of one answer in one id space. An institution with no id in that space gets a placeholder that never
    matches a label, so it counts as a wrong link."""
    other = "ror" if space == "openalex" else "openalex"
    return {a[space] or f"none:{a[other]}" for a in answers or []}


def labels(row, space):
    return {x[space] for x in row["labels"] if x[space]}


def pct(x):
    return f"{100 * x:.1f}"


def harmonic(p, r, beta=1.0):
    b2 = beta * beta
    return (1 + b2) * p * r / (b2 * p + r) if p + r else 0.0


# ---- judged scores: labels plus judge-confirmed links, OpenAlex ids

def judged_counts(rows, confirmed):
    c = {s: dict(tp=0, fn=0, ok=0, bad=0, exact=0, exact_labels=0) for s, _ in SYSTEMS}
    seen, strings = set(), 0
    for r in rows:
        G = labels(r, "openalex")
        pred = {s: ids(r[s], "openalex") for s, _ in SYSTEMS}
        for s, P in pred.items():
            c[s]["tp"] += len(P & G)
            c[s]["fn"] += len(G - P)
            for x in P - G:
                c[s]["ok" if (x, r["string"]) in confirmed else "bad"] += 1
        if r["string"] in seen:
            continue
        seen.add(r["string"])
        strings += 1
        T = G | {x for P in pred.values() for x in P - G if (x, r["string"]) in confirmed}
        for s, P in pred.items():
            c[s]["exact"] += P == T
            c[s]["exact_labels"] += P == G
    return strings, c


def judged_metrics(strings, c):
    named = c["tp"] + c["ok"] + c["bad"]
    p = (c["tp"] + c["ok"]) / named if named else 0.0
    r = c["tp"] / (c["tp"] + c["fn"]) if c["tp"] + c["fn"] else 0.0
    return dict(exact=c["exact"] / strings, exact_labels=c["exact_labels"] / strings, precision=p, recall=r,
                f=harmonic(p, r))


# ---- ROR's metrics, ROR ids, labels as given

def ror_metric(rows, field):
    tp = fp = fn = 0
    for r in rows:
        G, P = labels(r, "ror"), ids(r[field], "ror")
        tp += len(P & G)
        fp += len(P - G)
        fn += len(G - P)
    p = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    return p, rec, harmonic(p, rec), harmonic(p, rec, 0.5)


def ror_2023_metric(rows, field):
    tp = fp = fn = tn = 0
    for r in rows:
        G = labels(r, "ror")
        pred = sorted(ids(r[field], "ror"))
        assert len(pred) <= 1, (r["id"], pred)
        if pred and pred[0] in G:
            tp += 1
        elif pred:
            fp += 1
        elif not G:
            tn += 1
        else:
            fn += 1
    p = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    return p, rec, harmonic(p, rec), harmonic(p, rec, 0.5)


def table(header, rows):
    widths = [max(len(str(x)) for x in col) for col in zip(header, *rows)]
    line = lambda xs: "  ".join(str(x).ljust(w) if i < 2 else str(x).rjust(w) for i, (x, w) in enumerate(zip(xs, widths)))
    print(line(header))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print(line(r))
    print()


def main():
    verdicts = jsonl(os.path.join(EXT, "judge_verdicts.jsonl.gz"))
    confirmed = {(v["institution"], v["string"]) for v in verdicts if v["verdict"] == "names_it"}
    data = {name: load(name) for name, _ in JUDGED_SETS}

    counts = {name: judged_counts(data[name], confirmed) for name, _ in JUDGED_SETS}
    pooled_strings = sum(n for n, _ in counts.values())
    pooled = {s: {k: sum(counts[name][1][s][k] for name, _ in JUDGED_SETS) for k in counts["cwts"][1][s]}
              for s, _ in SYSTEMS}
    scopes = [("External, pooled", pooled_strings, pooled)] + [(label, *counts[name]) for name, label in JUDGED_SETS]

    print("Results by set: truth = the set's labels plus the institutions the blind judge confirmed")
    print(f"({len(verdicts):,} judge verdicts, {len(confirmed):,} confirmed)\n")
    rows = []
    for label, n, c in scopes:
        for s, sname in SYSTEMS:
            m = judged_metrics(n, c[s])
            rows.append([f"{label} ({n:,})" if s == SYSTEMS[0][0] else "", sname, pct(m["exact"]), pct(m["precision"]),
                         pct(m["recall"]), pct(m["f"])])
    table(["Benchmark", "System", "Exact match", "Precision", "Recall", "F-score"], rows)

    print("On the external labels alone: exact match without the judge\n")
    rows = []
    for label, n, c in scopes[1:] + scopes[:1]:
        rows.append([label, ""] + [pct(judged_metrics(n, c[s])["exact_labels"]) for s, _ in SYSTEMS])
    table(["Benchmark", ""] + [sname for _, sname in SYSTEMS], rows)

    print("ROR's metric: micro precision, recall, F1 and F0.5 over (item, ROR id) pairs, labels as given\n")
    rows = []
    for name, label in JUDGED_SETS[:2]:
        for k, (field, sname) in enumerate([("new_matcher", "New matcher"),
                                            ("new_matcher_most_confident", "New matcher, most confident id"),
                                            ("system_2023", "2023 system"), ("ror_matcher", "ROR's matcher")]):
            rows.append([label if k == 0 else "", sname] + [pct(x) for x in ror_metric(data[name], field)])
    table(["Benchmark", "System", "Precision", "Recall", "F1", "F0.5"], rows)

    print("ROR's 2023 sets, ROR's 2023 metric (one id per string)\n")
    rows = []
    for name, label in [("ror_api_logs_2023", "ROR API logs 2023"),
                        ("crossref_publisher_2023", "Crossref publisher-asserted 2023")]:
        d = load(name)
        for k, (field, sname) in enumerate([("new_matcher_most_confident", "New matcher, most confident id"),
                                            ("ror_matcher", "ROR's affiliation service, ROR's 2023 run")]):
            rows.append([f"{label} ({len(d):,})" if k == 0 else "", sname] + [pct(x) for x in ror_2023_metric(d, field)])
    table(["Benchmark", "System", "Precision", "Recall", "F1", "F0.5"], rows)


if __name__ == "__main__":
    main()
