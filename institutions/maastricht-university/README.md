# Maastricht University

[OpenAlex I34352273](https://openalex.org/institutions/I34352273) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Maastricht University itself): 135,307 → 133,916 (−1.0%).
- **Counting its units and predecessors** (the `lineage` filter): 137,111 → 135,663 (−1.1%).
- **Why:** the largest share of the strings it lost now have no institution (50% of lost works); most of the strings it gained were assigned to other institutions before (55% of gained works), mostly Maastricht University Medical Centre, Transnational University Limburg.

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**5,993 strings lost Maastricht University** ([removed.csv.gz](removed.csv.gz)), on 9,184 works; **7,197 strings gained it** ([added.csv.gz](added.csv.gz)), on 8,476 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 2% |
| To other institutions (mostly Maastricht University Medical Centre, European Graduate School of Neuroscience, RWTH Aachen University) | 48% |
| To no institution | 50% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 37% |
| Up from one of its units or predecessors | 8% |
| From other institutions (mostly Maastricht University Medical Centre, Transnational University Limburg, Maastro Clinic) | 55% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Maastricht, The Netherlands | 354 | no institution |
| Maastricht | 195 | no institution |
| University Eye Clinic Maastricht, Maastricht, The Netherlands | 117 | no institution |
| Cardiovascular Research Institute, Maastricht, The Netherlands | 80 | no institution |
| Department of Pathology, University of Limburg, Maastricht, The Netherlands | 72 | no institution |
| Department of Medical Microbiology, University of Limburg, Maastricht, The Netherlands | 69 | no institution |
| Department of Molecular Cell Biology and Genetics, University of Limburg, Maastricht, The Netherlands | 68 | no institution |
| Maastricht/NL | 61 | no institution |
| Maastricht, the Netherlands | 58 | no institution |
| Department of Pharmacology, University of Limburg,   Maastricht, The Netherlands | 55 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Department of Human Biology, NUTRIM School for Nutrition, Toxicology and Metabolism, Maastricht University Medical Centre, Maastricht, The N | 26 | Maastricht University Medical Centre |
| Department of Psychiatry and Psychology, School for Mental Health and Neuroscience, Maastricht University Medical Centre, Maastricht, The Ne | 26 | Maastricht University Medical Centre |
| Department of Psychiatry and Psychology, School of Mental Health and Neuroscience, Maastricht University Medical Centre, Maastricht, The Net | 22 | Maastricht University Medical Centre |
| Department of Respiratory Medicine, NUTRIM School of Nutrition and Translational Research in Metabolism, Maastricht University Medical Centr | 17 | Maastricht University Medical Centre |
| Department of Otorhinolaryngology and Head and Neck Surgery, Maastricht University Medical Centre, Maastricht, The Netherlands | 15 | Maastricht University Medical Centre |
| Department of Psychiatry and Neuropsychology, Maastricht University Medical Centre, Maastricht, The Netherlands | 15 | Maastricht University Medical Centre |
| University Eye Clinic Maastricht | 15 | no institution |
| Department of Cardiology, Academic Hospital Maastricht, University of Limburg, Maastricht, The Netherlands | 14 | Maastricht University Medical Centre |
| Department of Anesthesiology and Pain Management, Maastricht University Medical Centre, Maastricht, The Netherlands; | 13 | Maastricht University Medical Centre |
| Department of Anesthesiology and Pain Medicine, Maastricht University Medical Centre, Maastricht, The Netherlands | 13 | Maastricht University Medical Centre |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
