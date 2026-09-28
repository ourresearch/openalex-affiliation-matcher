# Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement

[OpenAlex I4210088668](https://openalex.org/institutions/I4210088668) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement itself): 414,280 → 300,808 (−27.4%).
- **Counting its units and predecessors** (the `lineage` filter): 804,243 → 715,239 (−11.1%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (98% of lost works); most of the strings it gained moved up from one of its units (72% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement at all, about **59% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **66% do name it** or one of its units.

**112,173 strings lost Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement** ([removed.csv.gz](removed.csv.gz)), on 192,933 works; **2,963 strings gained it** ([added.csv](added.csv)), on 3,582 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 98% |
| To other institutions (mostly Centre National de la Recherche Scientifique, L'Institut Agro, Université Paris-Sud) | 0% |
| To no institution | 2% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 19% |
| Up from one of its units or predecessors | 72% |
| From other institutions (mostly Centre National de la Recherche Scientifique, Institut National de la Recherche Agronomique, Inserm) | 9% |

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
| INRA | 975 | Institut National de la Recherche Agronomique |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| (INRAE, UMR SELMET, UMR MoSAR) | 26 | no institution |
| ASTREDHOR Sud-Ouest (Site Inrae - 71 avenue Edouard Bourlaux CS 20032 33882 VILLENAVE D'ORNON Cedex - France) | 17 | Animal, Santé, Territoires, Risques et Ecosystèmes |
| Centre IRD de Montpellier | 14 | Services déconcentrés d'appui à la recherche Occitanie-Montpellier, Institut de Recherche pour le Développement |
| UMº 1062 Centre de Biologie pour la Gestion des Populations, INÞe, CIÞD, Institut Agro Montpellier, IºD, Univ. Montpellier. 755 avenue du Ca | 10 | Université de Montpellier, Institut Agro Montpelier, Centre de Biologie pour la Gestion des Populations |
| (IRNAE) | 8 | no institution |
| INRA Laboratoire de la Lactation et de l’Elevage des Ruminants, Theix - 63122 Saint-Genès-Champanelle | 5 | no institution |
| Agrocampus-Ouest, Institut de Recherche en Horticulture et Semences (INRA, Agrocampus-Ouest, Université d'Angers), SFR 149 QUASAV, F-49045 A | 4 | Institut Agro Rennes-Angers, Université d'Angers |
| BIA-INRA UR 1268, Nantes, France | 4 | Biopolymères Interactions Assemblages |
| BIOGECO INRA UMR 1202 University of Bordeaux, Pessac, 33400, France | 4 | Université de Bordeaux, UMR BIOdiversity, GEnes & Communities |
| BioSP INRA 84914 Avignon France | 4 | Biostatistique et processus spatiaux |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
