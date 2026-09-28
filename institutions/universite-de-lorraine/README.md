# Université de Lorraine

[OpenAlex I90183372](https://openalex.org/institutions/I90183372) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Université de Lorraine itself): 177,759 → 150,620 (−15.3%).
- **Counting its units and predecessors** (the `lineage` filter): 235,961 → 243,136 (+3.0%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (85% of lost works); the largest share of the strings it gained had no institution before (41% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université de Lorraine at all, about **30% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **97% do name it** or one of its units.

Net, the works that really are Université de Lorraine's (counting its units) went up by about 3.8%.

**22,174 strings lost Université de Lorraine** ([removed.csv.gz](removed.csv.gz)), on 40,788 works; **5,095 strings gained it** ([added.csv.gz](added.csv.gz)), on 6,324 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 85% |
| To other institutions (mostly Centre National de la Recherche Scientifique, École Nationale Supérieure des Mines de Nancy, Centre Hospitalier Régional et Universitaire de Nancy) | 9% |
| To no institution | 5% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 41% |
| Up from one of its units or predecessors | 38% |
| From other institutions (mostly Centre de Médecine Préventive, Centre National de la Recherche Scientifique, Institut de Chimie Physique) | 21% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Université Henri Poincaré - Nancy 1 | 2,258 | Université Henri Poincaré |
| Université Henri Poincaré Nancy 1, | 994 | Université Henri Poincaré |
| Centre de Recherche Universitaire Lorrain d'Histoire | 792 | Centre de Recherche Universitaire Lorrain d’Histoire |
| Université Nancy 2 | 685 | Université Nancy-II |
| Archives Henri-Poincaré - Philosophie et Recherches sur les Sciences et les Technologies | 640 | Archives Henri-Poincaré - Philosophie et Recherches sur les Sciences et les Technologies |
| UNIVERSITE HENRI POINCARE - NANCY 1 | 554 | Université Henri Poincaré |
| Vandoeuvre-les-Nancy, INPL | 552 | no institution |
| Centre lorrain de recherches interdisciplinaires dans les domaines des littératures, des cultures et de la théologie | 432 | Centre lorrain de recherches interdisciplinaires dans les domaines des littératures, des cultures et de la théologie |
| Université Paul Verlaine − Metz | 431 | Université Paul Verlaine - Metz |
| CRAN - Centre de Recherche en Automatique de Nancy (Université Henri Poincaré, 2 avenue de la forêt de Haye, 54516 Vandoeuvre les Nancy - Fr | 422 | CRAN, Université Henri Poincaré |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Laboratoire Sciences de l'Antiquité et du Moyen Âge (SAMA) de Lorraine, 91 avenue de la Libération, boîte postale 454, F-54001 Nancy Cedex ( | 110 | Sciences de l'Antiquité et du Moyen-Age |
| Nancy Université | 96 | no institution |
| (BETA, Université de Loraine) | 35 | Bureau d'Economie Théorique et Appliquée |
| Faculté des Sciences de Nancy | 32 | no institution |
| IUT Nancy Charlemagne (2 ter boulevard Charlemagne, 54000 Nancy - France) | 32 | no institution |
| (Université de Lorraine, LEM3, ENSEM) | 25 | Laboratoire d'Étude des Microstructures et de Mécanique des Matériaux |
| Faculté de Pharmacie [Nancy] (5 rue Albert Lebrun, 54000 NANCY - France) | 25 | no institution |
| Faculté d'odontologie [Nancy] (Campus Brabois Santé, Faculté d'odontologie de Lorraine, 7 avenue de la forêt de Haye, BP 20199, 54505 Vandoe | 22 | no institution |
| Éditeur Presses universitaires de Lorraine Référence électronique | 22 | no institution |
| Chercheur auprès de l’association culturelle Joseph Jacquemotte et doctorant en économie à l’université de Nancy (France) | 13 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
