# University of California San Diego

[OpenAlex I36258959](https://openalex.org/institutions/I36258959) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of California San Diego itself): 383,332 → 424,030 (+10.6%).
- **Counting its units and predecessors** (the `lineage` filter): 406,680 → 439,658 (+8.1%).
- **Why:** the largest share of the strings it lost now have no institution (44% of lost works); most of the strings it gained were assigned to other institutions before (71% of gained works), mostly Universidad Católica Santo Domingo, University of California San Diego Medical Center.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of California San Diego at all, about **50% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **91% do name it** or one of its units.

Net, the works that really are University of California San Diego's (counting its units) went up by about 8.3%.

**4,830 strings lost University of California San Diego** ([removed.csv](removed.csv)), on 9,181 works; **23,404 strings gained it** ([added.csv.gz](added.csv.gz)), on 63,080 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To its parent institution | 28% |
| To other institutions (mostly Moores Cancer Center, University of California San Diego Medical Center, University of San Diego) | 28% |
| To no institution | 44% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 13% |
| Up from one of its units or predecessors | 16% |
| Down from its parent institution | 1% |
| From other institutions (mostly Universidad Católica Santo Domingo, University of California San Diego Medical Center, Moores Cancer Center) | 71% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| San Diego, CA, USA | 761 | no institution |
| UC San Diego Moores Cancer Center, La Jolla, CA | 190 | Moores Cancer Center |
| California, University La Jolla CA, United States | 174 | no institution |
| University of California, La Jolla, CA, USA | 150 | no institution |
| San Diego, CA USA | 146 | no institution |
| University of California San Diego Moores Cancer Center, La Jolla, CA; | 85 | Moores Cancer Center |
| California, University, La Jolla, United States | 81 | no institution |
| University of California San Diego, Moores Cancer Center, La Jolla, CA; | 72 | Moores Cancer Center |
| University of California, La Jolla, California | 67 | no institution |
| UNIVERSITY OF CALIFORNIA (LA JOLLA) | 59 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| UCSD | 28,763 | Universidad Católica Santo Domingo |
| (UCSD) | 266 | Universidad Católica Santo Domingo |
| California Univ. San Diego, CA, United States | 248 | no institution |
| Scripps Institution of Oceanography, University Of California - San Diego, La Jolla, California | 225 | Scripps Institution of Oceanography |
| UCSD; | 218 | Universidad Católica Santo Domingo |
| UCSD Female Reproductive Tissue Mapping Center | 202 | no institution |
| UCSD - Dept. of Pediatrics | 154 | no institution |
| Univ of California San Diego, San Diego, CA | 108 | no institution |
| Scripps Institution of Oceanography, UC San Diego | 98 | Scripps Institution of Oceanography |
| UCSD School of Medicine | 94 | Universidad Católica Santo Domingo |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
