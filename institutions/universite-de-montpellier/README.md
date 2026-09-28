# Université de Montpellier

[OpenAlex I19894307](https://openalex.org/institutions/I19894307) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Université de Montpellier itself): 155,811 → 116,817 (−25.0%).
- **Counting its units and predecessors** (the `lineage` filter): 264,071 → 250,685 (−5.1%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (78% of lost works); the largest share of the strings it gained moved up from one of its units (48% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université de Montpellier at all, about **69% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **92% do name it** or one of its units.

Net, the works that really are Université de Montpellier's (counting its units) went up by about 1.4%.

**48,435 strings lost Université de Montpellier** ([removed.csv.gz](removed.csv.gz)), on 77,135 works; **9,112 strings gained it** ([added.csv.gz](added.csv.gz)), on 12,499 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 78% |
| To other institutions (mostly Centre Hospitalier Universitaire de Montpellier, Centre de Coopération Internationale en Recherche Agronomique pour le Développement, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement) | 20% |
| To no institution | 2% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 34% |
| Up from one of its units or predecessors | 48% |
| From other institutions (mostly Centre National de la Recherche Scientifique, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement, Institut de Recherche pour le Développement) | 18% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| L2C - Laboratoire Charles Coulomb (1 place Eugène Bataillon Université Montpellier 34095 Montpellier Cedex 5 - France) | 955 | Laboratoire Charles Coulomb |
| IMAG - Institut Montpelliérain Alexander Grothendieck (UMR CNRS 5149 - Université Montpellier 2, Case courrier 051, 34095 Montpellier cedex  | 745 | Centre National de la Recherche Scientifique, Institut Montpelliérain Alexander Grothendieck, Université Montpellier 2 |
| CEFE, Univ Montpellier, CNRS, EPHE, IRD, Montpellier, France | 559 | Centre National de la Recherche Scientifique, Centre d'Écologie Fonctionnelle et Évolutive |
| UMPV - Université de Montpellier Paul-Valéry (Université de Montpellier Paul-Valéry Route de Mende 34199 Montpellier Cedex 5 - France) | 352 | Université Paul-Valéry Montpellier, Université de Montpellier Paul-Valéry |
| CREAM - Centre de Recherches et d’Études Administratives de Montpellier - EA 2038 (Faculté de Droit  39, rue de l’Université  34060 Montpe | 341 | Centre de Recherches et d'Etudes Administratives de Montpellier |
| Université Montpellier 1 | 324 | Université Montpellier 1 |
| Université Montpellier 2 | 282 | Université Montpellier 2 |
| CHU Montpellier = Montpellier University Hospital (371, avenue du Doyen Gaston Giraud 34295 MONTPELLIER cedex 5 - France) | 251 | Centre Hospitalier Universitaire de Montpellier |
| Université Montpellier 2 - Sciences et Techniques | 245 | Université Montpellier 2 |
| Université de Montpellier II | 227 | Université Montpellier 2 |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Géosciences Montpellier, Université de Montpellie | 500 | Géosciences Montpellier |
| Thèses d'exercice et mémoires - UFR des sciences pharmaceutiques et biologiques de Montpellier | 445 | no institution |
| IDU - Institut des usages (Institut des Usages Faculté de Droit de Montpellier 39 Rue de l’Université, 34000 Montpellier - France) | 107 | Gestion de l'Eau, Acteurs, Usages |
| Institut universitaire de formation des maîtres - Montpellier | 73 | no institution |
| University Montpellier | 60 | no institution |
| CIRAD, UPR GECO, F- 97285 Le Lamentin, Martinique, France & GECO, University Montpellier, CIRAD, Montpellier, France | 55 | Centre de Coopération Internationale en Recherche Agronomique pour le Développement, Géosciences Montpellier |
| Mémoires - Département d'orthophonie de Montpellier | 54 | no institution |
| ISEM, Univ de Montpellier, CNRS, IRD, Montpellier, France | 47 | Institut de Recherche pour le Développement, Centre National de la Recherche Scientifique, Institut des Sciences de l'Evolution de Montpellier |
| IUFM de Montpellier | 41 | no institution |
| University Montpellier, Montpellier, France | 34 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
