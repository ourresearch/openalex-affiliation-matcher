# Université de Limoges

[OpenAlex I65806277](https://openalex.org/institutions/I65806277) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Université de Limoges itself): 36,398 → 30,639 (−15.8%).
- **Counting its units and predecessors** (the `lineage` filter): 47,590 → 44,669 (−6.1%).
- **Why:** the largest share of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (38% of lost works); most of the strings it gained had no institution before (56% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université de Limoges at all, about **79% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **88% do name it** or one of its units.

**3,423 strings lost Université de Limoges** ([removed.csv](removed.csv)), on 11,396 works; **2,710 strings gained it** ([added.csv](added.csv)), on 3,854 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 38% |
| To other institutions (mostly Centre Hospitalier Universitaire de Limoges, Inserm, Centre National de la Recherche Scientifique) | 29% |
| To no institution | 33% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 56% |
| Up from one of its units or predecessors | 20% |
| From other institutions (mostly Centre National de la Recherche Scientifique, Laboratoire de Chimie, Hôpital Dupuytren) | 24% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Limoges | 1,532 | no institution |
| Laboratoire de Géographie Physique et Environnementale | 1,262 | Laboratoire de Géographie Physique et Environnementale |
| GEOLAB - Laboratoire de Géographie Physique et Environnementale (4, rue Ledru 63057 CLERMONT FERRAND CEDEX 1 - France) | 678 | Laboratoire de Géographie Physique et Environnementale |
| Science des Procédés Céramiques et de Traitements de Surface | 561 | Institut de Recherche sur les Céramiques |
| Axe 2 : procédés de traitements de surface | 406 | no institution |
| Axe 1 : procédés céramiques | 402 | no institution |
| SPCTS - Science des Procédés Céramiques et de Traitements de Surface (SPCTS, Centre Européen de la Céramique, 12 Rue Atlantis, 87068 LIMOGES | 217 | Centre Européen de la Céramique, Institut de Recherche sur les Céramiques |
| Axe 2 : procédés de traitements de surface (France) | 152 | no institution |
| GEOLAB-CE - Capital Environnemental (France) | 135 | Laboratoire de Géographie Physique et Environnementale |
| Maître de conférences | 133 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Laboratoire de Biostatistique et d'Informatique Médicale (Faculté de médecine 2 Rue du Docteur Raymond Marcland 87025 LIMOGES Cedex - France | 448 | no institution |
| GEMH - Groupe d'Etudes des Matériaux Hétérogènes (Centre Universitaire de Génie Civil Département Génie Civil, Faculté des Sciences et Tech | 73 | no institution |
| Centre de Mémoire de Ressources et de Recherches [Limoges] | 57 | no institution |
| Laboratoire d'Hématologie Expérimentale, Faculté de Médecine, Limoges, France | 31 | no institution |
| Centre d'Etudes et de Recherches Historiques de Limoges | 18 | Centre de Recherches Historiques |
| IRCOM, Limoges, France | 18 | no institution |
| Hospital and University Federation of Adult and Geriatric Psychiatry, Limoges, France | 14 | no institution |
| CeReS, université de Limoges, F-87036jacques-philippe.saint-gerand@unilim.fr | 11 | Centre de Recherches Sémiotiques |
| Choukri Ben Ayed est sociologue, professeur à l'université de Limoges, chercheur au GRESCO (Groupe de recherches et d'études sociologiques d | 10 | Groupe de Recherches Sociologiques sur les sociétés Contemporaines |
| Choukri Ben Ayed est sociologue, professeur à l’université de Limoges, chercheur au GRESCO (Groupe de recherches et d’études sociologiques d | 10 | Groupe de Recherches Sociologiques sur les sociétés Contemporaines |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
