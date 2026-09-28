# Centre de Coopération Internationale en Recherche Agronomique pour le Développement

[OpenAlex I131077856](https://openalex.org/institutions/I131077856) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Centre de Coopération Internationale en Recherche Agronomique pour le Développement itself): 57,327 → 55,009 (−4.0%).
- **Counting its units and predecessors** (the `lineage` filter): 107,719 → 100,546 (−6.7%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (65% of lost works); most of the strings it gained moved up from one of its units (64% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Centre de Coopération Internationale en Recherche Agronomique pour le Développement at all, about **63% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **96% do name it** or one of its units.

**2,535 strings lost Centre de Coopération Internationale en Recherche Agronomique pour le Développement** ([removed.csv](removed.csv)), on 6,307 works; **1,329 strings gained it** ([added.csv](added.csv)), on 1,935 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 65% |
| To other institutions (mostly Université de Montpellier, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement, Institut de Recherche pour le Développement) | 13% |
| To no institution | 22% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 19% |
| Up from one of its units or predecessors | 64% |
| From other institutions (mostly Centre international de recherche-développement sur l'elevage en zone subhumide, Kasetsart University, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement) | 17% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| UMR G-EAU - Gestion de l'Eau, Acteurs, Usages (361 rue J.F. Breton - BP 5095 34196 Montpellier Cedex 5 - France) | 1,534 | Gestion de l'Eau, Acteurs, Usages |
| Cirad-BIOS - Département Systèmes Biologiques (Avenue Agropolis TA A-DIR / 04 34398 Montpellier Cedex 5 France - France) | 999 | no institution |
| Cirad-Dgdrs - Direction Générale Déléguée à la Recherche et à la Stratégie (42 rue Scheffer - 75116 Paris - France) | 161 | CIRAD - Direction générale déléguée à la recherche et à la stratégie |
| UMR DAP - Développement et amélioration des plantes (Agro M 2 place Viala 34060 Montpellier Cedex 1 pour le Cirad TA A-108 / 03 - Avenue Agr | 88 | no institution |
| Montpellier SupAgro, UMR CBGP INRAE / IRD / CIRAD / SupAgro, 755 Avenue du Campus Agropolis | 62 | Institut Agro Montpellier, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement |
| Forêts et Sociétés | 43 | Forests and Societies |
| (UMR DIADE - IRD, University of Montpellier, Cirad - France) | 28 | Université de Montpellier, Diversité, adaptation et développement des plantes, Institut de Recherche pour le Développement |
| DAAV - Diversité, Adaptation et Amélioration de la Vigne [AGAP] (Cirad Avenue Agropolis 34398 Montpellier Cedex 5, France - France) | 23 | Amélioration Génétique et Adaptation des Plantes méditerranéennes et tropicales |
| Univ Montpellier, Cirad, IRD, Intertryp, Montpellier, France | 21 | Université de Montpellier, Institut de Recherche pour le Développement |
| Cirad-Dgdrs-Dims - Cirad-Dgdrs-Direction de l'impact et du Marketing de la Science (Avenue Agropolis - 34398 Montpellier Cedex 5 France - Fr | 20 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| CIRAD, UMR ASTRE | 26 | Animal, Santé, Territoires, Risques et Ecosystèmes |
| CIRAD-BIOS-UMR AGAP (FRA) | 22 | Amélioration Génétique et Adaptation des Plantes méditerranéennes et tropicales |
| CIRAD-DGDRS-DIST (FRA) | 19 | CIRAD - Direction générale déléguée à la recherche et à la stratégie |
| CIRAD-ES-UPR Forêts et sociétés (FRA) | 19 | Forests and Societies |
| CIRAD Département Performances des systèmes de production et de transformation tropicaux | 18 | no institution |
| CIRAD-PERSYST-UPR HortSys (FRA) | 18 | Fonctionnement agroécologique et performances des systèmes de culture horticoles |
| CIRAD-BIOS-UMR PVBMT, La Réunion | 15 | Peuplements végétaux et bioagresseurs en milieu tropical |
| CIRAD-ES-UMR ART-DEV (SEN) | 15 | Acteurs, Ressources et Territoires dans le Développement |
| CIRAD-ES-UMR TETIS (FRA) | 15 | Territoires, Environnement, Télédétection et Information Spatiale |
| CIRAD-DGDRS-Dims (FRA) | 14 | CIRAD - Direction générale déléguée à la recherche et à la stratégie |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
