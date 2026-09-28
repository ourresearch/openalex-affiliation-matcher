# Virginia Tech

[OpenAlex I859038795](https://openalex.org/institutions/I859038795) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Virginia Tech itself): 178,105 → 180,790 (+1.5%).
- **Counting its units and predecessors** (the `lineage` filter): 184,311 → 185,183 (+0.5%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (59% of lost works); most of the strings it gained moved up from one of its units (55% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**960 strings lost Virginia Tech** ([removed.csv](removed.csv)), on 2,245 works; **7,155 strings gained it** ([added.csv.gz](added.csv.gz)), on 9,731 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 59% |
| To other institutions (mostly Thapar Institute of Engineering & Technology, West Virginia University Institute of Technology, University of Virginia) | 8% |
| To no institution | 34% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 28% |
| Up from one of its units or predecessors | 55% |
| From other institutions (mostly University of Virginia, Molecular Sciences Software Institute, Biomedical Research Institute) | 17% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Blacksburg , Virginia | 168 | no institution |
| Virginia Tech Transportation Institute | 129 | Virginia Tech Transportation Institute |
| (Virginia Tech Transportation Institute) | 114 | Virginia Tech Transportation Institute |
| Virginia Technology, USA | 109 | no institution |
| Blacksburg, Virginia | 58 | no institution |
| Virginia Tech Transportation Institute, Blacksburg, VA | 34 | Virginia Tech Transportation Institute |
| Virginia Tech Transportation Institute, Blacksburg, VA, USA | 34 | Virginia Tech Transportation Institute |
| Virginia Tech. Transportation Institute | 34 | Virginia Tech Transportation Institute |
| Virginia Tech Transportation Institute, 3500 Transportation Research Plaza, Blacksburg, VA 24061, USA | 31 | Virginia Tech Transportation Institute |
| Blacksburg , VA | 23 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| @VirginiaTech @MolSSI | 222 | Molecular Sciences Software Institute |
| Virginia Polytech. Inst. and State Univ., Blacksburg, VA, USA | 179 | University of Virginia |
| Polytechnic Institute and State University | 155 | no institution |
| Virginia College of Technology | 47 | Virginia College |
| @VirginiaTech - @bi-sdal - GBCB | 36 | no institution |
| Virginia Polytech. Inst. & State Univ., Blacksburg, VA | 34 | University of Virginia |
| Virginia Tech/MolSSI | 30 | no institution |
| Virgina Tech | 28 | Virgin Care |
| PhD Student @VirginiaTech | 26 | no institution |
| School of Biomedical Engineering and Sciences, Virginia Tech-Wake Forest University, Blacksburg, VA, USA | 25 | Virginia Tech - Wake Forest University School of Biomedical Engineering & Sciences |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
