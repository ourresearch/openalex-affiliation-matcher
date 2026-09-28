# Utrecht University

[OpenAlex I193662353](https://openalex.org/institutions/I193662353) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Utrecht University itself): 248,303 → 264,144 (+6.4%).
- **Counting its units and predecessors** (the `lineage` filter): 250,603 → 264,667 (+5.6%).
- **Why:** most of the strings it lost now go to other institutions (91% of lost works), mostly University Medical Center Utrecht, University of Applied Sciences Utrecht; most of the strings it gained were assigned to other institutions before (71% of gained works), mostly University Medical Center Utrecht, Wilhelmina Children's Hospital.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Utrecht University at all, about **98% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **38% do name it** or one of its units.

**10,774 strings lost Utrecht University** ([removed.csv.gz](removed.csv.gz)), on 15,554 works; **24,372 strings gained it** ([added.csv.gz](added.csv.gz)), on 42,329 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly University Medical Center Utrecht, University of Applied Sciences Utrecht, Netherlands Organisation for Applied Scientific Research) | 91% |
| To no institution | 9% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 29% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly University Medical Center Utrecht, Wilhelmina Children's Hospital, Pharmo Institute) | 71% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Utrecht University of Applied Sciences | 175 | University of Applied Sciences Utrecht |
| University Medical Center Utrecht, , the Netherlands | 150 | University Medical Center Utrecht |
| UMC Utrecht, Utrecht, The Netherlands | 134 | University Medical Center Utrecht |
| Univ. Med. Ctr. Utrecht, Utrecht, Netherlands | 115 | University Medical Center Utrecht |
| Univ. Medical Ctr., Utrecht (Netherlands) | 108 | University Medical Center Utrecht |
| Univ Med Cntr Utrecht, Utrecht, Netherlands | 74 | University Medical Center Utrecht |
| Department of Vascular Surgery, University Medical Center Utrecht , Utrecht, The Netherlands | 69 | University Medical Center Utrecht |
| Center for Research and Development of Education, University Medical Center Utrecht, Utrecht, The Netherlands | 58 | University Medical Center Utrecht |
| Department of Neonatology, University Medical Center Utrecht, Utrecht, The Netherlands | 48 | University Medical Center Utrecht |
| Department of Vascular Surgery; University Medical Center Utrecht, The Netherlands; | 45 | University Medical Center Utrecht |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Julius Center for Health Sciences and Primary Care, University Medical Center Utrecht, Utrecht, The Netherlands | 1,660 | University Medical Center Utrecht |
| Julius Center for Health Sciences and Primary Care, University Medical Center Utrecht, Utrecht, the Netherlands | 586 | University Medical Center Utrecht |
| Image Sciences Institute, University Medical Center Utrecht, Utrecht, The Netherlands | 390 | University Medical Center Utrecht |
| Julius Centre for Health Sciences and Primary Care, University Medical Centre Utrecht, Utrecht, The Netherlands | 280 | University Medical Center Utrecht |
| Julius Center for Health Sciences and Primary Care, University Medical Center Utrecht, Utrecht, Netherlands | 277 | University Medical Center Utrecht |
| Julius Center for Health Sciences and Primary Care, University Medical Center, Utrecht, The Netherlands | 251 | University Medical Center Utrecht |
| Department of Medical Microbiology, University Medical Center Utrecht, Utrecht, the Netherlands | 143 | University Medical Center Utrecht |
| Department of Haematology, University Hospital Utrecht, The Netherlands | 129 | no institution |
| Department of Epidemiology, Julius Center for Health Sciences and Primary Care, University Medical Center Utrecht, Utrecht, The Netherlands | 124 | University Medical Center Utrecht |
| Rudolf Magnus Institute for Pharmacology, Medical Faculty University of Utrecht, Vondellaan 6, 3521 GD Utrecht, The Netherlands | 121 | University Medical Center Utrecht |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
