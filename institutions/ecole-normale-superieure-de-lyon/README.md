# École Normale Supérieure de Lyon

[OpenAlex I113428412](https://openalex.org/institutions/I113428412) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to École Normale Supérieure de Lyon itself): 57,694 → 44,662 (−22.6%).
- **Counting its units and predecessors** (the `lineage` filter): 165,029 → 145,568 (−11.8%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (97% of lost works); most of the strings it gained moved up from one of its units (67% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for École Normale Supérieure de Lyon at all, about **95% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **75% do name it** or one of its units.

Net, the works that really are École Normale Supérieure de Lyon's (counting its units) went up by about 5.8%.

**1,667 strings lost École Normale Supérieure de Lyon** ([removed.csv](removed.csv)), on 16,993 works; **2,548 strings gained it** ([added.csv](added.csv)), on 3,571 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 97% |
| To its parent institution | 0% |
| To other institutions (mostly Lyon 1 Université, Centre National de la Recherche Scientifique, Inserm) | 2% |
| To no institution | 1% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 15% |
| Up from one of its units or predecessors | 67% |
| Down from its parent institution | 0% |
| From other institutions (mostly Centre National de la Recherche Scientifique, Lyon 1 Université, École Normale Supérieure - PSL) | 18% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Univ. Lyon, ENS de Lyon, CNRS, Centre de Recherche Astrophysique de Lyon | 10,861 | Centre National de la Recherche Scientifique, Centre de Recherche Astrophysique de Lyon |
| IHRIM - Institut d’Histoire des Représentations et des Idées dans les Modernités (ENS de Lyon  15 parvis René Descartes  BP 7000 69342 Lyo | 2,019 | Institut d'Histoire des Représentations et des Idées dans les Modernités |
| LIP - Laboratoire de l'Informatique du Parallélisme (46 Allée d'Italie 69364 LYON CEDEX 07 - France) | 951 | Laboratoire de l'Informatique du Parallélisme |
| Phys-ENS - Laboratoire de Physique de l'ENS Lyon (46 allée d'Italie 69007 Lyon - France) | 739 | Laboratoire de Physique de l'ENS de Lyon |
| Univ Lyon, Univ Lyon1, Ens de Lyon, CNRS, Centre de Recherche Astrophysique de Lyon UMR5574, F-69230 Saint-Genis-Laval, France | 90 | Centre National de la Recherche Scientifique, Centre de Recherche Astrophysique de Lyon |
| Univ Lyon, Univ Lyon1, Ens de Lyon, CNRS, Centre de Recherche Astrophysique de Lyon UMR5574, F-69230, Saint-Genis-Laval, France | 66 | Centre National de la Recherche Scientifique, Centre de Recherche Astrophysique de Lyon |
| École de management de Lyon | 29 | École de management de Lyon |
| CNRS, Laboratoire LIP, Lyon, France | 27 | Centre National de la Recherche Scientifique, Laboratoire de l'Informatique du Parallélisme |
| Linguiste | 21 | no institution |
| Univ Lyon, ENS de Lyon, Univ Claude Bernard, CNRS, Laboratoire de Physique, Lyon, France | 18 | Centre National de la Recherche Scientifique, Laboratoire de Physique de l'ENS de Lyon |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| UMPA-ENSL - Unité de Mathématiques Pures et Appliquées (France) | 431 | Unité de Mathématiques Pures et Appliquées |
| UMPA-ENSL | 175 | Unité de Mathématiques Pures et Appliquées |
| NUMED - Numerical Medicine (Unité de Mathématiques Pures et Appliquées  Ecole Normale Supérieure  46 Allée d'Italie  69007 Lyon - France) | 47 | Unité de Mathématiques Pures et Appliquées |
| Université Claude Bernard Lyon 1, ENSL, CNRS, LGL-TPE, 43 boulevard du 11 Novembre, F- 69622 Villeurbanne (France) | 16 | Lyon 1 Université, Centre National de la Recherche Scientifique |
| CEP EA 4160 - Centre d'études poétiques (ENS LSH 15 parvis René Descartes 69007 LYON - France) | 12 | École normale supérieure de Fontenay-Saint-Cloud |
| ENSL, Laboratoire de Physique (lyon - France) | 12 | Laboratoire de Physique de l'ENS de Lyon |
| ENSL | 10 | no institution |
| (Laboratoire Environnement Ville Société ; Université de Lyon, CNRS, ENS ; France) | 9 | Lyon 1 Université, Centre National de la Recherche Scientifique, Environnement, ville, société |
| Ludovic Frobert est directeur de recherches au CNRS et travaille dans le laboratoire TRIANGLE (ENS-Lyon). Il a publié en 2014 Le Solitaire d | 7 | Maison des Sciences sociales et des Humanités - Lyon St-Étienne, Centre National de la Recherche Scientifique, Triangle : Action, Discours, Pensée politique et économique |
| Centre de Recherche Astrophysique de Lyon, CNRS/ENSL Université Lyon 1, 9 av. Ch. André, 69561 Saint-Genis-Laval, France | 6 | Centre de Recherche Astrophysique de Lyon, Lyon 1 Université, Centre National de la Recherche Scientifique |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
