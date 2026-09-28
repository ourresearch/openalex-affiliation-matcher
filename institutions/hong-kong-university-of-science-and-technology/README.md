# Hong Kong University of Science and Technology

[OpenAlex I200769079](https://openalex.org/institutions/I200769079) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Hong Kong University of Science and Technology itself): 98,597 → 97,833 (−0.8%).
- **Counting its units and predecessors** (the `lineage` filter): 105,690 → 101,055 (−4.4%).
- **Why:** most of the strings it lost now go to other institutions (88% of lost works), mostly The Hong Kong University of Science and Technology (Guangzhou), South China University of Technology; most of the strings it gained were assigned to other institutions before (56% of gained works), mostly Peking University Shenzhen Hospital, University of Hong Kong.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Hong Kong University of Science and Technology at all, about **85% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **52% do name it** or one of its units.

**2,021 strings lost Hong Kong University of Science and Technology** ([removed.csv](removed.csv)), on 3,693 works; **2,331 strings gained it** ([added.csv](added.csv)), on 3,636 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 3% |
| To other institutions (mostly The Hong Kong University of Science and Technology (Guangzhou), South China University of Technology, State Key Laboratory of Luminescent Materials and Devices) | 88% |
| To no institution | 9% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 8% |
| Up from one of its units or predecessors | 36% |
| From other institutions (mostly Peking University Shenzhen Hospital, University of Hong Kong, University of Hong Kong - Shenzhen Hospital) | 56% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| The Hong Kong University of Science and Technology (Guangzhou ) | 111 | The Hong Kong University of Science and Technology (Guangzhou) |
| Department of Chemistry, Hong Kong University of Science, Hong Kong, Hongkong | 65 | no institution |
| Center for Aggregation-Induced Emission, SCUT-HKUST Joint Research Institute, State Key Laboratory of Luminescent Materials and Devices, Sou | 48 | South China University of Technology, State Key Laboratory of Luminescent Materials and Devices |
| Hong Kong University of Science and Technology (Guangzhou ) | 35 | The Hong Kong University of Science and Technology (Guangzhou) |
| Center for Aggregation-Induced Emission, SCUT-HKUST Joint Research Institute, State Key Laboratory of Luminescent Materials and Devices, Sou | 30 | South China University of Technology, State Key Laboratory of Luminescent Materials and Devices |
| School of Science and Technology, Hong Kong Metropolitan University,Hong Kong,China | 23 | Hong Kong Metropolitan University |
| Guangzhou Key Laboratory of Electrochemical Energy Storage Technologies Fok Ying Tung Research Institute The Hong Kong University of Science | 20 | Guangzhou HKUST Fok Ying Tung Research Institute, The Hong Kong University of Science and Technology (Guangzhou) |
| The Hong Kong University of Science and Technology (Guangzhou ), | 19 | The Hong Kong University of Science and Technology (Guangzhou) |
| Center for Aggregation-Induced Emission, SCUT-HKUST Joint Research Institute, State Key Laboratory of Luminescent Materials and Devices, Sou | 15 | South China University of Technology, State Key Laboratory of Luminescent Materials and Devices |
| Hong Kong University of Science and Technology (Guangzhou) , | 15 | The Hong Kong University of Science and Technology (Guangzhou) |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| HKUST Shenzhen-Hong Kong Collaborative Innovation Research Institute, Futian, Shenzhen, China | 300 | HKUST Shenzhen Research Institute |
| HKUST-Shenzhen Research Institute | 43 | HKUST Shenzhen Research Institute |
| HKUST Shenzhen-Hong Kong Collaborative Innovation Research Institute | 40 | HKUST Shenzhen Research Institute |
| Hong Kong UST | 31 | no institution |
| HKUST Shenzhen-Hong Kong Collaborative Innovation Research Institute, Futian, Shenzhen | 25 | HKUST Shenzhen Research Institute |
| HKUST-gz | 24 | HKUST Shenzhen Research Institute, The Hong Kong University of Science and Technology (Guangzhou) |
| Department of Computer Science and Engineering , HKUST | 21 | National University of Sciences and Technology |
| PKU-HKUST Shenzhen-Hong Kong Institution, PKU-HKUST, Shen Zhen-Hong Kong Institution, Shenzh, Shenzhen, Guangdong 518057, China | 21 | HKUST Shenzhen Research Institute |
| SZU-HKUST Joint PhD Program in Marine Environmental Science, Shenzhen University, Shenzhen, China | 21 | Shenzhen University |
| HKUST-CAS Sanya Joint Laboratory of Marine Science Research, Chinese Academy of Sciences, Sanya, China | 20 | Institute of Deep-Sea Science and Engineering, Chinese Academy of Sciences |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
