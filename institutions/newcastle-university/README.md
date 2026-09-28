# Newcastle University

[OpenAlex I84884186](https://openalex.org/institutions/I84884186) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Newcastle University itself): 158,386 → 164,690 (+4.0%).
- **Counting its units and predecessors** (the `lineage` filter): 159,691 → 165,514 (+3.6%).
- **Why:** most of the strings it lost now go to other institutions (52% of lost works), mostly University of Newcastle Australia, Durham University; most of the strings it gained were assigned to other institutions before (54% of gained works), mostly University of Newcastle Australia, Newcastle Dental Hospital.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Newcastle University at all, about **56% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **84% do name it** or one of its units.

**1,335 strings lost Newcastle University** ([removed.csv](removed.csv)), on 1,810 works; **8,175 strings gained it** ([added.csv.gz](added.csv.gz)), on 12,582 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly University of Newcastle Australia, Durham University, Newcastle University Singapore) | 52% |
| To no institution | 48% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 43% |
| Up from one of its units or predecessors | 3% |
| From other institutions (mostly University of Newcastle Australia, Newcastle Dental Hospital, Universities UK) | 54% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Newcastle upon Tyne U.K | 50 | no institution |
| University of Newcastle (Australia) - Newcastle Business School, City Campus East – 231, Newcastle-Upon-Tyne NE1 8ST, NE1 8ST, Australia | 27 | University of Newcastle Australia |
| Newcastle upon Tyne/UK | 17 | no institution |
| University of Newcastle , N.S.W | 15 | University of Newcastle Australia |
| NEWCASTLE UNIVERSITY | 14 | no institution |
| The University of Newcastle , , , , | 14 | University of Newcastle Australia |
| Newcastle upon Tyne , NE6 2PA , UK British | 13 | no institution |
| Princess Mary Maternity Hospital, Newcastle‐upon‐Tyne | 10 | Princess Mary Maternity Hospital |
| Sch. of Electr. Eng. & Comput. Sci., Newcastle Univ., NSW | 10 | University of Newcastle Australia |
| Australian Museum Research Institute, Australian Museum, 1 William Street, Sydney, New South Wales 2010, Australia stephen.mahony@australian | 8 | University of Newcastle Australia, Australian Museum |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Dept. of Electr. & Electron. Eng., Newcastle-Upon-Tyne Univ., UK | 145 | Universities UK |
| Newcastle Business School, Northumbria University, UK | 124 | Northumbria University |
| Newcastle Law School | 110 | no institution |
| Univ. of Newcastle, Newcastle-upon-Tyne, UK#TAB# | 89 | no institution |
| School of Medicine and Public Health, University of Newcastle | 70 | University of Newcastle Australia |
| Dept. of Comput. Sci., Newcastle upon Tyne Univ., UK | 62 | Universities UK |
| Newcastle Business School | 61 | no institution |
| Univ. Newcastle upon Tyne, UK | 60 | Universities UK |
| University of Newcastle, Newcastle | 54 | no institution |
| School of Psychology, University of Newcastle | 50 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
