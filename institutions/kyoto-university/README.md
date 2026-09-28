# Kyoto University

[OpenAlex I22299242](https://openalex.org/institutions/I22299242) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Kyoto University itself): 376,696 → 423,837 (+12.5%).
- **Counting its units and predecessors** (the `lineage` filter): 384,064 → 439,273 (+14.4%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (86% of lost works); most of the strings it gained had no institution before (80% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Kyoto University at all, about **65% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **96% do name it** or one of its units.

**4,076 strings lost Kyoto University** ([removed.csv](removed.csv)), on 23,510 works; **16,813 strings gained it** ([added.csv.gz](added.csv.gz)), on 69,720 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 86% |
| To other institutions (mostly Kyoto University Hospital, Kyoto Prefectural University of Medicine, Kyoto Prefectural University) | 5% |
| To no institution | 9% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 80% |
| Up from one of its units or predecessors | 10% |
| From other institutions (mostly Kyoto University Hospital, Kyoto Architecture University, Kyoto Pharmaceutical University) | 10% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Institute for Chemical Research, Kyoto University | 1,650 | Kyoto University Institute for Chemical Research |
| Disaster Prevention Research Institute, Kyoto University | 1,243 | Disaster Prevention Research Institute, Kyoto University |
| Institute for Chemical Research, Kyoto University Uji, Kyoto 611 (Japan) | 606 | Kyoto University Institute for Chemical Research |
| Inst. Chem. Res., Kyoto Univ., Uji, Kyoto 611, Japan | 471 | Kyoto University Institute for Chemical Research |
| INSTITUTE FOR CHEMICAL RESEARCH KYOTO UNIVERSITY | 442 | Kyoto University Institute for Chemical Research |
| Institute for Chemical Research, Kyoto University Uji, Kyoto-fu, 611, Japan | 433 | Kyoto University Institute for Chemical Research |
| Institute of Advanced Energy, Kyoto University | 423 | Institute of Advanced Energy, Kyoto University |
| Research Institute for Mathematical Sciences, Kyoto University | 308 | Research Institute for Mathematical Sciences, Kyoto University |
| Research Institute for Mathematical Sciences, Kyoto University#TAB# | 258 | Research Institute for Mathematical Sciences, Kyoto University |
| Institute for Chemical Research, Kyoto University, Uji, Kyoto, 611-0011, Japan | 248 | Kyoto University Institute for Chemical Research |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| 京都大学 | 4,767 | no institution |
| 京都大学工学部 | 3,094 | no institution |
| 京都大学防災研究所 | 1,533 | Disaster Prevention Research Institute, Kyoto University |
| 京都大学大学院 | 1,316 | no institution |
| 京都大学大学院工学研究科 | 1,152 | no institution |
| 京都大学農学部 | 1,078 | no institution |
| Kyoto Univ | 1,009 | no institution |
| Kyoto U | 964 | no institution |
| 京都大学大学院農学研究科 | 825 | no institution |
| Pharmaceutical Institute, Medical Faculty, University of Kyoto | 609 | Kyoto Pharmaceutical University |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
