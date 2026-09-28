# Korea Institute of Science & Technology Information

[OpenAlex I878022262](https://openalex.org/institutions/I878022262) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Korea Institute of Science & Technology Information itself): 6,933 → 5,357 (−22.7%).
- **Counting its units and predecessors** (the `lineage` filter): 6,935 → 5,365 (−22.6%).
- **Why:** most of the strings it lost now go to other institutions (79% of lost works), mostly Korea Institute of Science and Technology, Korea Advanced Institute of Science and Technology; most of the strings it gained had no institution before (62% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Korea Institute of Science & Technology Information at all, about **90% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **60% do name it** or one of its units.

**1,043 strings lost Korea Institute of Science & Technology Information** ([removed.csv](removed.csv)), on 1,876 works; **43 strings gained it** ([added.csv](added.csv)), on 61 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Korea Institute of Science and Technology, Korea Advanced Institute of Science and Technology, Korea Research Institute of Chemical Technology) | 79% |
| To no institution | 20% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 62% |
| From other institutions (mostly Korea Institute of Science and Technology, KISTI Research Division for Data Analysis, Korean Association Of Science and Technology Studies) | 38% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Korea Institute of Information and Communication Engineering | 75 | no institution |
| Korea Institute of Science and Technology , , , | 53 | Korea Institute of Science and Technology |
| Department of Information and Communications Engineering, Korea Advanced Institute of Science and Technology, Daejeon, South Korea | 33 | Korea Advanced Institute of Science and Technology |
| Center for Quantum Information, Korea Institute of Science and Technology (KIST), Seoul, 02792, Republic of Korea | 28 | Korea Institute of Science and Technology |
| Center for Quantum Information, Korea Institute of Science and Technology (KIST), Seoul 02792, Republic of Korea | 24 | Korea Institute of Science and Technology |
| Bio-Org. Sci. Div., Korea Res. Inst. Chem. Technol., Daejeon 305-600, S. Korea | 21 | Korea Research Institute of Chemical Technology |
| Department of Information and Communication Engineering, Korea Advanced Institute of Science and Technology, Seoul, South Korea | 18 | Korea Advanced Institute of Science and Technology |
| [Korea Adv. Inst. of Sci. & Technol., Daejeon, South Korea] | 18 | Korea Advanced Institute of Science and Technology |
| Center for Quantum Information, Korea Institute of Science and Technology, Seoul 02792, Republic of Korea | 13 | Korea Institute of Science and Technology |
| Department of Information and Communications Engineering, Korea Advanced Institute of Science and Technology, Daejeon, Korea | 13 | Korea Advanced Institute of Science and Technology |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Intelligent System Control Research Center, KIST, Korea | 5 | no institution |
| Intelligent System Control Research Center, KIST, South Korea | 5 | no institution |
| Division of Electronics and Information Technology, KIST, 39-1 Haweolgog-dong, Seongbuk-gu, Seoul 136-791, Korea | 3 | no institution |
| ‡Disaster Management HPC Technology Research Center, Korea Institute of Science and Technology Infor | 3 | Korea Institute of Science and Technology |
| Dept. of Enterprises Innovation Strategy, KISTI, Seoul, Republic of Korea | 2 | no institution |
| Division of Electronics & Information Technology, KIST, South Korea | 2 | no institution |
| KISTI , 66 Hoegiro , Dongdaemun-gu , Seoul , 130-741 , Korea | 2 | Korean Institute of Architects |
| Korean Institute of Science and Technology Information, Seoul, Korea | 2 | Korean Association Of Science and Technology Studies |
| [Intelligent System Control Research Center, KIST, South Korea] | 2 | no institution |
| †Disaster Management HPC Technology Research Center, Korea Institute of Science and Technology Infor | 2 | Korea Institute of Science and Technology |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
