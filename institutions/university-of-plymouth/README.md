# University of Plymouth

[OpenAlex I897542642](https://openalex.org/institutions/I897542642) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Plymouth itself): 39,689 → 42,087 (+6.0%).
- **Counting its units and predecessors** (the `lineage` filter): 39,689 → 42,087 (+6.0%).
- **Why:** most of the strings it lost now go to other institutions (86% of lost works), mostly Peninsula College of Medicine and Dentistry, University of Exeter; most of the strings it gained were assigned to other institutions before (59% of gained works), mostly Peninsula College of Medicine and Dentistry, Plymouth Marine Laboratory.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Plymouth at all, about **41% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **94% do name it** or one of its units.

**458 strings lost University of Plymouth** ([removed.csv](removed.csv)), on 775 works; **2,776 strings gained it** ([added.csv](added.csv)), on 4,320 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly Peninsula College of Medicine and Dentistry, University of Exeter, University Hospitals Plymouth NHS Trust) | 86% |
| To no institution | 14% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 41% |
| From other institutions (mostly Peninsula College of Medicine and Dentistry, Plymouth Marine Laboratory, Plymouth Marjon University) | 59% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Peninsula College of Medicine and Dentistry | 84 | Peninsula College of Medicine and Dentistry |
| Peninsula College of Medicine and Dentistry, Plymouth, UK | 44 | Peninsula College of Medicine and Dentistry |
| Peninsula College of Medicine and Dentistry, Plymouth, United Kingdom | 19 | Peninsula College of Medicine and Dentistry |
| Peninsula College of Medicine and Dentistry, Universities of Plymouth and Exeter, PL4 8AA, Plymouth, United Kingdom | 17 | Peninsula College of Medicine and Dentistry |
| Peninsula College of Medicine and Dentistry, Universities of Plymouth and Exeter, Plymouth, United Kingdom | 17 | Peninsula College of Medicine and Dentistry |
| Peninsula College of Medicine and Dentistry, UK | 11 | Peninsula College of Medicine and Dentistry |
| Peninsula College of Medicine and Dentistry, Plymouth | 10 | Peninsula College of Medicine and Dentistry |
| Clinical Neurology Research Group, Peninsula College of Medicine and Dentistry, Plymouth, UK | 9 | Peninsula College of Medicine and Dentistry |
| Plymouth U.K | 7 | no institution |
| Plymouth, U.K | 7 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Plymouth#N#        University | 305 | no institution |
| Plymouth University Peninsula Schools of Medicine and Dentistry, Plymouth, UK | 91 | Peninsula College of Medicine and Dentistry |
| Peninsula Dental School, Plymouth, UK | 58 | Peninsula College of Medicine and Dentistry |
| Plymouth University Peninsula Schools of Medicine and Dentistry | 46 | Peninsula College of Medicine and Dentistry |
| Peninsula Dental School, Plymouth, United Kingdom | 28 | Peninsula College of Medicine and Dentistry |
| Peninsula Medical School, Universities of Exeter and Plymouth | 28 | Peninsula College of Medicine and Dentistry |
| Plymouth University Peninsula Schools of Medicine and Dentistry, Plymouth, United Kingdom | 25 | Peninsula College of Medicine and Dentistry |
| Plymouth University, Peninsula Schools of Medicine and Dentistry, Plymouth, UK | 25 | no institution |
| Peninsula Schools of Medicine and Dentistry, Plymouth University, Plymouth, UK | 24 | no institution |
| Plymouth University Peninsula School of Medicine and Dentistry, Plymouth, UK | 18 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
