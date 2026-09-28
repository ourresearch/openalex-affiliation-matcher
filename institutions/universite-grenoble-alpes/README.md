# Université Grenoble Alpes

[OpenAlex I899635006](https://openalex.org/institutions/I899635006) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Université Grenoble Alpes itself): 189,182 → 127,777 (−32.5%).
- **Counting its units and predecessors** (the `lineage` filter): 372,964 → 337,562 (−9.5%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (72% of lost works); the largest share of the strings it gained had no institution before (47% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université Grenoble Alpes at all, about **66% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **52% do name it** or one of its units.

Net, the works that really are Université Grenoble Alpes's (counting its units) went down by about 2.3%.

**55,738 strings lost Université Grenoble Alpes** ([removed.csv.gz](removed.csv.gz)), on 95,696 works; **1,921 strings gained it** ([added.csv](added.csv)), on 4,006 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 72% |
| To other institutions (mostly Centre Hospitalier Universitaire de Grenoble, Commissariat à l'Énergie Atomique et aux Énergies Alternatives, Laboratoire d'Électronique des Technologies de l'Information) | 25% |
| To no institution | 2% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 47% |
| Up from one of its units or predecessors | 36% |
| From other institutions (mostly Centre National de la Recherche Scientifique, IPAG Business School, Universidade Federal do Rio Grande do Sul) | 17% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Centre Hospitalier Universitaire de Grenoble | 712 | Centre Hospitalier Universitaire de Grenoble |
| Université Joseph Fourier, Grenoble, France | 685 | Université Joseph Fourier |
| LPNC - Laboratoire de Psychologie et NeuroCognition (LPNC - Laboratoire de Psychologie et NeuroCognition CNRS UMR 5105 - UGA BSHM - 1251 A | 494 | Centre National de la Recherche Scientifique, Laboratoire de Psychologie et NeuroCognition |
| Université Joseph Fourier | 426 | Université Joseph Fourier |
| (Univ. Grenoble Alpes, CNRS, Grenoble INP, LEGI, Grenoble, 38000, France) | 367 | Institut polytechnique de Grenoble, Centre National de la Recherche Scientifique, Laboratoire des Écoulements Géophysiques et Industriels |
| Univ. Grenoble Alpes , CNRS , IPAG , 38000 Grenoble , France | 345 | Centre National de la Recherche Scientifique, Institut de Planétologie et d'Astrophysique de Grenoble |
| LPNC - Laboratoire de Psychologie et NeuroCognition (LPNC - Laboratoire de Psychologie et NeuroCognition CNRS UMR 5105 - UGA Bâtiment Mich | 287 | Centre National de la Recherche Scientifique, Laboratoire de Psychologie et NeuroCognition |
| Joseph-Fourier University | 256 | Université Joseph Fourier |
| Université de Grenoble | 224 | Pôle de recherche et d'enseignement supérieur Université de Grenoble |
| Université Joseph-Fourier | 223 | Université Joseph Fourier |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Laboratoire des Sciences de l'Éducation (Grenoble) | 273 | no institution |
| LSE - Laboratoire des Sciences de l'Éducation (Grenoble) (UFR SHS - BSHM - 1251 avenue Centrale - Domaine Universitaire - 38400 Saint-Martin | 204 | no institution |
| UGA | 197 | no institution |
| IPAG / UGA - CNRS | 179 | IPAG Business School, Centre National de la Recherche Scientifique |
| Institut de géologie Dolomieu | 93 | no institution |
| PLC - Philosophie, Langages et Cognition (Département de Philosophie, ARSH 2, Domaine Universitaire, 38040 Grenoble Cedex 9 - France) | 83 | no institution |
| UFRGS/UGA | 66 | Universidade Federal do Rio Grande do Sul |
| Grenoble IAE Graduate School of Management | 63 | Grenoble Ecole de Management |
| Néel / UGA - CNRS | 53 | Institut Néel |
| UGA, GRENOBLE ,ST MARTIN D'HERES | 40 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
