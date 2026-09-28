# Boston University

[OpenAlex I111088046](https://openalex.org/institutions/I111088046) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Boston University itself): 247,842 → 235,265 (−5.1%).
- **Counting its units and predecessors** (the `lineage` filter): 248,868 → 236,201 (−5.1%).
- **Why:** most of the strings it lost now go to other institutions (87% of lost works), mostly Harvard University, University of Massachusetts Boston; most of the strings it gained had no institution before (67% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Boston University at all, about **96% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **96% do name it** or one of its units.

Net, the works that really are Boston University's (counting its units) went up by about 1.5%.

**11,886 strings lost Boston University** ([removed.csv.gz](removed.csv.gz)), on 20,738 works; **3,618 strings gained it** ([added.csv](added.csv)), on 8,597 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Harvard University, University of Massachusetts Boston, Massachusetts General Hospital) | 87% |
| To no institution | 12% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 67% |
| Up from one of its units or predecessors | 15% |
| From other institutions (mostly Marine Biological Laboratory, Boston Medical Center, Kingston University) | 18% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Northeastern University, Boston, U.S.A | 308 | Northeastern University |
| Harvard Medical School Boston, USA | 284 | Harvard University |
| Massachusetts General Hospital - Boston, USA | 220 | Massachusetts General Hospital |
| Northeastern University,Boston,USA | 147 | Northeastern University |
| Boston, U.S | 139 | no institution |
| Dept. of Neurobiology, Harvard Medical School, Boston, USA | 125 | Harvard University |
| Harvard Medical School, Boston, United States of America | 119 | Harvard University |
| Boston, U.S.A | 105 | no institution |
| Department of Epidemiology, Harvard School of Public Health, Boston, USA; | 88 | Harvard University |
| Boston College, Boston, United States | 73 | Boston College |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Boston Univ | 2,329 | no institution |
| Boston Univ. (United States) | 1,032 | no institution |
| Boston Univ, Boston, MA | 229 | no institution |
| Boston Univ Sch of Medicine, Boston, MA | 145 | no institution |
| BU | 104 | no institution |
| Department of Anatomy & Neurobiology, Boston University School of Medicine, Japan | 76 | no institution |
| Technology & Policy Research Initiative, BU School of Law | 60 | no institution |
| 1Boston University | 54 | no institution |
| Boston University Marine Program Marine Biological Laboratory Woods Hole, Massachusetts 02543 | 46 | Marine Biological Laboratory |
| University of Boston | 39 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
