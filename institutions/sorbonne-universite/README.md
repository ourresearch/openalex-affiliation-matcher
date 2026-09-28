# Sorbonne Université

[OpenAlex I39804081](https://openalex.org/institutions/I39804081) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Sorbonne Université itself): 365,179 → 188,116 (−48.5%).
- **Counting its units and predecessors** (the `lineage` filter): 627,738 → 559,293 (−10.9%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (86% of lost works); most of the strings it gained moved up from one of its units (64% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Sorbonne Université at all, about **61% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **67% do name it** or one of its units.

**182,287 strings lost Sorbonne Université** ([removed.csv.gz](removed.csv.gz)), on 262,417 works; **1,856 strings gained it** ([added.csv](added.csv)), on 5,848 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 86% |
| To other institutions (mostly Pitié-Salpêtrière Hospital, Inserm, Centre National de la Recherche Scientifique) | 13% |
| To no institution | 1% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 21% |
| Up from one of its units or predecessors | 64% |
| From other institutions (mostly Université Paris 1 Panthéon-Sorbonne, Université Paris Cité, Centre d'Économie de la Sorbonne) | 15% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Paris 6 | 2,928 | Université Pierre-et-Marie-Curie |
| Paris 4 | 2,225 | Paris-Sorbonne University |
| Université Pierre et Marie Curie, Paris, France | 1,398 | Université Pierre-et-Marie-Curie |
| LESIA, Observatoire Paris-Site de Meudon, Meudon, France | 1,349 | Observatoire de Paris, Laboratoire d’études spatiales et d’instrumentation en astrophysique |
| Universite Pierre et Marie Curie | 1,130 | Université Pierre-et-Marie-Curie |
| Université Pierre et Marie Curie - Paris 6 | 1,107 | Université Pierre-et-Marie-Curie |
| Pierre-and-Marie-Curie University | 1,060 | Université Pierre-et-Marie-Curie |
| UPMC - Université Pierre et Marie Curie - Paris 6 (4 place Jussieu - 75005 Paris - France) | 1,052 | Université Pierre-et-Marie-Curie |
| Université Pierre et Marie Curie | 732 | Université Pierre-et-Marie-Curie |
| University of Paris 4-Sorbonne | 546 | Paris-Sorbonne University |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Sorbonne, Identités, relations internationales et civilisations de l’Europe | 1,430 | Sorbonne - Identités, Relations Internationales et Civilisations de l’Europe |
| Institut de recherche en droit international et européen de la Sorbonne | 709 | Sorbonne - Identités, Relations Internationales et Civilisations de l’Europe |
| SIRICE - Sorbonne, Identités, relations internationales et civilisations de l’Europe (UMR SIRICE Bureau F 628 17, rue de la Sorbonne75231 Pa | 655 | Sorbonne - Identités, Relations Internationales et Civilisations de l’Europe |
| IREDIES - Institut de recherche en droit international et européen de la Sorbonne (12, place du Panthéon 75231 Paris Cedex 5 - France) | 167 | no institution |
| Sorbonne | 114 | no institution |
| OM-MP - Équipe Mondes pharaoniques (Équipe Mondes pharaoniques de l’UMR 8167 Centre de recherches égyptologiques de la Sorbonne (CRES) 1,  | 65 | no institution |
| Centre de philosophie contemporaine de la Sorbonne | 61 | no institution |
| Labex OBVIL - L’Observatoire de la vie littéraire (Labex OBVIL - Université de la Sorbonne, 28 Rue Serpente, 75006 Paris, France - France) | 60 | no institution |
| Université Paris Sorbonne, IEES-Biodis, Paris, France | 44 | Université Sorbonne Nouvelle, Institut d'écologie et des sciences de l'environnement de Paris, Paris-Sorbonne University |
| University of Paris , Sorbonne | 35 | Université Paris Cité |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
