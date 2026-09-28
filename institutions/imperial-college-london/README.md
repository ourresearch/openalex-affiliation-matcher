# Imperial College London

[OpenAlex I47508984](https://openalex.org/institutions/I47508984) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Imperial College London itself): 409,975 → 432,291 (+5.4%).
- **Counting its units and predecessors** (the `lineage` filter): 411,816 → 434,463 (+5.5%).
- **Why:** most of the strings it lost now go to other institutions (53% of lost works), mostly St Mary's Hospital, University College London; most of the strings it gained were assigned to other institutions before (75% of gained works), mostly Hammersmith Hospital, Imperial Valley College.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Imperial College London at all, about **34% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **96% do name it** or one of its units.

Net, the works that really are Imperial College London's (counting its units) went up by about 5.4%.

**1,172 strings lost Imperial College London** ([removed.csv](removed.csv)), on 1,878 works; **25,300 strings gained it** ([added.csv.gz](added.csv.gz)), on 42,015 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly St Mary's Hospital, University College London, Charing Cross Hospital) | 53% |
| To no institution | 47% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 24% |
| Up from one of its units or predecessors | 1% |
| From other institutions (mostly Hammersmith Hospital, Imperial Valley College, St Mary's Hospital) | 75% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Mathematical Institute, Tôkyô Imperial University | 91 | no institution |
| Professor of Diagnostic Haematology; St Mary's Hospital Campus of Imperial College; Faculty of Medicine, London and Honorary Consultant Haem | 87 | St Mary's Hospital |
| St Mary’s Hospital, Medical School | 33 | St Mary's Hospital |
| Imperial College University of London | 31 | no institution |
| st Mary's Hospital Medical School London UK | 29 | St Mary's Hospital |
| Imperial College London NHS Trust, London, UK | 20 | no institution |
| Imperial College School of Medicine, Hammersmith Hospital, London, UK; | 18 | Hammersmith Hospital |
| Department of Pathology, St. Mary's Hospital Medical School, London, | 15 | St Mary's Hospital |
| Botany in the Science College, Imperial University of Tokyo | 13 | no institution |
| Charing Cross Hospital, Medical School | 13 | Charing Cross Hospital |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Imperial College | 3,705 | Imperial Valley College |
| imperial College | 1,477 | Imperial Valley College |
| Imperial Coll., London | 1,330 | no institution |
| Imperial College Business School | 1,049 | no institution |
| Dep. Chem., Imp. Coll. Sci. Technol. Med., London SW7 2AY, UK | 352 | no institution |
| Dep. Chem., Imp. Coll., London SW7 2AZ, UK | 224 | no institution |
| Imperial College School of Medicine | 135 | Imperial Valley College |
| Imperial College of Science | 112 | Imperial Valley College |
| Dep. Chem., Imp. Coll. Sci., Technol. Med., London SW7 2AY, UK | 109 | no institution |
| National Heart and Lung Institute, Imperial College | 71 | Lung Institute |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
