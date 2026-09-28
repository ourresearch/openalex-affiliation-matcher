# Université de Montréal

[OpenAlex I70931966](https://openalex.org/institutions/I70931966) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Université de Montréal itself): 192,796 → 201,405 (+4.5%).
- **Counting its units and predecessors** (the `lineage` filter): 198,352 → 206,877 (+4.3%).
- **Why:** most of the strings it lost now go to other institutions (73% of lost works), mostly Université du Québec à Montréal, Centre Hospitalier de l’Université de Montréal; most of the strings it gained were assigned to other institutions before (76% of gained works), mostly Centre Hospitalier de l’Université de Montréal, Hôpital Notre-Dame.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université de Montréal at all, about **73% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **43% do name it** or one of its units.

**2,123 strings lost Université de Montréal** ([removed.csv](removed.csv)), on 2,594 works; **19,026 strings gained it** ([added.csv.gz](added.csv.gz)), on 24,126 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 2% |
| To other institutions (mostly Université du Québec à Montréal, Centre Hospitalier de l’Université de Montréal, Polytechnique Montréal) | 73% |
| To no institution | 25% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 21% |
| Up from one of its units or predecessors | 3% |
| From other institutions (mostly Centre Hospitalier de l’Université de Montréal, Hôpital Notre-Dame, Polytechnique Montréal) | 76% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Centre de Recherche en Calcul Thermochimique, Ecole Polytechnique, Campus de l'Universitè de Montrèal, Montrèal, Canada | 39 | Polytechnique Montréal |
| Centre Hospitalier de l'Université de Montréal, Hôpital Notre‐Dame, Montreal, Quebec, Canada | 17 | Hôpital Notre-Dame, Centre Hospitalier de l’Université de Montréal |
| Department of Education and Pedagogy, Université de Québec à Montréal, Montréal, QC, Canada | 17 | Université du Québec à Montréal |
| Institut Universitaire de Geriatrie de Montreal | 16 | Institut Universitaire de Gériatrie de Montréal |
| Department of Electrical and Computer Engineering [Montréal] (3480 University Street, Montreal, Quebec, Canada H3A 0E9 - Canada) | 15 | no institution |
| Est diplômé en psychologie cognitive (Université Laval – Canada) et docteur en neuropsychologie (Université de Montréal). Il a travaillé pen | 12 | University of Illinois Urbana-Champaign, Institut Universitaire de Gériatrie de Montréal |
| Département de Sciences Biologiques [Montreal] | 11 | no institution |
| Département de sciences biologiques, Universitè de Montrèal, Montrèal, Quèbec, Canada | 10 | no institution |
| Ville de Montréal | 9 | no institution |
| Polytechnique University of Montreal, Quebec, Canada | 8 | Polytechnique Montréal |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| EPM - École Polytechnique de Montréal (Campus de l'Université de Montréal - 2500, chemin de Polytechnique - Montréal (Québec) H3T 1J4 - Cana | 353 | Polytechnique Montréal |
| rudit est un consortium interuniversitaire sans but lucratif compos de l'Universit de Montral, l'Universit Laval et l'Universit du Qubec  Mo | 297 | no institution |
| Laboratoire De Paleobiogeog. et du Palynol., D鰡rtement de g鯧raphie, Universit頤e Montr顬, C.P. 6128, Succ. Centre-ville, Montr顬 PQ H3C 3J7, CA | 135 | no institution |
| Département d'Informatique et de Recherche Opérationnelle [Montreal] | 123 | no institution |
| Institut Universitaire de Gériatrie de Montréal | 121 | Institut Universitaire de Gériatrie de Montréal |
| Laboratoire Jacques-Rousseau, D鰡rtement de g鯧raphie, Universit頤e Montr顬, C.P. 6128 Succursale A, Montr顬, PQ H3C 3J7, CANADA | 87 | no institution |
| UdeM | 68 | Universidad de Managua |
| Department of Mathematics and Statistics [Montréal] | 54 | no institution |
| CR CHUM - Centre de Recherche du Centre Hospitalier de l’Université de Montréal (Canada) | 48 | Centre Hospitalier de l’Université de Montréal |
| SIMEXP Lab, CRIUGM, University of Montréal, Montréal, Canada | 45 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
