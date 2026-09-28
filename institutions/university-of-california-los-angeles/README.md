# University of California, Los Angeles

[OpenAlex I161318765](https://openalex.org/institutions/I161318765) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of California, Los Angeles itself): 504,745 → 553,314 (+9.6%).
- **Counting its units and predecessors** (the `lineage` filter): 505,708 → 554,014 (+9.6%).
- **Why:** the largest share of the strings it lost now go to other institutions (44% of lost works), mostly University of Southern California, University of California San Diego; most of the strings it gained were assigned to other institutions before (71% of gained works), mostly UCLA Medical Center, UCLA Health.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of California, Los Angeles at all, about **46% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **65% do name it** or one of its units.

Net, the works that really are University of California, Los Angeles's (counting its units) went up by about 6.2%.

**3,291 strings lost University of California, Los Angeles** ([removed.csv.gz](removed.csv.gz)), on 4,211 works; **52,149 strings gained it** ([added.csv.gz](added.csv.gz)), on 93,623 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To its parent institution | 13% |
| To other institutions (mostly University of Southern California, University of California San Diego, Los Angeles Medical Center) | 44% |
| To no institution | 42% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 28% |
| Up from one of its units or predecessors | 1% |
| Down from its parent institution | 0% |
| From other institutions (mostly UCLA Medical Center, UCLA Health, Harbor–UCLA Medical Center) | 71% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| [Dept. of Electr. & Comput. Eng., Univ. of California, La Jolla, CA, USA] | 74 | University of California San Diego |
| California States University Los Angeles | 64 | California State University Los Angeles |
| UCLA Stroke Cntr, Los Angeles, CA | 52 | no institution |
| University of Arizona University of California University of California Tucson , AZ 85721 Berkeley , CA 94720 Los Angeles , CA 90024 | 38 | University of Arizona |
| Los Angeles, California, 90068 U.S.A | 27 | no institution |
| [University of California, La Jolla, CA, USA] | 27 | no institution |
| David Geffen School of Medicine at Ucla | 24 | no institution |
| Los Angeles California 90068 U.S.A | 20 | no institution |
| Harbor-UCLA Med Cntr, Torrance, CA | 19 | Harbor–UCLA Medical Center |
| [University of California, La Jolla, CA] | 18 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| UCLA | 7,922 | UCLA Health |
| UCLA , | 1,099 | UCLA Health |
| UCLA School of Medicine | 653 | UCLA Health |
| UCLA School of Law | 506 | no institution |
| California University Los Angeles, CA, United States | 399 | no institution |
| (UCLA) | 387 | UCLA Health |
| Dep. Chem. Biochem., Univ. Calif., Los Angeles, CA 90095, USA | 372 | no institution |
| UCLA Mester | 365 | no institution |
| UCLA UCLA | 325 | UCLA Health |
| Dep. Chem. Biochem., Univ. Calif., Los Angeles, CA 90024, USA | 240 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
