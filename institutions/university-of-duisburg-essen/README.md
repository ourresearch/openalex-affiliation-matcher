# University of Duisburg-Essen

[OpenAlex I62318514](https://openalex.org/institutions/I62318514) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Duisburg-Essen itself): 88,496 → 100,363 (+13.4%).
- **Counting its units and predecessors** (the `lineage` filter): 90,583 → 102,206 (+12.8%).
- **Why:** most of the strings it lost now have no institution (67% of lost works); most of the strings it gained had no institution before (58% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Duisburg-Essen at all, about **36% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **100% do name it** or one of its units.

**739 strings lost University of Duisburg-Essen** ([removed.csv](removed.csv)), on 1,080 works; **13,891 strings gained it** ([added.csv.gz](added.csv.gz)), on 20,773 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Essen University Hospital, Stiftung Universitätsmedizin Essen, West German Heart and Vascular Center Essen) | 33% |
| To no institution | 67% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 58% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly Essen University Hospital, West German Heart and Vascular Center Essen, Ruhrlandklinik) | 42% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Duisburg-Essen, Deutschland | 51 | no institution |
| Univ. of Essen (Germany) | 21 | no institution |
| Department of Thoracic and Cardiovascular Surgery, West German Heart Center Essen, University Hospital Essen, Essen, Germany - | 18 | Essen University Hospital, West German Heart and Vascular Center Essen |
| Pharmakologisches Institut der Universität Essen, Essen 1, Federal Republic of Germany | 15 | no institution |
| Department of Obstetrics and Gynecology, University of Essen, School of Medicine, Essen, Germany | 10 | Essen University Hospital |
| Dept. of Comput. Sci., Gerhard-Mercator-University Duisburg, Germany#TAB# | 10 | no institution |
| Pharmakologisches Institut der Universität Essen, Hufelandstrasse 55, D-4300, Essen 1, Federal Republic of Germany | 10 | no institution |
| School of Medicine, University of Essen, Essen, Germany | 10 | Essen University Hospital |
| Center for Nanointegration Duisburg-Essen (CENIDE), Germany | 9 | no institution |
| Department of Medicine, University of Essen, FRG | 9 | Essen University Hospital |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| University of Essen | 220 | no institution |
| University of Essen, Essen, Germany | 172 | no institution |
| Institute of Pharmacology, West German Heart and Vascular Center, University Duisburg-Essen, Essen, Germany | 127 | West German Heart and Vascular Center Essen |
| University of Essen, Germany | 111 | no institution |
| Erwin L. Hahn Institute for Magnetic Resonance Imaging, University Duisburg-Essen, Essen, Germany | 110 | Erwin L. Hahn Institute for Magnetic Resonance Imaging |
| Department of Medical Oncology, West German Cancer Center, University Hospital Essen, University Duisburg-Essen, Essen, Germany | 69 | no institution |
| University of Duisburg | 67 | no institution |
| Institute of Pharmacology, West German Heart and Vascular Center, Faculty of Medicine, University Duisburg-Essen, Essen, Germany | 53 | West German Heart and Vascular Center Essen |
| Univ. Essen (Germany) | 48 | no institution |
| Institute for Virology, University Hospital Essen, University Duisburg-Essen, Essen, Germany | 46 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
