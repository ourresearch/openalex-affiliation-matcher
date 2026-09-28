# Centre National de la Recherche Scientifique

[OpenAlex I1294671590](https://openalex.org/institutions/I1294671590) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Centre National de la Recherche Scientifique itself): 1,635,636 → 1,762,212 (+7.7%).
- **Counting its units and predecessors** (the `lineage` filter): 3,575,369 → 3,362,118 (−6.0%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (72% of lost works); most of the strings it gained moved up from one of its units (51% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Centre National de la Recherche Scientifique at all, about **96% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **89% do name it** or one of its units.

Net, the works that really are Centre National de la Recherche Scientifique's (counting its units) went up by about 5.2%.

**11,908 strings lost Centre National de la Recherche Scientifique** ([removed.csv.gz](removed.csv.gz)), on 22,933 works; **149,124 strings gained it** ([added.csv.gz](added.csv.gz)), on 226,579 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 72% |
| To other institutions (mostly Inserm, Université de Reims Champagne-Ardenne, Commissariat à l'Énergie Atomique et aux Énergies Alternatives) | 20% |
| To no institution | 8% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 25% |
| Up from one of its units or predecessors | 51% |
| From other institutions (mostly Aix-Marseille Université, Sorbonne Université, Université Pierre-et-Marie-Curie) | 25% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Archives Henri-Poincaré - Philosophie et Recherches sur les Sciences et les Technologies | 640 | Archives Henri-Poincaré - Philosophie et Recherches sur les Sciences et les Technologies |
| ISTO - Institut des Sciences de la Terre d'Orléans - UMR7327 (Campus Géosciences 1A, rue de la Férollerie 45071 Orléans cedex 2 - France) | 575 | Institut des Sciences de la Terre d'Orléans |
| Science des Procédés Céramiques et de Traitements de Surface | 561 | Institut de Recherche sur les Céramiques |
| Laboratoire Interuniversitaire des Systèmes Atmosphériques | 487 | Laboratoire Interuniversitaire des Systèmes Atmosphériques |
| Institut des Sciences de la Terre d'Orléans - UMR7327 | 459 | Institut des Sciences de la Terre d'Orléans |
| Axe 2 : procédés de traitements de surface | 406 | no institution |
| Axe 1 : procédés céramiques | 402 | no institution |
| Génétique Quantitative et Evolution - Le Moulon (Génétique Végétale) | 380 | Génétique Quantitative et Évolution Le Moulon |
| AHP-PReST - Archives Henri-Poincaré - Philosophie et Recherches sur les Sciences et les Technologies (Site de Nancy : 91 avenue de la Libéra | 369 | Archives Henri-Poincaré - Philosophie et Recherches sur les Sciences et les Technologies |
| GQE-Le Moulon - Génétique Quantitative et Evolution - Le Moulon (Génétique Végétale) (UMR de Génétique Quantitative et Evolution - Le Moulon | 368 | Génétique Quantitative et Évolution Le Moulon |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| CNRS | 15,364 | no institution |
| CNRS ( UMR 7528 Mondes iraniens et indiens) , Éditions de l'IFRI Édition | 1,793 | Mondes Iranien et Indien |
| LJAD - Laboratoire Jean Alexandre Dieudonné (Université Côte d'Azur U.M.R. no 7351 du C.N.R.S. Parc Valrose 06108 Nice Cedex 02 France - Fra | 902 | Laboratoire Jean-Alexandre Dieudonné, Université Côte d'Azur |
| CNRS ( UMR 7528 Mondes iraniens et indiens) , Éditions de l'IFRI Référence électronique | 581 | Mondes Iranien et Indien |
| CNRS ( UMR 7528 Mondes iraniens et indiens) , Éditions de l'IFRI | 549 | Mondes Iranien et Indien |
| French National Center for Scientific Research (head office) | 462 | no institution |
| CNRS Éditions | 404 | no institution |
| JAD - Laboratoire Jean Alexandre Dieudonné (Université de Nice - Sophia Antipolis U.M.R. no 6621 du C.N.R.S. Parc Valrose 06108 Nice Cedex 0 | 205 | Laboratoire Jean-Alexandre Dieudonné |
| NeuroPSI - Institut des Neurosciences Paris-Saclay (Centre National de la Recherche Scientifique, Unité Mixte de Recherche-9197 Université P | 180 | Université Paris-Sud, Institut des Neurosciences Paris-Saclay, Université Paris-Saclay |
| Pôle de recherche pour l'organisation et la diffusion de l'information géographique (CNRS UMR 8586 | 179 | Pôle de Recherche pour l'Organisation et la Diffusion de l'Information Géographique |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
