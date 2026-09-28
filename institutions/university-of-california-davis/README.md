# University of California, Davis

[OpenAlex I84218800](https://openalex.org/institutions/I84218800) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of California, Davis itself): 316,569 → 321,396 (+1.5%).
- **Counting its units and predecessors** (the `lineage` filter): 316,581 → 321,527 (+1.6%).
- **Why:** most of the strings it lost now go to other institutions (66% of lost works), mostly UC Davis Comprehensive Cancer Center, University of California Davis Medical Center; the largest share of the strings it gained were assigned to other institutions before (50% of gained works), mostly University of California Davis Medical Center, Veterinary Medical Teaching Hospital.

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**3,033 strings lost University of California, Davis** ([removed.csv](removed.csv)), on 5,939 works; **12,556 strings gained it** ([added.csv.gz](added.csv.gz)), on 18,156 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To its parent institution | 1% |
| To other institutions (mostly UC Davis Comprehensive Cancer Center, University of California Davis Medical Center, UC Davis Health) | 66% |
| To no institution | 33% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 45% |
| Up from one of its units or predecessors | 0% |
| Down from its parent institution | 5% |
| From other institutions (mostly University of California Davis Medical Center, Veterinary Medical Teaching Hospital, Lawrence Livermore National Laboratory) | 50% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Davis, California | 185 | no institution |
| UC Davis Comprehensive Cancer Center, Sacramento, CA | 160 | UC Davis Comprehensive Cancer Center |
| University of California Davis Comprehensive Cancer Center, Sacramento, CA | 153 | UC Davis Comprehensive Cancer Center |
| University of California Davis Comprehensive Cancer Center, Sacramento, CA; | 129 | UC Davis Comprehensive Cancer Center |
| Davis, CA | 117 | no institution |
| UC Davis Comprehensive Cancer Center | 110 | UC Davis Comprehensive Cancer Center |
| Davis, USA | 98 | no institution |
| University of California (Davis) Medical Center | 95 | University of California Davis Medical Center |
| Davis, California, USA | 80 | no institution |
| Davis, CA, USA | 76 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Univ of California/Davis (United States) | 476 | no institution |
| California Univ., Davis, CA (United States) | 213 | no institution |
| @ucdavis | 144 | University of California System |
| Department of Electrical and Computer Engineering, University of California,슠Davis, Davis, CA, USA | 117 | no institution |
| California Animal Health and Food Safety Laboratory System, Davis, CA, USA | 97 | no institution |
| California Univ., Davis, CA (USA) | 96 | no institution |
| Mosquito Control Research Laboratory, Department of Entomology and Nematology and Vector Genetics Laboratory, Department of Pathology, Micro | 91 | Université de Dschang |
| @dib-lab - @ucdavis | 80 | no institution |
| University of CaliforniaDavis | 80 | no institution |
| California, University Davis, CA, United States | 78 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
