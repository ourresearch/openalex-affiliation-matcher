# Sorbonne Université

[OpenAlex I39804081](https://openalex.org/institutions/I39804081) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Sorbonne Université itself): 365,154 → 184,516 (−49.5%).
- **Counting its units and predecessors** (the `lineage` filter): 627,718 → 531,817 (−15.3%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (74% of lost works); most of the strings it gained moved up from one of its units (62% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Sorbonne Université at all, about **61% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **67% do name it** or one of its units.

Net, the works that really are Sorbonne Université's (counting its units) went down by about 5.0%.

**186,124 strings lost Sorbonne Université** ([removed.csv.gz](removed.csv.gz)), on 266,928 works; **1,639 strings gained it** ([added.csv](added.csv)), on 5,595 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 74% |
| To other institutions (mostly Pitié-Salpêtrière Hospital, Centre National de la Recherche Scientifique, Inserm) | 20% |
| To no institution | 7% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 22% |
| Up from one of its units or predecessors | 62% |
| From other institutions (mostly Université Paris 1 Panthéon-Sorbonne, Université Paris Cité, Centre d'Économie de la Sorbonne) | 16% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Paris 6 | 2,928 | no institution |
| Paris 4 | 2,225 | no institution |
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
