# University of Cambridge

[OpenAlex I241749](https://openalex.org/institutions/I241749) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of Cambridge itself): 483,132 → 543,550 (+12.5%).
- **Counting its units and predecessors** (the `lineage` filter): 513,716 → 561,084 (+9.2%).
- **Why:** most of the strings it lost now go to other institutions (54% of lost works), mostly King's College Hospital, King's College London; the largest share of the strings it gained were assigned to other institutions before (47% of gained works), mostly Cavendish Hospital, St. John's College of Nursing.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Cambridge at all, about **69% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **92% do name it** or one of its units.

Net, the works that really are University of Cambridge's (counting its units) went up by about 10.5%.

**3,420 strings lost University of Cambridge** ([removed.csv](removed.csv)), on 6,208 works; **32,670 strings gained it** ([added.csv.gz](added.csv.gz)), on 97,929 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 3% |
| To other institutions (mostly King's College Hospital, King's College London, Addenbrooke's Hospital) | 54% |
| To no institution | 42% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 45% |
| Up from one of its units or predecessors | 8% |
| From other institutions (mostly Cavendish Hospital, St. John's College of Nursing, The King's College) | 47% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Science, AAAS, Cambridge CB2 1LQ, UK | 372 | no institution |
| Institute of Liver Studies , King’s College Hospital, London, UK | 115 | King's College Hospital |
| #N#Clare Hall, Cambridge#N# | 85 | no institution |
| King's College Newcastle Upon Tyne | 82 | no institution |
| Cambridge, U.K | 76 | no institution |
| Trinity Coll., Cambridge, UK | 57 | no institution |
| Newnham college | 50 | Newham College |
| Department of Physics, King?s College, Strand, London WC2R 2LS,#N#UK | 45 | King's College London |
| Department of Radiology; King's College Hospital; London UK | 44 | King's College Hospital |
| Cambridge Crystallographic Data Centre, 12 Union Road,Cambridge,UK | 41 | Cambridge Crystallographic Data Centre |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Trinity College, Cambridge | 2,205 | no institution |
| King's College, Cambridge | 1,217 | The King's College |
| Trinity college, Cambridge | 1,088 | no institution |
| Peterhouse, Cambridge | 941 | Westinghouse Electric (United States) |
| Cavendish Laboratory, Cambridge | 906 | Cavendish Hospital |
| Gonville and Caius College, Cambridge | 868 | Canisius College |
| ST. John's College, Cambridge | 803 | St. John's College of Nursing |
| St John's College, Cambridge | 790 | St. John's College of Nursing |
| Emmanuel College, Cambridge | 749 | Emmanuel College - Massachusetts |
| Clare College, Cambridge | 711 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
