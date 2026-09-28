# University of Dundee

[OpenAlex I177639307](https://openalex.org/institutions/I177639307) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Dundee itself): 65,988 → 67,986 (+3.0%).
- **Counting its units and predecessors** (the `lineage` filter): 66,719 → 68,072 (+2.0%).
- **Why:** most of the strings it lost now have no institution (72% of lost works); the largest share of the strings it gained were assigned to other institutions before (46% of gained works), mostly Ninewells Hospital, Dundee Dental Hospital.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Dundee at all, about **96% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **89% do name it** or one of its units.

**720 strings lost University of Dundee** ([removed.csv](removed.csv)), on 978 works; **2,951 strings gained it** ([added.csv](added.csv)), on 4,332 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly University of St Andrews, Abertay University, NHS Tayside) | 28% |
| To no institution | 72% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 32% |
| Up from one of its units or predecessors | 23% |
| From other institutions (mostly Ninewells Hospital, Dundee Dental Hospital, Acadia University) | 46% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Dundee/UK | 48 | no institution |
| Dundee College of Technology | 26 | no institution |
| Dundee Institute of Technology | 13 | no institution |
| (Dundee Township Public Library, Dundee, Illinois, USA) | 11 | no institution |
| Dundee DD1 9SY, UK | 11 | no institution |
| Dundee Institute of Technology, UK | 11 | no institution |
| Dundee United Kingdom | 11 | no institution |
| STAR-Dundee Ltd., Dundee, UK | 8 | no institution |
| Dundee DD1 9SY | 7 | no institution |
| Association for Medical Education in Europe Dundee UK | 5 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Dundee Law School | 168 | Dundee Dental Hospital |
| Queen's College, Dundee | 60 | Acadia University |
| Cardiovascular Epidemiology Unit, Ninewells Hospital and Medical School, Dundee | 24 | Ninewells Hospital |
| MRC Protein Phosphorylation Unit, MSI/WTB Complex, University of Dundee, Dow Street, Dundee DD1 5EH, Scotland, U.K | 20 | MRC Protein Phosphorylation and Ubiquitylation Unit |
| Medical Research Council Protein Phosphorylation and Ubiquitylation Unit , School of Life Sciences , University of Dundee , Dow Street , Dun | 20 | MRC Protein Phosphorylation and Ubiquitylation Unit |
| Department of Pharmacology and Therapeutics, Queen's College, Dundee | 19 | no institution |
| Department of Biological Sciences, The University, Dundee DD1 4HN, Scotland | 18 | no institution |
| University Department of Medicine, Ninewells Hospital and Medical School, Dundee, Scotland | 18 | Ninewells Hospital |
| Centre for Medical Education, Ninewells Hospital & Medical School, Dundee | 17 | Ninewells Hospital |
| Department of Biological Sciences, The University, DD1 4HN, Dundee, Scotland | 17 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
