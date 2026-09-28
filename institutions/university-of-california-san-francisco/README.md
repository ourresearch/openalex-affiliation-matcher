# University of California, San Francisco

[OpenAlex I180670191](https://openalex.org/institutions/I180670191) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of California, San Francisco itself): 327,292 → 345,788 (+5.7%).
- **Counting its units and predecessors** (the `lineage` filter): 337,980 → 352,772 (+4.4%).
- **Why:** most of the strings it lost now have no institution (58% of lost works); most of the strings it gained were assigned to other institutions before (62% of gained works), mostly University of California San Francisco Medical Center, UCSF Benioff Children's Hospital.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of California, San Francisco at all, about **88% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **100% do name it** or one of its units.

Net, the works that really are University of California, San Francisco's (counting its units) went up by about 6.5%.

**2,647 strings lost University of California, San Francisco** ([removed.csv](removed.csv)), on 5,225 works; **32,607 strings gained it** ([added.csv.gz](added.csv.gz)), on 45,279 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 1% |
| To its parent institution | 10% |
| To other institutions (mostly University of San Francisco, Stanford University, Stanford Medicine) | 31% |
| To no institution | 58% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 24% |
| Up from one of its units or predecessors | 13% |
| Down from its parent institution | 1% |
| From other institutions (mostly University of California San Francisco Medical Center, UCSF Benioff Children's Hospital, San Francisco VA Medical Center) | 62% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| San Francisco, California, USA | 919 | no institution |
| University of California , , , , | 857 | no institution |
| University of California, San | 67 | no institution |
| Department of Ophthalmology, University of California | 26 | University of California System |
| University of California Medical Center, San Francisco, | 23 | University of California San Francisco Medical Center |
| San Francisco California USA | 21 | no institution |
| From the Department of Medicine, Stanford University School of Medicine, San Francisco, Calif | 20 | Stanford University, Stanford Medicine |
| San Francisco , California , USA | 18 | no institution |
| Department of Radiology, Stanford University School of Medicine, San Francisco, Calif | 13 | Stanford University, Stanford Medicine |
| From the Department of Obstetrics and Gynecology, Stanford University, School of Medicine, San Francisco, California | 13 | Stanford University, Stanford Medicine |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| UCSF | 1,738 | Universidad Católica de Santa Fe |
| University of California at San Francisco, San Francisco, CA, USA | 310 | no institution |
| Department of Obstetrics, Gynecology & Reproductive Sciences, UCSF | 216 | no institution |
| University of California at San Francisco, San Francisco, CA | 210 | no institution |
| Univ of California, San Francisco, San Francisco, CA | 186 | no institution |
| UC Berkeley - UCSF Graduate Program in Bioengineering | 150 | Bioengineering Center, University of California, Berkeley |
| Univ of California San Francisco, San Francisco, CA | 137 | no institution |
| Philip R. Lee Institute for Health Policy Studies, University of California, San Francisco | 128 | Philip R. Lee Institute for Health Policy Studies |
| 1UCSF, San Francisco, CA; | 108 | City College of San Francisco |
| Univ of California At San Francisco, San Francisco, CA, United States | 99 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
