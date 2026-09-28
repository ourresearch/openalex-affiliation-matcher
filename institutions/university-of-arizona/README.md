# University of Arizona

[OpenAlex I138006243](https://openalex.org/institutions/I138006243) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Arizona itself): 284,032 → 280,994 (−1.1%).
- **Counting its units and predecessors** (the `lineage` filter): 284,494 → 287,487 (+1.1%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (68% of lost works); most of the strings it gained had no institution before (60% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**7,862 strings lost University of Arizona** ([removed.csv.gz](removed.csv.gz)), on 14,060 works; **5,419 strings gained it** ([added.csv](added.csv)), on 8,328 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 68% |
| To other institutions (mostly University of Arizona Cancer Center, Arizona State University, St. Joseph's Hospital and Medical Center) | 28% |
| To no institution | 4% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 60% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly Banner - University Medical Center Tucson, Arizona Science Center, Planetary Science Institute) | 40% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| University of Arizona College of Medicine, Phoenix, AZ | 293 | University of Arizona College of Medicine- Phoenix |
| University of Arizona Cancer Center, Tucson, AZ | 224 | University of Arizona Cancer Center |
| University of Arizona Cancer Center, Tucson, AZ, USA | 214 | University of Arizona Cancer Center |
| University of Arizona Cancer Center, Tucson, AZ; | 174 | University of Arizona Cancer Center |
| University of Arizona College of Medicine, Phoenix, AZ, USA | 172 | University of Arizona College of Medicine- Phoenix |
| University of Arizona College of Medicine, Phoenix, AZ; | 117 | University of Arizona College of Medicine- Phoenix |
| University of Arizona College of Medicine-Phoenix, Phoenix, AZ, USA | 103 | University of Arizona College of Medicine- Phoenix |
| University of Arizona College of Medicine-Phoenix | 92 | University of Arizona College of Medicine- Phoenix |
| University of Arizona College of Medicine, Phoenix, Arizona | 87 | University of Arizona College of Medicine- Phoenix |
| University of Arizona College of Medicine - Phoenix | 78 | University of Arizona College of Medicine- Phoenix |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Arizona U | 303 | no institution |
| Steward Observatory, Tucson, AZ, United States | 166 | no institution |
| U. Arizona | 142 | no institution |
| Opt. Sci. Center, Arizona Univ., Tucson, AZ, USA | 120 | no institution |
| Arizona Respiratory Center | 101 | no institution |
| U Arizona | 71 | no institution |
| Steward Observatory, 933 North Cherry Avenue, Tucson, AZ 85721, USA | 64 | no institution |
| Steward Observatory, 933 North Cherry Avenue, Tucson, AZ 85721 | 63 | no institution |
| Department of Astronomy/Steward Observatory, 933 North Cherry Avenue, Tucson, AZ 85721-0065, USA | 55 | no institution |
| Steward Observatory (Department of Astronomy, 933 North Cherry Avenue, Tucson, Arizona 85721, USA - United States) | 49 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
