# Université Paris Cité

[OpenAlex I204730241](https://openalex.org/institutions/I204730241) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Université Paris Cité itself): 392,251 → 124,319 (−68.3%).
- **Counting its units and predecessors** (the `lineage` filter): 569,945 → 504,476 (−11.5%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (80% of lost works); most of the strings it gained moved up from one of its units (54% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université Paris Cité at all, about **66% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **50% do name it** or one of its units.

**250,411 strings lost Université Paris Cité** ([removed.csv.gz](removed.csv.gz)), on 398,444 works; **8,681 strings gained it** ([added.csv.gz](added.csv.gz)), on 10,479 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 80% |
| To other institutions (mostly Centre National de la Recherche Scientifique, Université Paris-Sud, Université Pierre-et-Marie-Curie) | 18% |
| To no institution | 2% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 20% |
| Up from one of its units or predecessors | 54% |
| From other institutions (mostly Assistance Publique – Hôpitaux de Paris, Centre National de la Recherche Scientifique, Sorbonne Université) | 25% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| University of Paris VII, Paris, France | 12,530 | Université Paris Diderot |
| Sorbonne Paris Cité | 4,191 | Sorbonne Paris Cité |
| Université Denis Diderot Paris 7, Paris, France | 2,820 | Université Paris Diderot |
| ITODYS, Université Denis Diderot Paris 7, Paris, France | 2,802 | Interfaces Traitements Organisation et Dynamique des Systèmes, Université Paris Diderot |
| Université Paris-Sorbonne | 1,541 | Paris-Sorbonne University |
| APC (UMR_7164) - AstroParticule et Cosmologie (APC - UMR 7164, Université Paris Diderot, 10 rue Alice Domon et Léonie Duquet, case postale 7 | 1,450 | Université Paris Diderot |
| LESIA, Observatoire Paris-Site de Meudon, Meudon, France | 1,349 | Observatoire de Paris, Laboratoire d’études spatiales et d’instrumentation en astrophysique |
| University of Paris I (Panthéon-Sorbonne) | 1,275 | Université Paris 1 Panthéon-Sorbonne |
| Université Paris Descartes, Paris, France | 1,170 | Université Paris Descartes |
| UPD5 - Université Paris Descartes - Paris 5 (12, rue de l'École de Médecine - 75270 Paris cedex 06 - France) | 1,108 | Université Paris Descartes |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Paris University, Paris, France | 139 | no institution |
| Laboratoire Interuniversitaire des Systèmes Atmosphériques (LISA), UMR 7583 CNRS, Universités Paris-Est Créteil et Université de Paris,  | 104 | Laboratoire Interuniversitaire des Systèmes Atmosphériques, Laboratoire Techniques, Territoires et Sociétés, Centre National de la Recherche Scientifique, Institut Pierre-Simon Laplace |
| Universidade de Paris | 67 | no institution |
| UNIVERSIDAD DE PARÍS | 62 | no institution |
| Universidad de París | 55 | no institution |
| VAC (URP_7326) - Vision Action Cognition (Institut de Psychologie - Université de Paris, 71 avenue Édouard Vaillant, 92774 Boulogne-Billanco | 34 | Laboratoire Vision Action Cognition |
| Universit&#x00E9; Paris Cit&#x00E9;,Centre Borelli UMR 9010,Paris,France | 21 | Centre Borelli |
| (CRT, Institut Pasteur; MERIT, Institut de Recherche pour le Développement et Université de Paris, Paris, France.) | 20 | Institut Pasteur, Santé Internationale de la mère et de l'enfant |
| Universit&#x00E9; Paris Cit&#x00E9;,France | 20 | no institution |
| University of Paris - Centre for Research in Epidemiology and Statistics (CRESS) | 19 | Centre de Recherche Épidémiologie et Statistique |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
