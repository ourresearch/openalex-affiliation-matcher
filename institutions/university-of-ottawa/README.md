# University of Ottawa

[OpenAlex I153718931](https://openalex.org/institutions/I153718931) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of Ottawa itself): 176,836 → 174,961 (−1.1%).
- **Counting its units and predecessors** (the `lineage` filter): 181,756 → 184,457 (+1.5%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (95% of lost works); the largest share of the strings it gained had no institution before (49% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**6,287 strings lost University of Ottawa** ([removed.csv.gz](removed.csv.gz)), on 12,517 works; **4,312 strings gained it** ([added.csv](added.csv)), on 6,164 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 95% |
| To other institutions (mostly University of Toronto, University of Calgary, University of British Columbia) | 3% |
| To no institution | 2% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 49% |
| Up from one of its units or predecessors | 10% |
| From other institutions (mostly Ottawa University, Central China Normal University, Carleton University) | 41% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Division of Cardiology, University of Ottawa Heart Institute, Ottawa, Ontario, Canada | 390 | Ottawa Heart Institute |
| University of Ottawa Heart Institute, Ottawa, ON, Canada | 335 | Ottawa Heart Institute |
| University of Ottawa Heart Institute, Ottawa, Canada | 333 | Ottawa Heart Institute |
| Division of Cardiac Surgery, University of Ottawa Heart Institute, Ottawa, Ontario, Canada | 278 | Ottawa Heart Institute |
| University of Ottawa Heart Institute | 239 | Ottawa Heart Institute |
| Division of Cardiology, University of Ottawa Heart Institute, Ottawa, ON, Canada | 122 | Ottawa Hospital, Ottawa Heart Institute |
| Division of Cardiology, University of Ottawa Heart Institute, Ottawa, Canada | 91 | Ottawa Heart Institute |
| University of Ottawa Heart Institute, Ontario, Canada | 70 | Ottawa Heart Institute |
| Cardiovascular Research Methods Centre, University of Ottawa Heart Institute, Ottawa, Ontario, Canada | 67 | Ottawa Heart Institute |
| Univ of Ottawa Heart Institute, Ottawa, Canada | 67 | Ottawa Heart Institute |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Sch. of Information Technol. & Eng., Ottawa Univ., Ont., Canada#TAB# | 209 | Ottawa University |
| Telfer School of Management, U. of Ottawa | 73 | no institution |
| Sch. of Inf. Technol. & Eng, Ottawa Univ., Ont | 67 | Ottawa University |
| U. of Ottawa | 53 | Ottawa University |
| University of Ottowa | 47 | no institution |
| Uni- versité d'Ottawa | 46 | no institution |
| School of Computer Science [Ottawa] (Herzberg Building 1125 Colonel By Drive, Ottawa, Ontario, K1S 5B6 Canada - Canada) | 36 | no institution |
| Sch. of Inf. Technol. & Eng., Ottawa Univ., Ottawa, ON | 35 | Ottawa University |
| [Ottawa Univ., Ottawa] | 35 | Ottawa University |
| University of Ottawa, USA | 32 | Ottawa University |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
