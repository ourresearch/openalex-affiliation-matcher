# Swedish Research Council

[OpenAlex I2802499594](https://openalex.org/institutions/I2802499594) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Swedish Research Council itself): 1,319 → 288 (−78.2%).
- **Counting its units and predecessors** (the `lineage` filter): 7,484 → 6,412 (−14.3%).
- **Why:** most of the strings it lost now have no institution (53% of lost works); most of the strings it gained had no institution before (75% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Swedish Research Council at all, about **58% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **84% do name it** or one of its units.

**884 strings lost Swedish Research Council** ([removed.csv](removed.csv)), on 1,213 works; **12 strings gained it** ([added.csv](added.csv)), on 12 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly Karolinska University Hospital, Karolinska Institutet, Uppsala University) | 47% |
| To no institution | 53% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 75% |
| From other institutions (mostly European High Performance Computing Joint Undertaking, Region Blekinge, Swedish Agency for Economic and Regional Growth) | 25% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| The Swedish Council for Information on Alcohol and Other Drugs (CAN), Stockholm, Sweden | 26 | no institution |
| Reproductive Endocrinology Research Unit, Swedish Medical Research Council, Karolinska sjukhuset, Stockholm | 16 | Karolinska University Hospital |
| The Swedish Council for Information on Alcohol and Other Drugs, Stockholm, Sweden | 14 | no institution |
| Swedish Council for Information on Alcohol and Other Drugs (CAN), Stockholm, Sweden | 13 | no institution |
| Swedish Medical Research Council, Reproductive Endocrinology Research Unit, Karolinska sjukhuset, 104 01 Stockholm 60 | 11 | Karolinska University Hospital |
| Swedish Medical Research Council, Reproductive Endocrinology Research Unit, Karolinska sjukhuset, Stockholm | 11 | Karolinska University Hospital |
| Reproductive Endocrinology Research Unit, Swedish Medical Research Council, Karolinska sjukhuset, Stockholm, Sweden | 10 | no institution |
| Department of Toxicology Swedish Medical Research Council Karolinska Institutet, Stockholm, Sweden | 9 | Karolinska Institutet |
| Swedish Medical Research Council, Reproductive Endocrinology Research Unit and Hormone Laboratory, Department of Women's Diseases, Karolinsk | 9 | Karolinska University Hospital |
| Department of Toxicology, Swedish Medical Research Council, Karolinska Institutet, Stockholm, Sweden | 8 | Karolinska Institutet |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| 1Association VR‐Euratom, Sweden | 1 | no institution |
| Andreas DIEDRICH PhD is an Associate Professor in Business Administration at the Department for Business Administration, School of Business  | 1 | no institution |
| Association VR-Euratom, Sweden | 1 | no institution |
| Hanifeh Khayyeri is a part of a national commission of  inquiry in Sweden that has been tasked by the Swedish Government to  propose approac | 1 | European High Performance Computing Joint Undertaking |
| I'm in VR | 1 | no institution |
| The research reported and planned received financial support from NUTEK (Tillväxtverket, Swedish Agency for Economic and Regional Growth) an | 1 | Region Blekinge, Swedish Agency for Economic and Regional Growth |
| This work was supported by the Swedish Research Council through the project "Share or Spare? Explaining the Nature and Determinants of Clima | 1 | no institution |
| This work was supported by the Swedish Research Council through the project “Share or Spare? Explaining the Nature and Determinants of Clima | 1 | no institution |
| We thank the editors and three anonymous reviewers for their insightful comments. We received constructive feedback from Stockholm Universit | 1 | Conference Board |
| We thank three anonymous reviewers for their constructive comments on earlier versions of the manuscript. We are also grateful for comments  | 1 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
