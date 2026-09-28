# University College London

[OpenAlex I45129253](https://openalex.org/institutions/I45129253) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University College London itself): 609,590 → 540,661 (−11.3%).
- **Counting its units and predecessors** (the `lineage` filter): 624,627 → 552,887 (−11.5%).
- **Why:** most of the strings it lost now go to other institutions (88% of lost works), mostly Great Ormond Street Hospital, The Royal Free Hospital; most of the strings it gained were assigned to other institutions before (53% of gained works), mostly University College Lahore, Middlesex University London.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University College London at all, about **90% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **89% do name it** or one of its units.

**84,688 strings lost University College London** ([removed.csv.gz](removed.csv.gz)), on 169,935 works; **17,224 strings gained it** ([added.csv.gz](added.csv.gz)), on 40,977 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 6% |
| To its parent institution | 4% |
| To other institutions (mostly Great Ormond Street Hospital, The Royal Free Hospital, National Hospital for Neurology and Neurosurgery) | 88% |
| To no institution | 3% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 42% |
| Up from one of its units or predecessors | 3% |
| Down from its parent institution | 2% |
| From other institutions (mostly University College Lahore, Middlesex University London, Institute of Child Health) | 53% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Hospital for Sick Children | 3,494 | Great Ormond Street Hospital, Hospital for Sick Children |
| Moorfields Eye Hospital, London, UK | 1,352 | Moorfields Eye Hospital |
| Great Ormond Street Hospital | 1,318 | Great Ormond Street Hospital |
| University College London Hospitals NHS Foundation Trust | 1,235 | University College London Hospitals NHS Foundation Trust |
| National Hospital for Neurology and Neurosurgery | 1,017 | National Hospital for Neurology and Neurosurgery |
| Royal Free Hospital, London, UK | 1,013 | The Royal Free Hospital |
| University College Hospital | 905 | University College Hospital |
| University College London Hospitals NHS Foundation Trust, London, UK | 880 | University College London Hospitals NHS Foundation Trust |
| Moorfields Eye Hospital, London, United Kingdom | 858 | Moorfields Eye Hospital |
| Great Ormond Street Hospital, London, UK | 835 | Great Ormond Street Hospital |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| UCL | 6,139 | University College Lahore |
| @UCL-ARC | 555 | no institution |
| University College of London [London] | 454 | no institution |
| ICTEAM, UCL | 418 | Institut Catholique d'Arts et Métiers |
| UCL Institute of Archaeology | 386 | Institute of Archaeology |
| UCL , | 384 | no institution |
| Institute of Child Health, London, UK | 373 | no institution |
| Dep. Chem., Univ. Coll., London WC1H 0AJ, UK | 340 | no institution |
| UCL Institute of Education | 316 | no institution |
| College London | 313 | The London College |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
