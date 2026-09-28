# University of California, Irvine

[OpenAlex I204250578](https://openalex.org/institutions/I204250578) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of California, Irvine itself): 211,641 → 216,336 (+2.2%).
- **Counting its units and predecessors** (the `lineage` filter): 211,645 → 216,580 (+2.3%).
- **Why:** most of the strings it lost now go to other institutions (54% of lost works), mostly University of California, Irvine Medical Center, California Southern University; most of the strings it gained were assigned to other institutions before (59% of gained works), mostly Irvine University, University of California, Irvine Medical Center.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of California, Irvine at all, about **75% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **88% do name it** or one of its units.

Net, the works that really are University of California, Irvine's (counting its units) went up by about 2.4%.

**1,581 strings lost University of California, Irvine** ([removed.csv](removed.csv)), on 2,181 works; **6,840 strings gained it** ([added.csv.gz](added.csv.gz)), on 11,132 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 3% |
| To its parent institution | 3% |
| To other institutions (mostly University of California, Irvine Medical Center, California Southern University, Westcliff University) | 54% |
| To no institution | 40% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 39% |
| Up from one of its units or predecessors | 0% |
| Down from its parent institution | 2% |
| From other institutions (mostly Irvine University, University of California, Irvine Medical Center, Beckman Laser Institute and Medical Clinic) | 59% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Faculty of Chemistry , California South University , 14731 Comet St. Irvine , CA 92604 , USA | 93 | California Southern University |
| University of California (Irvine) Medical Center | 45 | University of California, Irvine Medical Center |
| Faculty of Chemistry , California South University , 14731 Comet St. Irvine , CA 92604 , USA, | 27 | California Southern University |
| UCI Medical Center, Orange, CA | 25 | University of California, Irvine Medical Center, UC Irvine Health |
| Department of Surgery, University of California-Irvine Medical Center, Orange, USA | 14 | University of California, Irvine Medical Center |
| Irvine, California, U.S.A | 11 | no institution |
| Irvine, U.S.A | 11 | no institution |
| Department of Computer Science , Westcliff University , Irvine , CA 92614 , USA | 8 | Westcliff University |
| UC Irvine, Chao Family Comprehensive Cancer Center, Orange, CA | 8 | UC Irvine Chao Family Comprehensive Cancer Center |
| UCI Medical Center, Chao Family Comprehensive Cancer Center, Gastrointestinal Oncology, 101, The City Drive, Bldg. 23, Rt.81, Rm.330, C92668 | 8 | UC Irvine Chao Family Comprehensive Cancer Center |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Dep. Chem., Univ. Calif., Irvine, CA 92697, USA | 372 | Irvine University |
| Dept. of Electr. & Comput. Eng., California Univ., Irvine, CA, USA#TAB# | 296 | Irvine University |
| Dep. Chem., Univ. Calif., Irvine, CA 92717, USA | 269 | Irvine University |
| UCI | 229 | no institution |
| Univ of California, Irvine, CA | 223 | Irvine University |
| Department of Electrical Engineering and Computer Science, University of California at Irvine, Irvine, CA, USA | 120 | no institution |
| Univ of California, Irvine, Irvine, CA | 98 | no institution |
| California Univ., Irvine, CA (United States) | 78 | Irvine University |
| California, University, Irvine | 77 | no institution |
| California, Univ., Irvine | 74 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
