# University Hospital Carl Gustav Carus

[OpenAlex I4210162051](https://openalex.org/institutions/I4210162051) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University Hospital Carl Gustav Carus itself): 26,204 → 28,685 (+9.5%).
- **Counting its units and predecessors** (the `lineage` filter): 43,325 → 33,181 (−23.4%).
- **Why:** most of the strings it lost now go to other institutions (88% of lost works), mostly Technische Universität Dresden, OncoRay; most of the strings it gained moved up from one of its units (52% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University Hospital Carl Gustav Carus at all, about **86% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **98% do name it** or one of its units.

**5,881 strings lost University Hospital Carl Gustav Carus** ([removed.csv.gz](removed.csv.gz)), on 8,394 works; **8,210 strings gained it** ([added.csv.gz](added.csv.gz)), on 12,085 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 10% |
| To other institutions (mostly Technische Universität Dresden, OncoRay, Herzzentrum Dresden Universitätsklinik) | 88% |
| To no institution | 2% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 19% |
| Up from one of its units or predecessors | 52% |
| From other institutions (mostly Technische Universität Dresden, Klinik und Poliklinik für Kinder- und Jugendmedizin, Klinik für Frauenheilkunde) | 29% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Faculty of Medicine Carl Gustav Carus, Technische Universität Dresden, Fetscher Str. 74, 01307, Dresden, Germany | 105 | Technische Universität Dresden |
| Faculty of Medicine Carl Gustav Carus, Technische Universität Dresden, Fetscher Str. 74, 0307, Dresden, Germany | 75 | Technische Universität Dresden |
| Department of Pediatrics, Medizinische Fakultät Carl Gustav Carus, Technische Universität Dresden, Dresden, Germany | 58 | Technische Universität Dresden |
| Institute for Medical Informatics and Biometry, Carl Gustav Carus Faculty of Medicine, Technische Universität Dresden, Dresden, Germany | 53 | Technische Universität Dresden |
| Else Kroener Fresenius Center for Digital Health, Medical Faculty Carl Gustav Carus, Technical University Dresden, Dresden, Germany | 51 | Technische Universität Dresden, Else Kröner Fresenius Center for Digital Health |
| Institute for Medical Informatics and Biometry, Faculty of Medicine Carl Gustav Carus, Technische Universität Dresden, Dresden, Germany | 40 | Technische Universität Dresden |
| Technische Universität Dresden, Medizinische Fakultät Carl Gustav Carus, Bereich Allgemeinmedizin, Dresden, Deutschland | 22 | Technische Universität Dresden |
| Medical Oncology Department, Technische Universität Dresden - Carl Gustav Carus Faculty of Medicine, Dresden, Germany | 21 | Technische Universität Dresden |
| Abteilung Neuropädiatrie, Medizinische Fakultät Carl Gustav Carus, Technische Universität Dresden, Dresden, Germany | 20 | Technische Universität Dresden |
| Medical Clinic I, University Hospital, Dresden, Germany, | 19 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Universitätsklinikum Carl Gustav Carus | 69 | no institution |
| Department of Medicine I, University Hospital Dresden, Dresden, Germany | 61 | no institution |
| Universitätsklinikum Dresden | 50 | Klinik und Poliklinik für Psychotherapie und Psychosomatik |
| Klinik für Psychotherapie und Psychosomatik, Universitätsklinikum Carl Gustav Carus, TU Dresden | 44 | Klinik und Poliklinik für Psychotherapie und Psychosomatik, Technische Universität Dresden |
| Klinik und Poliklinik für Psychotherapie und Psychosomatik, Universitätsklinik „Carl Gustav Carus“, Dresden | 37 | Klinik und Poliklinik für Psychotherapie und Psychosomatik |
| Stabsstelle Didaktik & Lehrforschung, Universitätsklinikum Carl Gustav Carus an der Technischen Universität Dresden, Dresden, Deutschland | 35 | Klinik und Poliklinik für Psychotherapie und Psychosomatik |
| Klinik und Poliklinik für Anästhesiologie und Intensivtherapie, Universitätsklinikum Carl Gustav Carus an der Technischen Universität Dresde | 33 | Klinik und Poliklinik für Psychotherapie und Psychosomatik |
| Klinik für Anästhesiologie und Intensivtherapie Universitätsklinikum Carl Gustav Carus, Technischen Universität Dresden, Fetscherstraße 74,  | 31 | Klinik und Poliklinik für Psychotherapie und Psychosomatik |
| Klinik für Psychosomatik und Psychotherapeutische Medizin, Uniklinik Dresden | 30 | Klinik für Psychosomatik |
| Universitätsklinikum Carl Gustav Carus an der Technischen Universität Dresden | 30 | Klinik und Poliklinik für Psychotherapie und Psychosomatik |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
