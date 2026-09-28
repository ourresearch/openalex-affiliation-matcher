# Virginia Commonwealth University

[OpenAlex I184840846](https://openalex.org/institutions/I184840846) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Virginia Commonwealth University itself): 105,875 → 109,076 (+3.0%).
- **Counting its units and predecessors** (the `lineage` filter): 106,320 → 109,723 (+3.2%).
- **Why:** the largest share of the strings it lost now go to other institutions (43% of lost works), mostly Virginia Commonwealth University Medical Center, University of Virginia; most of the strings it gained were assigned to other institutions before (83% of gained works), mostly Virginia Commonwealth University Medical Center, Children's Hospital of Richmond at VCU.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Virginia Commonwealth University at all, about **60% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **53% do name it** or one of its units.

**994 strings lost Virginia Commonwealth University** ([removed.csv](removed.csv)), on 1,359 works; **3,740 strings gained it** ([added.csv](added.csv)), on 6,570 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 37% |
| To other institutions (mostly Virginia Commonwealth University Medical Center, University of Virginia, Boston University) | 43% |
| To no institution | 19% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 12% |
| Up from one of its units or predecessors | 4% |
| From other institutions (mostly Virginia Commonwealth University Medical Center, Children's Hospital of Richmond at VCU, Hunter Holmes McGuire VA Medical Center) | 83% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Commonwealth University of Pennsylvania | 31 | no institution |
| Boston University , , 590 Commonwealth Avenue , , , | 21 | Boston University |
| Virginia Commonwealth University - Massey Comprehensive Cancer Center, Richmond, VA | 21 | VCU Massey Comprehensive Cancer Center |
| Virginia Commonwealth University Massey Cancer Center, Richmond, VA | 15 | VCU Massey Comprehensive Cancer Center |
| Virginia Commonwealth University Massey Cancer Center, Richmond, VA; | 15 | VCU Massey Comprehensive Cancer Center |
| Virginia Commonwealth University, Massey Cancer Center, Richmond, VA, USA | 15 | VCU Massey Comprehensive Cancer Center |
| Virginia Commonwealth University Massey Cancer Center | 14 | VCU Massey Comprehensive Cancer Center |
| Virginia Commonwealth University Massey Cancer Center, Richmond, VA, USA | 14 | VCU Massey Comprehensive Cancer Center |
| Virginia Commonwealth University, Massey Cancer Center, Richmond, VA | 13 | VCU Massey Comprehensive Cancer Center |
| VCU Pauley Heart Center, Richmond, VA, USA | 12 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Physical Medicine and Rehabilitation, and Professor of Neurosurgery, and Psychiatry Virginia Commonwealth University – Medical Center Depart | 1,321 | Virginia Commonwealth University Medical Center |
| Assistant Professor, Departments of Pathology and Dermatology, Director of Dermatopathology Services, Virgina Commonwealth University Medica | 366 | Virginia Commonwealth University Medical Center |
| Children's Hospital of Richmond at VCU | 48 | Children's Hospital of Richmond at VCU |
| VCU Medical Center | 34 | Virginia Commonwealth University Medical Center |
| Dep. Chem., Va. Commonw. Univ., Richmond, VA 23284, USA | 24 | no institution |
| Dep. Med. Chem., Sch. Pharm., Va. Commonw. Univ., Richmond, VA 23298, USA | 24 | no institution |
| Medical College of Virginia/Virginia Commonwealth Univ. (USA) | 22 | Virginia Commonwealth University Medical Center |
| Department of Emergency Medicine, Virginia Commonwealth University Medical Center, P.O. Box 980401, Richmond, VA, 23298-0401, USA | 17 | Virginia Commonwealth University Medical Center |
| Department of Microbiology and Immunology, Virginia Commonwealth University Medical Center, School of Medicine, Richmond, Virginia, USA | 17 | Virginia Commonwealth University Medical Center |
| Children's Hospital of Richmond at VCU, Richmond, VA, USA | 16 | Children's Hospital of Richmond at VCU |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
