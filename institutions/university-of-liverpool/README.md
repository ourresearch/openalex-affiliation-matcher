# University of Liverpool

[OpenAlex I146655781](https://openalex.org/institutions/I146655781) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of Liverpool itself): 230,250 → 202,537 (−12.0%).
- **Counting its units and predecessors** (the `lineage` filter): 231,582 → 203,411 (−12.2%).
- **Why:** most of the strings it lost now go to other institutions (94% of lost works), mostly Royal Liverpool University Hospital, Aintree University Hospital; most of the strings it gained were assigned to other institutions before (51% of gained works), mostly Liverpool School of Tropical Medicine, Liverpool College.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Liverpool at all, about **98% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **41% do name it** or one of its units.

Net, the works that really are University of Liverpool's (counting its units) went up by about 0.5%.

**33,657 strings lost University of Liverpool** ([removed.csv.gz](removed.csv.gz)), on 62,919 works; **4,188 strings gained it** ([added.csv](added.csv)), on 6,705 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Royal Liverpool University Hospital, Aintree University Hospital, Alder Hey Children's Hospital) | 94% |
| To no institution | 6% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 48% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly Liverpool School of Tropical Medicine, Liverpool College, Xi’an Jiaotong-Liverpool University) | 51% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Malawi-Liverpool-Wellcome Trust Clinical Research Programme | 2,219 | Malawi-Liverpool-Wellcome Trust Clinical Research Programme |
| Royal Liverpool University Hospital, Liverpool, UK | 525 | Royal Liverpool University Hospital |
| Royal Liverpool University Hospital | 445 | Royal Liverpool University Hospital |
| Liverpool University Hospitals NHS Foundation Trust, Liverpool, UK | 378 | Liverpool University Hospitals NHS Foundation Trust |
| Liverpool Heart and Chest Hospital | 368 | Liverpool Heart and Chest Hospital |
| Malawi-Liverpool-Wellcome Trust Clinical Research Programme, Blantyre, Malawi | 354 | Malawi-Liverpool-Wellcome Trust Clinical Research Programme |
| Liverpool Heart and Chest Hospital, Liverpool, UK | 311 | Liverpool Heart and Chest Hospital |
| Alder Hey Children's Hospital | 285 | Alder Hey Children's Hospital |
| Liverpool University Hospitals NHS Foundation Trust | 243 | Liverpool University Hospitals NHS Foundation Trust |
| Alder Hey Children's Hospital, Liverpool, UK | 238 | Alder Hey Children's Hospital |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| [Xi'an Jiaotong, Liverpool University] | 146 | Xi’an Jiaotong-Liverpool University |
| Liverpool University, UK | 136 | no institution |
| The University , Liverpool | 100 | no institution |
| The University, Liverpool | 91 | no institution |
| University College, Liverpool | 57 | Liverpool College |
| Liverpool U., Dept. Math | 42 | no institution |
| Liverpool University UK | 39 | no institution |
| Liverpool Business School | 36 | Liverpool College |
| The University Liverpool | 36 | no institution |
| University College Liverpool | 33 | Liverpool College |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
