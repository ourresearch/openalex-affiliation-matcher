# University Medical Center Groningen

[OpenAlex I1334415907](https://openalex.org/institutions/I1334415907) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University Medical Center Groningen itself): 86,242 → 95,310 (+10.5%).
- **Counting its units and predecessors** (the `lineage` filter): 87,094 → 95,651 (+9.8%).
- **Why:** most of the strings it lost now go to other institutions (91% of lost works), mostly University of Groningen, Amsterdam UMC Location Vrije Universiteit Amsterdam; most of the strings it gained were assigned to other institutions before (59% of gained works), mostly University of Groningen, European Society for Organ Transplantation.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University Medical Center Groningen at all, about **74% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **100% do name it** or one of its units.

**1,862 strings lost University Medical Center Groningen** ([removed.csv](removed.csv)), on 2,561 works; **11,539 strings gained it** ([added.csv.gz](added.csv.gz)), on 20,260 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly University of Groningen, Amsterdam UMC Location Vrije Universiteit Amsterdam, University Medical Center Utrecht) | 91% |
| To no institution | 9% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 39% |
| Up from one of its units or predecessors | 2% |
| From other institutions (mostly University of Groningen, European Society for Organ Transplantation, Kidney Centre) | 59% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Faculty of Medical Sciences, University of Groningen, Groningen, The Netherlands | 55 | University of Groningen |
| Department of Medical Physiology, University of Groningen, Groningen, The Netherlands | 46 | University of Groningen |
| Department of Medical Physiology, University of Groningen, Groningen, the Netherlands | 28 | University of Groningen |
| Faculty of Medical Sciences, University of Groningen, Groningen, the Netherlands | 22 | University of Groningen |
| Faculty of Medical Sciences, University of Groningen, Groningen, Netherlands | 21 | University of Groningen |
| Department of Cardiology, University of Groningen , Groningen , | 16 | University of Groningen |
| Department of Medical Microbiology, University of Groningen, The Netherlands | 14 | University of Groningen |
| Department of Medical Microbiology, University of Groningen, Groningen, The Netherlands | 11 | University of Groningen |
| University of Groningen - Department of Medical Microbiology and Infection Prevention | 11 | University of Groningen |
| University of Groningen - Department of Medical Microbiology and Infection Prevention, Groningen, Netherlands | 11 | University of Groningen |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Groningen Institute for Organ Transplantation (GIOT) | 762 | European Society for Organ Transplantation |
| Groningen Kidney Center (GKC) | 744 | Kidney Centre |
| Department of Internal Medicine, University Hospital Groningen, The Netherlands | 124 | University of Groningen |
| Department of Internal Medicine, University Hospital, Groningen, The Netherlands | 124 | University of Groningen |
| University Hospital Groningen | 96 | no institution |
| University Hospital, Groningen, The Netherlands | 94 | no institution |
| Department of Cardiology, University Hospital Groningen, The Netherlands | 90 | no institution |
| Department of Oral and Maxillofacial Surgery, University Hospital Groningen, The Netherlands | 85 | no institution |
| Department of Surgery, University Hospital Groningen, The Netherlands | 81 | no institution |
| Dept. of Neurology, University Hospital, Groningen, the Netherlands | 71 | University of Groningen |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
