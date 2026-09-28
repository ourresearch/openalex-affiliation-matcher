# University of Southampton

[OpenAlex I43439940](https://openalex.org/institutions/I43439940) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Southampton itself): 193,640 → 197,437 (+2.0%).
- **Counting its units and predecessors** (the `lineage` filter): 195,632 → 198,693 (+1.6%).
- **Why:** most of the strings it lost now go to other institutions (54% of lost works), mostly University Hospital Southampton NHS Foundation Trust, Long Island University; the largest share of the strings it gained were assigned to other institutions before (47% of gained works), mostly University Hospital Southampton NHS Foundation Trust, National Oceanography Centre.

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**608 strings lost University of Southampton** ([removed.csv](removed.csv)), on 897 works; **4,662 strings gained it** ([added.csv](added.csv)), on 7,517 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 3% |
| To other institutions (mostly University Hospital Southampton NHS Foundation Trust, Long Island University, Southampton General Hospital) | 54% |
| To no institution | 42% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 35% |
| Up from one of its units or predecessors | 18% |
| From other institutions (mostly University Hospital Southampton NHS Foundation Trust, National Oceanography Centre, Southampton General Hospital) | 47% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Southampton University Hospitals NHS trust | 53 | University Hospital Southampton NHS Foundation Trust |
| Southampton University Hospitals NHS Trust, Southampton, UK.  | 33 | University Hospital Southampton NHS Foundation Trust |
| National Institute for Health Research, Evaluation, Trials and Studies Coordinating Centre, Alpha House, University of Southampton Science P | 19 | National Institute for Health and Care Research, NIHR Evaluation Trials and Studies Coordinating Centre |
| Southampton U.K | 19 | no institution |
| Southampton, U.K | 19 | no institution |
| Southampton Street, Strand | 16 | no institution |
| MRC Lifecourse Epidemiology UnitUniversity of SouthamptonSouthamptonUK | 14 | MRC Lifecourse Epidemiology Unit |
| Southampton Photonics, Inc.orporated, Southampton, UK | 13 | no institution |
| @Southampton-RSG | 12 | no institution |
| Southampton PA, USA | 9 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| University Hospital Southampton, Southampton, UK | 305 | University Hospital Southampton NHS Foundation Trust |
| University Hospital Southampton, Southampton, United Kingdom | 238 | University Hospital Southampton NHS Foundation Trust |
| Department of Urology, University Hospital Southampton NHS Trust, Southampton, UK | 134 | University Hospital Southampton NHS Foundation Trust |
| Department of Urology, University Hospital Southampton, Southampton, UK | 101 | University Hospital Southampton NHS Foundation Trust |
| Department of Clinical Law, University Hospital Southampton | 47 | University Hospital Southampton NHS Foundation Trust |
| Southampton Business School, Southampton, UK | 44 | no institution |
| Southampton National Institute for Health Research Biomedical Research Centre, University Hospital Southampton NHS Foundation Trust, Southam | 37 | University Hospital Southampton NHS Foundation Trust, National Institute for Health and Care Research |
| Institute of Sound and Vibration Research | 35 | no institution |
| NIHR Journals Library, National Institute for Health Research, Evaluation, Trials and Studies Coordinating Centre, Alpha House, University o | 30 | NIHR Evaluation Trials and Studies Coordinating Centre |
| Ocean and Earth Science [Southampton] (European Way, Southampton SO 14 3ZH - United Kingdom) | 29 | National Oceanography Centre |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
