# Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement

[OpenAlex I4210088668](https://openalex.org/institutions/I4210088668) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement itself): 414,257 → 298,551 (−27.9%).
- **Counting its units and predecessors** (the `lineage` filter): 804,191 → 687,540 (−14.5%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (69% of lost works); most of the strings it gained moved up from one of its units (61% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement at all, about **59% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **66% do name it** or one of its units.

Net, the works that really are Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement's (counting its units) went down by about 5.1%.

**113,933 strings lost Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement** ([removed.csv.gz](removed.csv.gz)), on 195,158 works; **1,904 strings gained it** ([added.csv](added.csv)), on 2,050 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 69% |
| To other institutions (mostly Centre National de la Recherche Scientifique, Inserm, AgroParisTech) | 12% |
| To no institution | 19% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 33% |
| Up from one of its units or predecessors | 61% |
| From other institutions (mostly Institut National de la Recherche Agronomique, Institut de l’Elevage, Centre National de la Propriété Forestière) | 7% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| (INRA - Institut National de la Recherche Agronomique) | 11,385 | Institut National de la Recherche Agronomique |
| French National Institute for Agricultural Research (INRA) | 9,669 | Institut National de la Recherche Agronomique |
| Institut National de la Recherche Agronomique | 5,621 | Institut National de la Recherche Agronomique |
| AMAP, IRD, Université de Montpellier, CIRAD, CNRS, INRAE, Boulevard de la Lironde, TA A- 51 / PS 2, F- 34398 Montpellier cedex 5 (France) | 2,240 | Université de Montpellier, Centre de Coopération Internationale en Recherche Agronomique pour le Développement, Centre National de la Recherche Scientifique, UMR Botanique et Modélisation de l’Architecture des Plantes et des végétations, Institut de Recherche pour le Développement |
| Génétique Animale et Biologie Intégrative | 2,214 | Génétique Animale et Biologie Intégrative |
| INRA - Institut National de la Recherche Agronomique (France) | 1,887 | Institut National de la Recherche Agronomique |
| GABI - Génétique Animale et Biologie Intégrative (Domaine de Vilvert F-78252 Jouy-en-Josas - France) | 1,539 | Génétique Animale et Biologie Intégrative |
| UMR G-EAU - Gestion de l'Eau, Acteurs, Usages (361 rue J.F. Breton - BP 5095 34196 Montpellier Cedex 5 - France) | 1,534 | Gestion de l'Eau, Acteurs, Usages |
| Ecologie fonctionnelle et écotoxicologie des agroécosystèmes | 1,056 | Écologie Fonctionnelle et Écotoxicologie des Agroécosystèmes |
| INRA | 975 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| (INRAE, UMR SELMET, UMR MoSAR) | 26 | no institution |
| ASTREDHOR Sud-Ouest (Site Inrae - 71 avenue Edouard Bourlaux CS 20032 33882 VILLENAVE D'ORNON Cedex - France) | 17 | Animal, Santé, Territoires, Risques et Ecosystèmes |
| UMº 1062 Centre de Biologie pour la Gestion des Populations, INÞe, CIÞD, Institut Agro Montpellier, IºD, Univ. Montpellier. 755 avenue du Ca | 10 | Université de Montpellier, Institut Agro Montpelier, Centre de Biologie pour la Gestion des Populations |
| (IRNAE) | 8 | no institution |
| INRA Laboratoire de la Lactation et de l’Elevage des Ruminants, Theix - 63122 Saint-Genès-Champanelle | 5 | no institution |
| INRA Neuro-Gastroenterology & Nutrition Unit, Toulouse, France | 4 | NutriNeuro |
| Laboratoire Sous-Nutrition des Ruminants, INRA Theix, Saint Genès Champanelle, France | 4 | Centre de Recherche en Nutrition Humaine d'Auvergne |
| Laboratoire de Biologie Cellulaire, INRA-Centre de Versailles, F-78026, Versailles Cedex, France | 4 | Laboratoire de Génétique Cellulaire |
| Unit of Animal Health Management, Veterinary School-INRA, BP 40706, 44307 Nantes Cedex 03, France | 4 | Département Santé Animale |
| INRA Laboratoire de la Lactation et de l'Elevage des Ruminants, Theix - 63122 Saint-Genès-Champanelle | 3 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
