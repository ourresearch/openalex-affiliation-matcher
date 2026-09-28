# Technische Universität Dresden

[OpenAlex I78650965](https://openalex.org/institutions/I78650965) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Technische Universität Dresden itself): 147,881 → 153,303 (+3.7%).
- **Counting its units and predecessors** (the `lineage` filter): 154,998 → 158,583 (+2.3%).
- **Why:** most of the strings it lost now have no institution (86% of lost works); most of the strings it gained were assigned to other institutions before (62% of gained works), mostly University Hospital Carl Gustav Carus, Klinik und Poliklinik für Psychotherapie und Psychosomatik.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Technische Universität Dresden at all, about **93% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **92% do name it** or one of its units.

**1,443 strings lost Technische Universität Dresden** ([removed.csv](removed.csv)), on 8,251 works; **16,918 strings gained it** ([added.csv.gz](added.csv.gz)), on 23,341 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 1% |
| To other institutions (mostly University Hospital Carl Gustav Carus, Herzzentrum Dresden Universitätsklinik, Klinik und Poliklinik für Hals-, Nasen- und Ohrenheilkunde) | 13% |
| To no institution | 86% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 26% |
| Up from one of its units or predecessors | 12% |
| From other institutions (mostly University Hospital Carl Gustav Carus, Klinik und Poliklinik für Psychotherapie und Psychosomatik, Munich University of Applied Sciences) | 62% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Dresden | 5,940 | no institution |
| Dresden, | 372 | no institution |
| @tud-cor @tud-dri @sam-xl | 49 | no institution |
| Hannah-Arendt-Institut für Totalitarismusforschung e.V. an der TU Dresden | 29 | Hannah-Arendt-Institut für Totalitarismusforschung e.V. an der TU Dresden |
| University of Dresden, Department of Neurology, Dresden, Germany | 15 | no institution |
| Dresden , Germany  | 13 | no institution |
| t Dresden, Germany | 13 | no institution |
| Internal Medicine I University Hospital Carl Gustav Carus Dresden Germany | 12 | University Hospital Carl Gustav Carus |
| Heart Centre Dresden - Dresden Technical University Hospital , Dresden , | 10 | Herzzentrum Dresden Universitätsklinik |
| Institute of Pathology, University Hospital Dresden, Dresden, Germany | 10 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Technischen Hochschule Dresden, Deutschland | 96 | no institution |
| University of Dresden | 91 | no institution |
| University of Dresden, Dresden, Germany | 82 | no institution |
| Technischen Hochschule, Dresden, Deutschland | 79 | no institution |
| Dresden, Institut für anorganische und anorganisch-technische Chemie der Technischen Hochschule | 76 | Munich University of Applied Sciences |
| Technischen Hochschule Dresden | 74 | no institution |
| INST F. FESTKOERPERPHYS, TU DRESDEN | 73 | no institution |
| Dresden, Institut für anorganische und anorganisch‐technische Chemie der Technischen Hochschule | 65 | Munich University of Applied Sciences |
| Else Kroener Fresenius Center for Digital Health, Medical Faculty Carl Gustav Carus, Technical University Dresden, Dresden, Germany | 51 | University Hospital Carl Gustav Carus, Else Kröner Fresenius Center for Digital Health |
| Professor,         Technischen Hochschule, Dresden, Deutschland | 45 | Munich University of Applied Sciences |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
