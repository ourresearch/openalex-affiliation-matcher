# External benchmark sets

Five public test sets from outside our own benchmark, with their labels and the answers of every system we
scored. Run `python3 scripts/score_external.py` from the repo root to reproduce the external numbers in
[benchmarks/README.md](../../README.md). It needs only the Python standard library.

| Folder | Strings | Source | License |
|---|---:|---|---|
| `crossref_2024` | 3,000 | [Crossref Marple](https://gitlab.com/crossref/marple); the same items are in [ror-affiliation-matching-eval](https://github.com/adambuttrick/ror-affiliation-matching-eval) | MIT (Crossref) |
| `springer_nature_2023` | 3,000 (2,999 distinct) | [Crossref Marple](https://gitlab.com/crossref/marple) | MIT (Crossref) |
| `cwts` | 952 | Chosen by CWTS at Leiden University, labelled by OpenAlex, released by OurResearch in 2023 in [openalex-institution-parsing](https://github.com/ourresearch/openalex-institution-parsing/tree/main/V2) | None attached; see `cwts/NOTICE` |
| `ror_api_logs_2023` | 690 | [affiliation-matching-experimental](https://github.com/ror-community/affiliation-matching-experimental) | MIT (ROR) |
| `crossref_publisher_2023` | 6,747 (6,708 distinct) | [affiliation-matching-experimental](https://github.com/ror-community/affiliation-matching-experimental) | MIT (ROR) |

Each folder's `LICENSE` or `NOTICE` names the exact source files and commits.

## The files

`<folder>/strings.jsonl.gz` has one line per item:

- `id`: the folder name and the item's number in the source (Marple's `seq_no`, the CSV row counted from 0, or for
  CWTS the order of first appearance).
- `string`: the affiliation string as released.
- `labels`: the set's labels. An empty list means the labels say the string names no institution (`NP` in the 2023
  sets).
- `system_2023`: OpenAlex's answers until 27 September 2026 (the 2023 classifier, hand-written rules and
  curations). `null` means OpenAlex had no answer row for the string; it scores as an empty answer.
- `new_matcher`: the new matcher as anyone can run it (the small model and the chooser, no Jev).
- `new_matcher_most_confident`: its single most confident institution (ROR's four sets only), to compare under the
  labels' one-institution-per-string convention.
- `ror_matcher`: ROR's matcher. On Crossref 2024 and Springer Nature 2023, ROR's published single-search results of
  7 January 2025. On the 2023 sets, ROR's own 2023 run of its affiliation service. On CWTS, the live service
  (single search) on 27 September 2026.
- CWTS only: `source_file`, `openalex_work` (the work the string came from), `cwts_institutions` (the institutions
  CWTS listed) and `labels_as_released` (the 2023 ids, before two merges).

Every label and answer is `{"openalex": "I…", "ror": "https://ror.org/…"}`. ROR's sets were released with ROR ids
and we added the OpenAlex record for each; CWTS was released with OpenAlex ids and we added the ROR ids. Either id
can be `null` when the other has no counterpart. For the 2023 system on ROR's sets, a record that has since been
merged is given as the record it merged into, as it was scored.

`judge_verdicts.jsonl.gz` has one line per judged pair: `set`, `string`, `institution` (OpenAlex id),
`institution_ror`, `institution_name`, `named_by` (the systems that named it), `verdict`, `reason` (the judge's
own words) and `model`. The prompt is in [judge_prompt.md](judge_prompt.md).

## How truth is built

The labels usually list one institution per string, and sometimes none, even when a string names more. Wherever a
system named an institution the labels lack, Claude Opus 5.5 judged whether the string names it, without knowing
which system named it. It judged 1,785 such pairs and said "names it" for 874. Truth for a string is its labels
plus those confirmed institutions, the same for every system. The script also prints scores on the labels alone.

## Contamination check

We looked for every external string in our development sets, our test sets and the small model's training
sample, both exactly and ignoring case and spacing. The strings found in the development sets (all 952 CWTS
strings and 33 of the 13,308 in ROR's sets) were removed and the chooser was retrained without them; every
`new_matcher` answer here comes from that retrained chooser. The small model's training sample held 27 of ROR's
strings; leaving them out moves the new matcher's scores by 0.1 point at most.
