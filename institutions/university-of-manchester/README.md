# University of Manchester

[OpenAlex I28407311](https://openalex.org/institutions/I28407311) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Manchester itself): 336,466 → 351,309 (+4.4%).
- **Counting its units and predecessors** (the `lineage` filter): 343,652 → 357,335 (+4.0%).
- **Why:** most of the strings it lost now go to other institutions (53% of lost works), mostly Manchester Academic Health Science Centre, Manchester University NHS Foundation Trust; the largest share of the strings it gained had no institution before (49% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Manchester at all, about **85% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **91% do name it** or one of its units.

**3,060 strings lost University of Manchester** ([removed.csv](removed.csv)), on 4,977 works; **14,730 strings gained it** ([added.csv.gz](added.csv.gz)), on 27,029 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Manchester Academic Health Science Centre, Manchester University NHS Foundation Trust, Wythenshawe Hospital) | 53% |
| To no institution | 47% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 49% |
| Up from one of its units or predecessors | 13% |
| From other institutions (mostly Manchester University NHS Foundation Trust, Manchester University, Manchester Academic Health Science Centre) | 39% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| University of Greater Manchester | 189 | University of Greater Manchester |
| (Manchester School of Management, UMIST, Manchester, UK,) | 106 | no institution |
| Central Manchester University Hospitals | 56 | no institution |
| Manchester Centre for Genomic Medicine and NW Laboratory Genetics Hub, Manchester University Hospitals NHS Foundation Trust, Manchester, UK | 54 | Manchester University NHS Foundation Trust |
| Manchester, U.K | 51 | no institution |
| UMIST, UK#TAB# | 38 | no institution |
| Central Manchester University Hospitals, Manchester, UK | 35 | no institution |
| CRC Department of Medical Oncology, Christie Hospital Manchester, UK | 29 | The Christie Hospital |
| NIHR Manchester Biomedical Research Centre, Central Manchester University Hospitals NHS Foundation Trust, Manchester Academic Health Science | 25 | Manchester Academic Health Science Centre, NIHR Manchester Biomedical Research Centre |
| NIHR Manchester Biomedical Research Centre, Manchester University Hospitals NHS Foundation Trust, Manchester Academic Health Science Centre, | 25 | Manchester Academic Health Science Centre, NIHR Manchester Biomedical Research Centre |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Manchester Business School | 472 | no institution |
| Alliance Manchester Business School - Management Science and Marketing Division | 443 | no institution |
| Alliance Manchester Business School | 411 | Digital Research Alliance of Canada |
| Alliance Manchester Business School - Innovation Management and Policy Division | 399 | no institution |
| Alliance Manchester Business School - People, Management and Organisation Division | 325 | no institution |
| Manchester International Law Centre | 273 | NIHR Manchester Biomedical Research Centre |
| Manchester Business School, UK | 258 | Manchester School of Architecture |
| Alliance Manchester Business School - Accounting and Finance division | 239 | Manchester University |
| Manchester Business School, Manchester, UK | 223 | Manchester School of Architecture |
| Manchester U | 197 | Manchester University |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
