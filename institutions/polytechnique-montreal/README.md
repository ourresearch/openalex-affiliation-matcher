# Polytechnique Montréal

[OpenAlex I45683168](https://openalex.org/institutions/I45683168) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Polytechnique Montréal itself): 40,186 → 40,018 (−0.4%).
- **Counting its units and predecessors** (the `lineage` filter): 42,260 → 41,429 (−2.0%).
- **Why:** most of the strings it lost now go to other institutions (53% of lost works), mostly Université de Montréal, École Polytechnique; most of the strings it gained had no institution before (61% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**323 strings lost Polytechnique Montréal** ([removed.csv](removed.csv)), on 361 works; **94 strings gained it** ([added.csv](added.csv)), on 146 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 9% |
| To other institutions (mostly Université de Montréal, École Polytechnique, National Research Council Canada) | 53% |
| To no institution | 38% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 61% |
| From other institutions (mostly École Polytechnique, Université de Montréal, Université du Québec à Montréal) | 39% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Ecole Polytechnique de Montrea (Canada) | 6 | no institution |
| National Research Council Canada, 2107 Chemin de Polytechnique, Montreal, QC H3T 1J4, Canada | 5 | National Research Council Canada |
| 1 Ecole Polytechnique | 3 | École Polytechnique |
| Department of Mathematics and Industrial Engineering, École Polytechnique - Gerad, Montréal, Canada | 3 | Group for Research in Decision Analysis |
| Ecole Polytechnique de Montre´al, Montre´al, QC, Canada | 3 | no institution |
| Polytechnique Douala | 3 | no institution |
| École Polytechnique and GERAD, Canada | 3 | Group for Research in Decision Analysis |
| 2900, boul. Édouard-Montpetit, Campus de l'Université de Montréal, 2500, chemin de Polytechnique, Montréal (Québec) H3T 1J4, Canada | 2 | Université de Montréal |
| Applied Mathematics , École Polytechnique , 2019 | 2 | École Polytechnique |
| DEPT. ENGG. PHYSICS ECOLE POLYTECHNIQUE, UNIVERSITY OF MONTREAL, Canada | 2 | Université de Montréal |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Département de génie physique [Montréal] | 24 | no institution |
| Department of Mechanical Engineering [Montréal] | 17 | no institution |
| Polytech'Montpellier | 11 | no institution |
| Ecole Polytechnique de Montreal (France) | 3 | École Polytechnique |
| بخش مهندسی عمران، ژئوفیزیک و معدن، دانشگاه پلی تکنیک مونترال، مونترال، کانادا | 2 | no institution |
| . Poly-Grames Research Center Montreal | 1 | no institution |
| 2940 Chemin de Polytechnique, Montreal, QC H3T 1J4 Canada | 1 | no institution |
| Amy Armstrong and Ameneé Shiapush, 100 Resilience Cities; Nathalie Bleau, OURANOS; Louise Bradette, City of Montreal; Fredrik Bynander, Swe | 1 | City of Calgary, City of Toronto, City of Vancouver |
| BWC / AECL/NSERC Chair of Fluid-Structure Interaction , Department of Mechanical Engineering , Ecole Polytechnique , 2900 Boul. Edouard Mont | 1 | Natural Sciences and Engineering Research Council of Canada |
| Biomedical Engineering Institute, Polytechnique Montreal, Montreal, QC, Canada; Biomomentum Inc., 970 Michelin St., Suite 200, Laval, QC H7L | 1 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
