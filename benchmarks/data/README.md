# Benchmark data

Our test and development sets, with labels, the candidates the matcher considered for each string, and the scores
it gave them. With these files anyone can rerun the matcher's last step and score it on a laptop, without
Elasticsearch, the OpenAlex corpus or a GPU. [REPRODUCE.md](../../REPRODUCE.md) says how.
The sets made by others are in [external/](external/).

| Set | Strings | High confidence | What it is |
|---|---:|---:|---|
| `test_v2` | 20,000 | 17,906 | Our benchmark. Drawn at random from OpenAlex's affiliation strings that have at least one work, leaving out the strings in the sets below. |
| `test_v1` | 20,000 | 17,736 | An earlier random draw, the same way. |
| `dev_v1` | 5,615 | 4,796 | Development set, drawn by failure mode (strata). The chooser was trained on it. |
| `dev_v2` | 5,666 | 4,824 | A second development set, more strata. The chooser was trained on it too. |

Nothing was trained on either test set. The student's training sample (200,000 other random strings) is a
release asset; see [REPRODUCE.md](../../REPRODUCE.md).

## The files

All are gzipped JSON lines, one line per string, in the same order in every file. `id` joins them.

**`<set>.jsonl.gz`**: the strings and their labels.

- `id`, `string` (as in OpenAlex), `works_count` (works with this string when drawn).
- `institutions`: the labelled answer, OpenAlex institution ids. Empty means the string names no institution that
  has a record.
- `confidence`: the labeller's confidence, `high`, `medium` or `low`. Headline scores use `high`.
- `is_affiliation`: false for text that is not an affiliation (a name, a sentence, junk).
- `mentions`: every organisation the labeller found, with the text span, a kind (`institution`, `unit_no_record`,
  `org_no_record`, `email_domain`, `not_affiliation`), the institution id where there is one, a confidence and a
  one-line reason. `candidate` is the card number the labeller saw (C1, C2, ...).
- `label_source`: `label` (first pass); `dispute` (a second model disagreed and the two converged); `residual` (they
  did not converge: the first model's label is kept at low confidence); `resolved` (settled by hand); `completion`
  (changed by a later pass that looked for missed institutions; `completion_residual` if that pass did not
  converge); `corrected` (fixed by hand).
- `instructions`: which version of the labelling rules applied (`labelling/instructions_v3.md` to `v5`). `v6` is the
  current version; it adds one rule ("Faculté de ..., City").
- `unresolved`: institution mentions the labeller could not match to a record (usually 0).
- `strata` (dev sets only): the failure modes the string was drawn for. `qa_*` strata follow the categories of an
  internal quality review; `roracle_*` strata come from [RORacle](https://github.com/ourresearch/RORacle)'s test cases.
- `system_2023`: OpenAlex's answer until 27 September 2026 (the 2023 classifier, hand-written rules and curations),
  scored beside the new matcher.

**`pools/<set>.jsonl.gz`**: the candidates. For each of the four generators, its top ids in rank order, as many as
the pool uses: `lex2` (10), `neighbour` (5), `dense_me5b_chunks` (10), `top5` (5). The pool is their union, first
occurrence wins, less any id without a card in `models/institutions.jsonl.gz`. The chooser also uses the ranks.

**`student_p/<set>.jsonl.gz`**: `p`, a list of `[institution id, p]` for every pool candidate: the student's
probability that the string names that institution, rounded to 4 decimals, as the chooser saw it. Computed once on
an H100 with the released student.

**`jev_p/<set>.jsonl.gz`**: the same pairs scored by Jev, the commercial model the student learned from. Only for
checking the Jev chooser (`models/chooser_jev.json`); nothing in the reproduction needs it.

**`successors.json`**: ROR successor links (predecessor id: successor ids). The scorer counts a predecessor's
successor as over-general, not wrong.

**`labelling/`**: the labelling instructions, one file per version.

## How the labels were made

Claude Opus 5.5 labelled every string, one call per string, under the instructions in `labelling/`. It saw the
string and up to 45 numbered institution cards: lexical and acronym candidates (`matcher/retrieve.py`) plus every
institution the 2023 system had given the string. When it named an organisation it could not find among the cards,
we searched for that name and asked once more with the new cards. Claude Fable 5.1 labelled a sample of each set
too (about 2,000 strings of each test set). Where the two disagreed, each saw the other's label and reasons and
labelled again. Labels they converged on were kept; the rest keep the first label at low confidence, and a few were
settled by hand. A last pass looked for institutions the first had missed. The labeller never saw which system
proposed a card.

## License

Our sets and labels: [CC0](https://creativecommons.org/publicdomain/zero/1.0/), like all OpenAlex data.
