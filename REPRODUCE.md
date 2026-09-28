# Reproduce the benchmark

Three paths, easiest first. The first takes a few minutes on a laptop and gives the headline number: **89.6% exact
match on our benchmark** (test v2, the 17,906 strings labelled with high confidence). None of the paths needs Jev,
Elasticsearch, the OpenAlex corpus or any private resource.

The matcher has three steps. **Candidates:** four generators each rank institutions for the string; their top ids
form a pool of about 19. **Student:** a small model (multilingual-e5-base, fine-tuned) gives each (string,
candidate) pair a probability that the string names the institution. **Chooser:** gradient-boosted trees look at
the whole pool at once (the probabilities, the ranks, names found in the string, parent and child links) and keep
the institutions it rates 0.5 or higher.

## 1. On a laptop, in minutes (CPU)

The repo holds every test string's candidate pool and the student's probability for every pair, so only the
chooser runs. You need Python 3.10 or later and numpy.

```bash
git clone https://github.com/ourresearch/openalex-affiliation-matcher
cd openalex-affiliation-matcher
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python scripts/decide.py test_v2
python -m matcher.score test_v2 --conf high --pred new_matcher=preds/test_v2.jsonl
```

`decide.py` takes under a minute. The score table's first rows should read:

```
test_v2: 17,906 strings (label confidence high)

Systems (weighted by strings)
| System | n | Exact set | P | P lenient | R | F1 | Hallucinated / predicted | of which sibling | Strings with a hallucination | Over-general / predicted | None correct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| system_2023 | 17,906 | 73.5% | 82.3% | 84.1% | 82.6% | 82.5% | 15.3% | 1.1% | 14.4% | 1.7% | 68.1% |
| new_matcher | 17,906 | 89.6% | 93.3% | 94.8% | 95.4% | 94.4% | 4.5% | 0.8% | 4.5% | 1.6% | 90.4% |
```

`system_2023` is OpenAlex's answer before the switch. The second table weights each string by its works. Your
answers should equal the frozen matcher's string for string (we checked: 20,000 of 20,000).

More from the same files:

| Command | Exact set, high confidence |
|---|---:|
| `python scripts/decide.py test_v1` then `python -m matcher.score test_v1 --conf high --pred preds/test_v1.jsonl` | 90.2% |
| `python scripts/decide.py test_v2 --chooser models/chooser_no_model.json --out preds/no_model.jsonl` (no model at all) | 82.5% |
| `python scripts/decide.py test_v2 --chooser models/chooser_jev.json --p benchmarks/data/jev_p/test_v2.jsonl.gz --out preds/jev.jsonl` (Jev's probabilities, for reference) | 90.2% |
| `python3 scripts/score_external.py` (the external sets; standard library only) | see [benchmarks/](benchmarks/README.md) |

Drop `--conf high` to score all 20,000 strings. `python -m matcher.score dev_v2 --strata --pred ...` scores the
development sets by stratum (their chooser answers are not held out: the chooser was trained on them).

## 2. Recompute the student's scores (GPU)

This replaces the shipped probabilities with ones you compute from the released weights.

```bash
curl -LO https://github.com/ourresearch/openalex-affiliation-matcher/releases/download/v3.0.0/student_model.tar.gz
shasum -a 256 student_model.tar.gz    # 8180d696be44667da2e8426369489fc23903eff57bdf12717fb4efdb19ec3599
tar -xzf student_model.tar.gz         # -> student_model/
pip install torch==2.6.0 "transformers>=4.51,<5" sentencepiece huggingface_hub
python scripts/student_scores.py test_v2 --model student_model
python scripts/decide.py test_v2 --p preds/student_p_test_v2.jsonl.gz --out preds/test_v2_recomputed.jsonl
python -m matcher.score test_v2 --conf high --pred new_matcher=preds/test_v2_recomputed.jsonl
```

`student_scores.py` scores the 376,065 pairs of test v2 and compares them with the shipped ones. It fetches the
public base model's config and weights from the Hugging Face Hub at a pinned revision (the fine-tuned weights then
replace every weight). torch 2.6.0 needs Python 3.13 or earlier. On one H100 the script took 50 seconds; the
recomputed probabilities differed from the shipped ones by at most 0.0045, no pair crossed 0.5, and the answers and
the score were identical (89.6%).

On a CPU the same script works but takes over an hour for the full set; `--limit 300` checks the first 300 strings
(5,697 pairs) in about a minute. A CPU runs the student in fp32 rather than bf16, so its probabilities differ
slightly: on those 300 strings the mean difference was 0.0004 and 2 of 5,697 pairs crossed 0.5.

## 3. Reference: new strings, and training

### Candidates for a new string

`matcher/candidates.py` has the four generators the production matcher uses:

| Generator | Pool | Needs |
|---|---:|---|
| `lex2`: names and acronyms of the institution found in the string | top 10 | `models/institutions.jsonl.gz` |
| `dense_me5b_chunks`: multilingual-e5-base embeddings of the string and its pieces against every institution name | top 10 | the cards file and the public base model; embedding the 266K names once takes a few minutes on a GPU |
| `neighbour`: institutions of the 30 most similar strings already in OpenAlex | top 5 | OpenAlex's Elasticsearch index of affiliation strings (not public) |
| `top5`: the 2023 model's stored top 5 | top 5 | only strings OpenAlex saw before the switch |

A missing generator is an empty list; the chooser then sees no rank for it, as it did in training whenever a
generator had nothing. New strings in the production nightly get `lex2`, `dense_me5b_chunks` and `neighbour`.
For the benchmark strings, all four lists are in `benchmarks/data/pools/`.

```python
from matcher import candidates as cg, student
from matcher.batch import decide_many
from matcher.decider import Features
from matcher.gbt import load_decider
from matcher.retrieve import Index

ix = Index("models/institutions.jsonl.gz")
F = Features(ix, "models/lineage.jsonl.gz", ror_rel="models/ror_rel.jsonl.gz")
chooser = load_decider("models/chooser_student.json", F)
st = student.load("student_model")          # fetches the base model's architecture from the Hub

s = "Dept. of Physics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA"
ranks = {"lex2": cg.lex2(ix, s), "neighbour": [], "top5": [],
         "dense_me5b_chunks": cg.dense_chunks_all([s], cg.names_for_dense(ix))[0][0]}
pool = cg.candidates(ix, ranks)
p = {i: pp for (_, i), pp in student.p_for(st, ix, [("s1", s, i) for i in pool], workers=0).items()}
ids, probs = decide_many(chooser, [(s, p, ranks)])[0]
print([ix.inst[i]["name"] for i in ids])
```

The cards file (`models/institutions.jsonl.gz`) is OpenAlex's institutions with their ROR names and locations, as of
25 September 2026. A newer file in the same format works for new institutions; the card format must not change.
One quirk: `lex2` orders tied acronym matches by Python's set order, which changes with the per-process hash seed, so
a rerun can reorder ties (same candidates). The shipped pools fix the order the benchmark used.

### Retrain the chooser (CPU, about a minute)

```bash
pip install scikit-learn==1.9.1     # needs Python 3.11 or later
python matcher/training/train_chooser.py --fset ror --json preds/chooser_retrained.json --out preds/chooser_retrained.jsonl
```

It trains on the development sets (dev v1 and v2) with the shipped student probabilities and predicts the test sets.
With scikit-learn 1.9.1 it rebuilds `models/chooser_student.json` exactly: the same 400 trees, and the same answer on
all 51,281 strings. `--p jev_p` rebuilds the Jev chooser and `--no-model` the fallback, also exactly. The out file
scores directly:
`python -m matcher.score test_v2 --conf high --pred preds/chooser_retrained.jsonl`.

### Retrain the student (8 GPUs, about 20 minutes)

```bash
curl -LO https://github.com/ourresearch/openalex-affiliation-matcher/releases/download/v3.0.0/train_v1_jev_labels.jsonl.gz
pip install torch==2.6.0 "transformers>=4.51,<5" sentencepiece accelerate scikit-learn
accelerate launch --multi_gpu --num_processes 8 --mixed_precision bf16 matcher/training/student_xenc.py train \
    --train train_v1_jev_labels.jsonl.gz --out student_retrained --base intfloat/multilingual-e5-base
```

The training data is 3.76 million (string, card) pairs from 200,000 random OpenAlex affiliation strings (none in
the test or development sets), each labelled by Jev, the commercial decision model the student learned from. The
question Jev answered is in `matcher/training/jev_teacher.py`. The shipped student trained 2 epochs on 8 H100s in
17 minutes, and agrees with Jev at 0.5 on 97.6% of the held-out pairs.
GPU training is not bit-for-bit repeatable, so a retrained student gives slightly different probabilities; score it
with `student_scores.py --model student_retrained`, `decide.py` and `matcher.score`, and retrain the chooser on its
dev-set probabilities for a fair comparison.

## Files

In the repo:

| Path | What |
|---|---|
| `matcher/` | The matcher: `retrieve.py` (cards, lexical search), `candidates.py`, `student.py`, `decider.py` (the chooser's features), `gbt.py` (the chooser's trees), `batch.py`, and `score.py` for scoring. OpenAlex's nightly runs the same matcher code. |
| `matcher/training/` | Reference: how the student and chooser were trained, and the question Jev answered. |
| `models/` | The choosers as JSON trees, the institution cards, lineage and ROR links. `MANIFEST.json` lists every file with its sha256. |
| `benchmarks/data/` | Our test and development sets with labels, candidate pools and scores ([README](benchmarks/data/README.md)); the external sets with their licenses ([external/](benchmarks/data/external/README.md)). |
| `scripts/` | `decide.py`, `student_scores.py`, `score_external.py`. |

Release assets (v3.0.0), too big for the repo:

| File | Size | sha256 |
|---|---:|---|
| [`student_model.tar.gz`](https://github.com/ourresearch/openalex-affiliation-matcher/releases/download/v3.0.0/student_model.tar.gz): the student's weights and tokenizer | 904 MB | `8180d696be44667da2e8426369489fc23903eff57bdf12717fb4efdb19ec3599` |
| [`train_v1_jev_labels.jsonl.gz`](https://github.com/ourresearch/openalex-affiliation-matcher/releases/download/v3.0.0/train_v1_jev_labels.jsonl.gz): the student's training pairs with Jev's labels | 202 MB | `50e32c7c567a2362c5fc0e8b8255db05280d04d0a80f775c3c9d21f6faf75f73` |

Inside the tarball, `model.pt` has sha256 `54bfbe3f0905cddb7df65a5cc5a54f50744412ba6373010ffc3371513dc2172f`.
Each training row is `{set, k, i, s, c, p, split}`: string id, institution id, the string (first 1,500
characters), the institution's card, Jev's probability, and `train` or `val`.
