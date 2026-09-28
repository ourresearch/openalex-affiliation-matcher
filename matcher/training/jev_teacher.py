"""The question the teacher answered for every (string, candidate) pair (reference only).

Jev is TypeSafe's commercial decision model. It is NOT needed to reproduce the benchmark: the student learned from
Jev's answers, and those answers are released (train_v1_jev_labels.jsonl.gz). This file records exactly what Jev
was asked, so the labels can be read correctly. Model jev-1.13.0; one call per pair; the answer is a calibrated
probability ("noul" question type) that the string names the institution, used as the pair's p.

The same question and card score the Jev tier of the production nightly (models/chooser_jev.json is the chooser
trained on Jev's p instead of the student's; benchmarks/data/jev_p/ holds Jev's p for every benchmark pool pair).
"""

NAMES_IT = ("Does this affiliation string say the author is affiliated with the institution shown? Answer yes if the string names the institution "
    "(by any of its names, other names, acronyms, former names or obvious typos) or a unit that is part of it (campus, school, college, department, "
    "institute, lab, center, hospital). Answer no if the string names only a different organization (including one with a similar name or the same "
    "acronym elsewhere), only a place, only a person, or no organization at all. Several organizations may be listed; answer yes if any of them is this "
    "institution or a unit of it. A unit name counts only when the string does not present it as belonging to a different organization, and an acronym "
    "counts only when the string does not spell it out as, or attach it to, a different organization. An organization merely located on the institution's "
    "campus, or a fellowship, prize or degree named after it, is not an affiliation.")
QUESTIONS = {"names_this_institution": {"type": "noul", "instructions": NAMES_IT}}


def jev_card(ix, i):
    """The institution as Jev saw it (from retrieve.Index)."""
    d = ix.inst[i]
    return {"name": d["name"], "other_names": d["alts"][:6], "acronyms": d["acr"][:4],
            "type": d["type"], "city": d["city"], "country": d["country"]}


def request(ix, string, i):
    """One pair's request: state + questions. p = response["answers"]["names_this_institution"]["noul"]."""
    return {"model": "jev-1.13.0", "state": {"affiliation_string": string, "institution": jev_card(ix, i)},
            "questions": QUESTIONS}
