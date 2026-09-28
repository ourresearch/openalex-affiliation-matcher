# Nantes Université

[OpenAlex I97188460](https://openalex.org/institutions/I97188460) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Nantes Université itself): 116,319 → 96,051 (−17.4%).
- **Counting its units and predecessors** (the `lineage` filter): 178,782 → 163,898 (−8.3%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (84% of lost works); the largest share of the strings it gained moved up from one of its units (44% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Nantes Université at all, about **81% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **83% do name it** or one of its units.

**5,375 strings lost Nantes Université** ([removed.csv](removed.csv)), on 32,658 works; **6,405 strings gained it** ([added.csv.gz](added.csv.gz)), on 7,613 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 84% |
| To other institutions (mostly Centre Hospitalier Universitaire de Nantes, Inserm, Centre National de la Recherche Scientifique) | 15% |
| To no institution | 2% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 34% |
| Up from one of its units or predecessors | 44% |
| From other institutions (mostly Centre Hospitalier Universitaire de Nantes, Inserm, Centre National de la Recherche Scientifique) | 22% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Espaces et Sociétés | 2,474 | Espaces et Sociétés |
| CREN - Centre de recherche en éducation de Nantes (Chemin de la Censive du Tertre BP 81227 44312 Nantes cedex 3 - France) | 2,370 | Centre de Recherche en Éducation de Nantes |
| Droit et changement social | 2,251 | Droit et changement social |
| ESO - Espaces et Sociétés (France) | 1,794 | Espaces et Sociétés |
| CReAAH - Centre de Recherche en Archéologie, Archéosciences, Histoire (Université de Rennes 1 Bâtiment 24-25 Campus de Beaulieu 263, Avenue  | 1,405 | Université de Rennes, Centre de Recherche en Archéologie, Archéosciences, Histoire, Université Rennes 1 |
| Faculté des Sciences et des Techniques de Nantes, Centre François Viète d’Histoire des Sciences et de Techniques EA 1161, Nantes, France | 1,297 | Centre François Viète |
| Laboratoire des Sciences du Numérique de Nantes | 1,270 | Laboratoire des Sciences du Numérique de Nantes |
| Faculté des Sciences et des Techniques de Nantes, Centre François Viète d'Histoire des Sciences et de Techniques EA 1161, Nantes, France | 1,221 | Centre François Viète |
| Centre François Viéte d'Histoire des Sciences et des Techniques EA 1161, Faculté des Sciences et des, Techniques de Nantes, Nantes, France | 1,117 | Centre François Viète |
| Laboratoire de Planétologie et Géodynamique [UMR 6112] | 1,083 | Laboratoire de Planétologie et Géosciences |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| TRUST - Contrôle de santé fiabilité et calcul des structures (UFR des Sciences et Techniques 2 chemin de la Houssinière BP 92208 44322 Nante | 35 | no institution |
| Nuclear Medicine Department, University Hospital, Nantes, France | 33 | no institution |
| CRGNA - Centre de Recherche en Gestion Nantes Atlantique (Rue de la Censive du Tertre B.P. 62232 44322 Nantes Cedex 3  - France) | 31 | no institution |
| CRGNA - Centre de Recherche en Gestion Nantes Atlantique (Rue de la Censive du Tertre B.P. 62232 44322 Nantes Cedex 3 - France) | 26 | no institution |
| Department of Dermatology Nantes University Hospital Nantes France | 20 | Centre Hospitalier Universitaire de Nantes |
| IUML - FR 3473 Institut universitaire Mer et Littoral (2, rue de la Houssinière - BP 92208 - 44322 Nantes Cedex 3 - France) | 17 | no institution |
| Department of Pathology, University Hospital, Nantes, France | 13 | Centre Hospitalier Universitaire de Nantes |
| Ecole Polytechnique de l'Univ. de Nantes (France) | 13 | École Polytechnique |
| IAE Nantes | 13 | no institution |
| Laboratory of Hematology, University Hospital, Nantes, France | 13 | Centre Hospitalier Universitaire de Nantes |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
