# Graduate Institute of International and Development Studies

[OpenAlex I951315](https://openalex.org/institutions/I951315) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Graduate Institute of International and Development Studies itself): 8,935 → 7,862 (−12.0%).
- **Counting its units and predecessors** (the `lineage` filter): 9,294 → 9,554 (+2.8%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (86% of lost works); the largest share of the strings it gained had no institution before (49% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Graduate Institute of International and Development Studies at all, about **37% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **94% do name it** or one of its units.

Net, the works that really are Graduate Institute of International and Development Studies's (counting its units) went up by about 3.2%.

**640 strings lost Graduate Institute of International and Development Studies** ([removed.csv](removed.csv)), on 1,496 works; **187 strings gained it** ([added.csv](added.csv)), on 201 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 86% |
| To other institutions (mostly University of Geneva, Swansea University, Institut catholique de paris) | 4% |
| To no institution | 10% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 49% |
| Up from one of its units or predecessors | 19% |
| From other institutions (mostly University of Geneva, Institut de Recherche pour le Développement, Geneva Centre for Security Policy) | 32% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Graduate Institute of International Studies, Geneva | 196 | Graduate Institute of International Studies |
| Graduate Institute of International Studies, Geneva, Switzerland | 125 | Graduate Institute of International Studies |
| Graduate Institute of International Studies | 68 | Graduate Institute of International Studies |
| Institut universitaire d’études du développement, Genève | 49 | Graduate Institute of Development Studies |
| Graduate Institute of International Studies, Geneva and University Centre for International Humanitarian Law | 46 | Graduate Institute of International Studies |
| Graduate Institute of International Studies (Geneva) | 44 | Graduate Institute of International Studies |
| International Management School Geneva (IMSG), Geneva | 33 | no institution |
| Graduate Institute of International Studies , Geneva | 32 | Graduate Institute of International Studies |
| Institut Universitaire de Hautes Etudes Internationales, Geneva | 24 | Graduate Institute of International Studies |
| The Graduate Institute of International Studies, Geneva, Switzerland | 18 | Graduate Institute of International Studies |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Institut d’Etudes du Développement, Genève et Institut Universitaire de Hautes Etudes Internationales, Genève | 5 | Graduate Institute of Development Studies, Graduate Institute of International Studies |
| Graduate Insitute of Internatonal and Development Studies | 3 | Institute of Development Studies |
| Anthropologue, spécialiste de l’anthropologie rurale et religieuse et membre du comité de rédaction de Recherches Familiales. Il enseigne à  | 2 | no institution |
| Christine Verschuur est Senior lecturer à l’Institut de hautes études internationales et du développement à Genève. Elle fait partie du corp | 2 | Laboratoire de Biologie du Développement, Université Paris 1 Panthéon-Sorbonne |
| Daniel Meier, docteur en sociologie politique, est chercheur à l'Institut de hautes études internationales et du développement (Genève) et c | 2 | no institution |
| Est politologue. Elle a achevé un doctorat en études du développement en septembre 2009 à l’Institut de hautes études internationales et du  | 2 | no institution |
| Geneva Graduate Institute, Switzerland and KU Leuven, Belgium | 2 | no institution |
| Graduate Institute of Internaitonal and Development Studies | 2 | Institute of Development Studies |
| Isabelle Schulte-Tenckhoff est professeure honoraire d’anthropologie à l’Institut de hautes études internationales et du développement, Genè | 2 | no institution |
| Université de Genève / Graduate Institute / | 2 | University of Geneva |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
