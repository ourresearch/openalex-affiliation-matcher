# Université de Toulouse

[OpenAlex I4405258862](https://openalex.org/institutions/I4405258862) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Université de Toulouse itself): 108,824 → 114,409 (+5.1%).
- **Counting its units and predecessors** (the `lineage` filter): 276,266 → 260,672 (−5.6%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (98% of lost works); most of the strings it gained moved up from one of its units (55% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université de Toulouse at all, about **91% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **54% do name it** or one of its units.

**13,919 strings lost Université de Toulouse** ([removed.csv.gz](removed.csv.gz)), on 25,234 works; **26,564 strings gained it** ([added.csv.gz](added.csv.gz)), on 37,105 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 98% |
| To other institutions (mostly Université Toulouse - Jean Jaurès, Centre National de la Recherche Scientifique, Toulouse School of Economics) | 2% |
| To no institution | 0% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 7% |
| Up from one of its units or predecessors | 55% |
| From other institutions (mostly Université Fédérale de Toulouse Midi-Pyrénées, Toulouse School of Economics, Centre National de la Recherche Scientifique) | 38% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| UT3 - Université Toulouse III - Paul Sabatier (118 route de Narbonne - 31062 Toulouse - France) | 2,670 | Université Toulouse III - Paul Sabatier |
| Paul Sabatier University | 869 | Université Toulouse III - Paul Sabatier |
| Université Paul Sabatier, Toulouse, France | 506 | Université Toulouse III - Paul Sabatier |
| Université Paul Sabatier | 441 | Université Toulouse III - Paul Sabatier |
| Université Paul Sabatier | 419 | Université Toulouse III - Paul Sabatier |
| Paul Sabatier University, Toulouse, France | 185 | Université Toulouse III - Paul Sabatier |
| Université Toulouse III Paul Sabatier, Toulouse, France | 130 | Université Toulouse III - Paul Sabatier |
| Université Toulouse III - Paul Sabatier, Toulouse, France | 126 | Université Toulouse III - Paul Sabatier |
| Université Toulouse III Paul-Sabatier, Toulouse, France | 120 | Université Toulouse III - Paul Sabatier |
| Université de Toulouse II-Le Mirail | 117 | Université Toulouse - Jean Jaurès |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| University of Toulouse 1 - Toulouse School of Economics (TSE) | 535 | Toulouse School of Economics |
| University of Toulouse 1 - Toulouse School of Economics (TSE), Place Anatole-France, Toulouse Cedex, F-31042, France | 439 | Toulouse School of Economics |
| Université Toulouse | 141 | Université Fédérale de Toulouse Midi-Pyrénées |
| Toulouse Graduate School | 137 | no institution |
| IRIT, University of Toulouse, Toulouse, France | 128 | Institut de Recherche en Informatique de Toulouse, Université Toulouse III - Paul Sabatier, Université Toulouse-I-Capitole, Institut Polytechnique de Bordeaux, Université Toulouse - Jean Jaurès |
| Univ. of Toulouse | 126 | Université Fédérale de Toulouse Midi-Pyrénées |
| University of Toulouse 1 - Industrial Economic Institute (IDEI) | 116 | Institut d'Économie Industrielle |
| Toulouse School of Economics, University of Toulouse Capitole, Toulouse, France | 95 | Toulouse School of Economics |
| University of Toulouse Capitole - Toulouse School of Economics | 92 | Toulouse School of Economics |
| University of Toulouse Capitole - Toulouse School of Economics, Toulouse, France | 90 | Toulouse School of Economics |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
