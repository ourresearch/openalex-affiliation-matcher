# University of York

[OpenAlex I52099693](https://openalex.org/institutions/I52099693) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of York itself): 108,356 → 112,548 (+3.9%).
- **Counting its units and predecessors** (the `lineage` filter): 108,839 → 113,973 (+4.7%).
- **Why:** most of the strings it lost now go to other institutions (63% of lost works), mostly York University, New York University; most of the strings it gained were assigned to other institutions before (70% of gained works), mostly York University, Universities UK.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of York at all, about **91% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **52% do name it** or one of its units.

Net, the works that really are University of York's (counting its units) went up by about 2.9%.

**591 strings lost University of York** ([removed.csv](removed.csv)), on 1,479 works; **2,584 strings gained it** ([added.csv](added.csv)), on 7,084 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly York University, New York University, New York State Psychiatric Institute) | 63% |
| To no institution | 37% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 30% |
| From other institutions (mostly York University, Universities UK, New York University) | 70% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| York, UK | 245 | no institution |
| New York U, Department of Psychology, New York, NY, US | 58 | New York University |
| New York State Psychiatric Inst, New York | 54 | New York State Psychiatric Institute |
| Dept. of Psychology, York University, North York, Canada | 48 | York University |
| Department of Biology, York University , North York, Canada | 41 | York University |
| New York U, New YOrk, NY, US | 37 | New York University |
| Dept of Comput. Sci., York Univ., North York, Ont., Canada | 36 | York University |
| York University, North York, Ont., Canada#TAB# | 33 | York University |
| University of York St John | 27 | York St John University |
| University of Nottingham - Malaysia Campus, york, york YO10 5BR, United Kingdom | 21 | University of Nottingham, University of Nottingham Malaysia Campus |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Department of Psychology, York University | 355 | York University |
| York U | 218 | no institution |
| Dept. of Comput. Sci., York Univ., UK#TAB# | 216 | no institution |
| [Dept. of Electron., York Univ., UK] | 194 | Universities UK |
| Université York | 135 | York University |
| Centre for Vision Research, York University | 131 | York University |
| York Univ., , UK | 124 | no institution |
| School of Kinesiology and Health Science, York University | 102 | York University |
| York University - Department of Economics | 77 | York University |
| Department of Biology, York University | 74 | York University |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
