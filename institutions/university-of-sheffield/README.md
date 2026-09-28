# University of Sheffield

[OpenAlex I91136226](https://openalex.org/institutions/I91136226) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of Sheffield itself): 199,370 → 202,521 (+1.6%).
- **Counting its units and predecessors** (the `lineage` filter): 199,379 → 202,531 (+1.6%).
- **Why:** most of the strings it lost now have no institution (76% of lost works); most of the strings it gained had no institution before (73% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**777 strings lost University of Sheffield** ([removed.csv](removed.csv)), on 1,292 works; **4,089 strings gained it** ([added.csv](added.csv)), on 6,208 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Yale University, Royal Hallamshire Hospital, Sheffield Teaching Hospitals NHS Foundation Trust) | 24% |
| To no institution | 76% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 73% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly Huddersfield Royal Infirmary, Medical Research Council, Royal Hallamshire Hospital) | 27% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Sheffield - | 320 | no institution |
| Sheffield/UK | 32 | no institution |
| Sheffield Biological Laboratory, Yale University | 14 | Yale University |
| Sheffield Centre for Health and Related Research | 9 | no institution |
| The Earl of Sheffield | 9 | no institution |
| Sheffield Laboratory of Bacteriology, Yale University | 7 | Yale University |
| From the Laboratory of Applied Physiology, Sheffield Scientific School, Yale University | 6 | Yale University |
| University of Leeds, Sheffield, United Kingdom | 6 | University of Leeds |
| Central Sheffield University Hospitals NHS Trust | 5 | no institution |
| Department of Microbiology, The University, Western Bank, Sheffield S10 2TN | 5 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| SHEFFIELD | 166 | no institution |
| The University, Sheffield | 103 | no institution |
| Univ. Sheffield, UK | 82 | no institution |
| U. of Sheffield | 72 | no institution |
| The University Sheffield | 61 | no institution |
| The UniversitySheffield | 43 | no institution |
| Sheffield Business School | 40 | no institution |
| Department of Pure Mathematics, The University, Sheffield S3 7RH | 31 | no institution |
| a  The University ,  Sheffield | 28 | no institution |
| The University, Sheffield, | 24 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
