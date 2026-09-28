# Indiana University

[OpenAlex I592451](https://openalex.org/institutions/I592451) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Indiana University itself): 165,690 → 164,947 (−0.4%).
- **Counting its units and predecessors** (the `lineage` filter): 351,300 → 337,745 (−3.9%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (98% of lost works); most of the strings it gained moved up from one of its units (94% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Indiana University at all, about **65% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **94% do name it** or one of its units.

Net, the works that really are Indiana University's (counting its units) went down by about 0.4%.

**15,959 strings lost Indiana University** ([removed.csv.gz](removed.csv.gz)), on 57,036 works; **33,774 strings gained it** ([added.csv.gz](added.csv.gz)), on 66,668 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 98% |
| To other institutions (mostly Indiana University – Purdue University Fort Wayne, University of Indianapolis, University of Michigan) | 1% |
| To no institution | 1% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 4% |
| Up from one of its units or predecessors | 94% |
| From other institutions (mostly Indiana University – Purdue University Fort Wayne, Indiana University of Pennsylvania, WisdomTools (United States)) | 1% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Indiana University Bloomington | 5,296 | Indiana University Bloomington |
| Indiana University School of Medicine | 4,620 | Indiana University School of Medicine |
| Indiana University. Bloomington | 3,278 | Indiana University Bloomington |
| Indiana University, Bloomington | 3,145 | Indiana University Bloomington |
| Indiana University, Bloomington, USA | 1,467 | Indiana University Bloomington |
| Indiana University, Bloomington, United States | 1,395 | Indiana University Bloomington |
| Indiana University, Bloomington, IN | 1,044 | Indiana University Bloomington |
| Indiana University, Bloomington, Indiana | 918 | Indiana University Bloomington |
| Indiana University, Bloomington, Indiana, USA | 671 | Indiana University Bloomington |
| Indiana University Bloomington, Bloomington, IN, USA | 624 | Indiana University Bloomington |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Indiana U | 984 | no institution |
| Dep. Chem., Indiana Univ., Bloomington, IN 47405, USA | 534 | Indiana University Bloomington |
| Indiana University - Kelley School of Business - Department of Finance, 1309 E. 10th St., Bloomington, IN 47405, United States | 385 | Indiana University Bloomington |
| Indiana University Bloomington - School of Public & Environmental Affairs (SPEA) | 361 | Indiana University Bloomington |
| Indiana University Bloomington - Department of Economics | 264 | Indiana University Bloomington |
| Indiana Univ., Bloomington, IN (United States) | 251 | Indiana University Bloomington |
| Indiana University Maurer School of Law, 211 S. Indiana Avenue, Bloomington, IN 47405, United States | 241 | Indiana University Bloomington |
| Indiana University Robert H. McKinney School of Law, 530 West New York Street, Indianapolis, IN 46202, United States | 225 | Indiana University – Purdue University Indianapolis |
| Indiana Univ. (United States) | 203 | Indiana University – Purdue University Indianapolis |
| Indiana University Bloomington - School of Public & Environmental Affairs (SPEA), 1315 East Tenth Street, Bloomington, IN 47405, United Stat | 203 | Indiana University Bloomington |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
