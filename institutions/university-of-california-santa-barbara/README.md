# University of California, Santa Barbara

[OpenAlex I154570441](https://openalex.org/institutions/I154570441) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of California, Santa Barbara itself): 148,253 → 149,027 (+0.5%).
- **Counting its units and predecessors** (the `lineage` filter): 156,564 → 157,145 (+0.4%).
- **Why:** most of the strings it lost now have no institution (56% of lost works); the largest share of the strings it gained had no institution before (40% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**716 strings lost University of California, Santa Barbara** ([removed.csv](removed.csv)), on 872 works; **1,716 strings gained it** ([added.csv](added.csv)), on 2,425 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 4% |
| To its parent institution | 4% |
| To other institutions (mostly University of California, Los Angeles, University of California, Berkeley, University of Southern California) | 37% |
| To no institution | 56% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 40% |
| Up from one of its units or predecessors | 27% |
| Down from its parent institution | 0% |
| From other institutions (mostly California Department of Education, Santa Barbara City College, Dynamic Systems (United States)) | 33% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Department of Electrical and Computer Engineering, University of California, Los Angeles, Santa Barbara, CA, USA | 24 | University of California, Los Angeles |
| Santa Barbara, Cal., U.S.A | 9 | no institution |
| #National Center for Ecological Analysis and Synthesis, 735 State St., Santa Barbara, CA, 93101, USA | 8 | National Center for Ecological Analysis and Synthesis |
| Santa Barbara, Calif., U.S.A | 8 | no institution |
| Santa Barbara , CA 93108 | 6 | no institution |
| Santa Barbara, California, U.S.A | 6 | no institution |
| University of Santa Barbara; | 6 | no institution |
| Department of Electrical and Computer Engineering, University of California Berkeley, Santa Barbara, CA, USA | 5 | University of California, Berkeley |
| UNIVERSITY OF BRITISH COLUMBIA CALIFORNIA INSTITUTE OF TECHNOLOGY UNIVERSITY OF CALIFORNIA, BERKELEY UNIVERSITY OF CALIFORNIA, DAVIS UNIVERS | 5 | University of California, Davis, University of California, Berkeley |
| [Department of Electrical and Computer Engineering, University of California, Los Angeles, Santa Barbara, CA, USA] | 5 | University of California, Los Angeles |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| U California, Dept of Psychology, Santa Barbara, CA, US | 69 | California Department of Education |
| Institute for Theoretical Physics, University of California, 93106, Santa Barbara, CA, USA | 27 | Kavli Institute for Theoretical Physics |
| Institute for Theoretical Physics, University of California, 93106, Santa Barbara, California | 26 | Kavli Institute for Theoretical Physics |
| Santa Barbara College, University of California | 22 | Santa Barbara City College |
| Department of Computer Science [Santa Barbara] | 19 | no institution |
| Speech Technology Laboratory, 3888 State Street, Santa Barbara, CA 93105 | 19 | State Street (United States) |
| U California, Graduate School of Education, Santa Barbara, US | 17 | California Department of Education |
| University of Santa Barbara | 17 | no institution |
| Kavli Institute for Theoretical Physics, UCSB | 15 | Instituto de Física Teórica, Kavli Institute for Theoretical Physics |
| Bren School of Environmental Science and Management, University of California | 14 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
