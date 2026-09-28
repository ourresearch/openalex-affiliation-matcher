# University of Minnesota

[OpenAlex I130238516](https://openalex.org/institutions/I130238516) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of Minnesota itself): 428,170 → 441,842 (+3.2%).
- **Counting its units and predecessors** (the `lineage` filter): 428,936 → 442,799 (+3.2%).
- **Why:** most of the strings it lost now go to other institutions (53% of lost works), mostly University of Minnesota, Duluth, China Agricultural University; most of the strings it gained had no institution before (56% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Minnesota at all, about **65% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **90% do name it** or one of its units.

Net, the works that really are University of Minnesota's (counting its units) went up by about 3.2%.

**2,329 strings lost University of Minnesota** ([removed.csv](removed.csv)), on 3,607 works; **10,484 strings gained it** ([added.csv.gz](added.csv.gz)), on 24,525 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 25% |
| To its parent institution | 0% |
| To other institutions (mostly University of Minnesota, Duluth, China Agricultural University, University of Minnesota Rochester) | 53% |
| To no institution | 21% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 56% |
| Up from one of its units or predecessors | 2% |
| Down from its parent institution | 15% |
| From other institutions (mostly University of Minnesota Medical Center, University of Minnesota Morris, University of Minnesota, Duluth) | 27% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| University of Minnesota Masonic Cancer Center, Minneapolis, MN | 90 | Masonic Cancer Center |
| University of Minnesota – Morris | 68 | University of Minnesota Morris |
| University of Minnesota, Duluth, USA#TAB# | 62 | University of Minnesota, Duluth |
| University of Minnesota Cancer Center, Minneapolis, MN, USA | 49 | Masonic Cancer Center |
| University of Minnesota Masonic Cancer Center, Minneapolis, MN; | 37 | Masonic Cancer Center |
| University of Minnesota Masonic Cancer Center, Minneapolis, MN, USA | 31 | Masonic Cancer Center |
| Islamic University of Minnesota | 26 | Islamic University of Minnesota |
| State Key Laboratory of Plant Physiology and Biochemistry,  College of Biological Sciences,  China Agricultural University,  Beijing 100193, | 26 | China Agricultural University, State Key Laboratory of Plant Physiology and Biochemistry |
| University of Minnesota Press | 25 | no institution |
| State Key Laboratory of Agrobiotechnology, College of Biological Sciences,  China Agricultural University, Beijing, China | 24 | China Agricultural University |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Chemistry (Twin Cities) | 1,181 | no institution |
| Physics and Astronomy (Twin Cities) | 976 | no institution |
| Univ of Minnesota, Minneapolis, MN | 810 | no institution |
| Minnesota U | 702 | University of Minnesota System |
| Psychology (Twin Cities) | 578 | no institution |
| Dep. Chem., Univ. Minn., Minneapolis, MN 55455, USA | 487 | no institution |
| Art History (Twin Cities) | 453 | no institution |
| U. of Minnesota | 440 | University of Minnesota System |
| Social Work (Twin Cities) | 415 | no institution |
| Sociology (Twin Cities) | 397 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
