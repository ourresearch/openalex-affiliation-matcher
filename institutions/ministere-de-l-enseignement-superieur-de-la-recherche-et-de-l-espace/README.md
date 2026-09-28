# Ministère de l'Enseignement Supérieur, de la Recherche et de l'Espace

[OpenAlex I4210131494](https://openalex.org/institutions/I4210131494) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Ministère de l'Enseignement Supérieur, de la Recherche et de l'Espace itself): 2,289 → 1,943 (−15.1%).
- **Counting its units and predecessors** (the `lineage` filter): 331,380 → 339,136 (+2.3%).
- **Why:** most of the strings it lost now go to other institutions (74% of lost works), mostly Ministere de l'Education Nationale, Ministry of Higher Education; most of the strings it gained were assigned to other institutions before (64% of gained works), mostly Institut Universitaire de France, Ministere de l'Education Nationale.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Ministère de l'Enseignement Supérieur, de la Recherche et de l'Espace at all, about **73% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **61% do name it** or one of its units.

Net, the works that really are Ministère de l'Enseignement Supérieur, de la Recherche et de l'Espace's (counting its units) went up by about 5.6%.

**284 strings lost Ministère de l'Enseignement Supérieur, de la Recherche et de l'Espace** ([removed.csv](removed.csv)), on 843 works; **53 strings gained it** ([added.csv](added.csv)), on 66 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Ministere de l'Education Nationale, Ministry of Higher Education, Centre National de la Recherche Scientifique) | 74% |
| To no institution | 26% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 33% |
| Up from one of its units or predecessors | 3% |
| From other institutions (mostly Institut Universitaire de France, Ministere de l'Education Nationale, Ministre de la Santé) | 64% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Ministère de l'Éducation nationale/Ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation - Direction générale des ressou | 143 | Ministere de l'Education Nationale |
| Ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation - Service de la coordination des stratégies de l'enseignement supé | 137 | Ministry of Higher Education |
| Ministère de l'Enseignement Supérieur et de la Recherche | 61 | Ministère de l'Enseignement Supérieur et de la Recherche, Ministère de l'Enseignement Superieur et de la Recherche |
| Ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation - Direction générale de la recherche et de l'innovation | 57 | no institution |
| Ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation - Direction générale de l'enseignement supérieur et de l'insertion | 34 | no institution |
| Ministère de l'Enseignement Supérieur et de la Recherche Scientifique | 24 | Ministère de l’Enseignement Supérieur et de la Recherche Scientifique, Ministry of Higher Education and Scientific Research, Ministère de l’Enseignement Supérieur et de la Recherche Scientifique, Ministry of Higher Education and Scientific Research |
| Laboratoire pour l'Utilisation du Rayonnement Electromagnetique, CNRS-CEA-MESR, F-91405 Orsay, France | 11 | Centre National de la Recherche Scientifique, Commissariat à l'Énergie Atomique et aux Énergies Alternatives |
| Ministry of Higher Education and Research | 10 | no institution |
| Alain Burlaud, diplômé de ESCP, est professeur émérite du Conservatoire national des arts et métiers (Cnam) où il a dirigé l'Intec pendant 1 | 7 | Conservatoire National des Arts et Métiers, Ministère de l'Enseignement Superieur et de la Recherche |
| Alain Burlaud, diplômé de ESCP, est professeur émérite du Conservatoire national des arts et métiers (Cnam) où il a dirigé l’Intec pendant 1 | 7 | Conservatoire National des Arts et Métiers, Ministère de l'Enseignement Superieur et de la Recherche |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| French Ministry of Higher Education, Research and Innovation (MESRI) | 4 | no institution |
| Ministre de l'Enseignement supérieur et de la Recherche | 4 | Ministre de la Santé |
| Ministre de l’Enseignement supérieur et de la Recherche | 3 | Ministre de la Santé |
| Direction de la Recherche Scientifique du Ministère de l'Enseignement Supérieur et de la Recherche Scientifique, Abidjan, Côte d'Ivoire | 2 | no institution |
| Institut Universitaire de France, Ministère de l’Education Nationale, de l’Enseignement Supérieur et de la Recherche, 1 rue Descartes, F-752 | 2 | Ministere de l'Education Nationale, Institut Universitaire de France |
| Institut Universitaire de France, Ministère de l’Éducation Nationale, de l’Enseignement Supérieur et de la Recherche, 1 rue Descartes, CEDEX | 2 | Ministere de l'Education Nationale, Institut Universitaire de France |
| LURE, CNRS, CEA, MESR, Centre Universitaire, Bat. 209D, 91405 Orsay Cedex, France | 2 | Commissariat à l'Énergie Atomique et aux Énergies Alternatives, Centre National de la Recherche Scientifique |
| Unité de Génétique Oncologique Institut Curie Paris, France Supported by l'INSERM, le Comité de Paris de la Ligue Nationale Contre le Ca | 2 | Inserm, La Ligue Contre le Cancer |
| *PNUD [1], OuagadougouFernand Sanou est expert principal en prospective du projet PNUD-Burkina Faso de renforcement des capacités dans le do | 1 | Université Joseph Ki-Zerbo |
| *PNUD [1], OuagadougouFernand Sanou est expert principal en prospective du projet PNUD-Burkina Faso de renforcement des capacités dans le do | 1 | Université Joseph Ki-Zerbo |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
