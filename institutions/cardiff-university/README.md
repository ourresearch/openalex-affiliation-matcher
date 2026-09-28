# Cardiff University

[OpenAlex I79510175](https://openalex.org/institutions/I79510175) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Cardiff University itself): 134,377 → 140,467 (+4.5%).
- **Counting its units and predecessors** (the `lineage` filter): 134,389 → 140,512 (+4.6%).
- **Why:** most of the strings it lost now have no institution (70% of lost works); most of the strings it gained were assigned to other institutions before (54% of gained works), mostly University of Wales, Welsh Government.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Cardiff University at all, about **63% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **98% do name it** or one of its units.

Net, the works that really are Cardiff University's (counting its units) went up by about 6.7%.

**3,660 strings lost Cardiff University** ([removed.csv](removed.csv)), on 6,727 works; **6,921 strings gained it** ([added.csv](added.csv)), on 14,799 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly University of Wales, University Hospital of Wales, Cardiff Metropolitan University) | 30% |
| To no institution | 70% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 46% |
| From other institutions (mostly University of Wales, Welsh Government, Institute of Catalysis and Petrochemistry) | 54% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Cardiff | 1,143 | no institution |
| Cardiff, UK | 320 | no institution |
| Cardiff CF10 3AT | 83 | no institution |
| Cardiff (UK) | 73 | no institution |
| CARDIFF | 72 | no institution |
| Cardiff/UK | 53 | no institution |
| , Cardiff | 46 | no institution |
| Welsh National School of Medicine Cardiff | 36 | no institution |
| Department of Applied Mathematics & Astronomy, University College, PO Box 78, Cardiff CF1 1XL | 34 | University College London |
| Cardiff Business School, University of Wales, Cardiff, UK | 33 | University of Wales |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| University College, Cardiff | 923 | no institution |
| Cardiff Business School | 489 | no institution |
| University of Wales, Cardiff, UK | 264 | University of Wales |
| University College Cardiff | 254 | no institution |
| Senior Lecturer, Department of Child Health, Welsh National School of Medicine, Cardiff, Honorary Consultant Pædiatrician, United Cardiff Ho | 164 | no institution |
| Cardiff Catalysis Institute | 131 | Institute of Catalysis and Petrochemistry |
| Department of Haematology, University of Wales College of Medicine, Cardiff, UK | 118 | University of Wales |
| University College , Cardiff | 99 | no institution |
| School of Chemistry and Applied Chemistry, University of Wales Cardiff, Wales, UK | 94 | University of Wales |
| Cardiff Gravitational Waves Physics | 93 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
