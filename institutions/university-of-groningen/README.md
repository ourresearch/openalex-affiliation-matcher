# University of Groningen

[OpenAlex I169381384](https://openalex.org/institutions/I169381384) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Groningen itself): 194,428 → 205,586 (+5.7%).
- **Counting its units and predecessors** (the `lineage` filter): 197,582 → 209,135 (+5.8%).
- **Why:** most of the strings it lost now go to other institutions (85% of lost works), mostly University Medical Center Groningen, Beatrix Kinderziekenhuis; most of the strings it gained had no institution before (59% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Groningen at all, about **95% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **72% do name it** or one of its units.

**5,876 strings lost University of Groningen** ([removed.csv](removed.csv)), on 9,593 works; **9,187 strings gained it** ([added.csv.gz](added.csv.gz)), on 21,961 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 3% |
| To other institutions (mostly University Medical Center Groningen, Beatrix Kinderziekenhuis, Space Research Organisation Netherlands) | 85% |
| To no institution | 12% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 59% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly University Medical Center Groningen, Institute of Archaeology, Institute for Asthma and Allergy) | 41% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Kapteyn Astronomical Inst | 318 | no institution |
| Department of Internal Medicine, University Hospital Groningen, The Netherlands | 124 | University Medical Center Groningen |
| Department of Internal Medicine, University Hospital, Groningen, The Netherlands | 124 | University Medical Center Groningen |
| Dept. of Neurology, University Hospital, Groningen, the Netherlands | 71 | University Medical Center Groningen |
| Department of Developmental Neurology, University Hospital, Groningen, The Netherlands | 63 | University Medical Center Groningen |
| Groningen/NL | 63 | no institution |
| Department of Surgery, University Hospital, Groningen, The Netherlands | 61 | University Medical Center Groningen |
| Department of Clinical Immunology, University Hospital, Groningen, The Netherlands | 60 | University Medical Center Groningen |
| Department of Neurology, University Hospital, Groningen, The Netherlands | 60 | University Medical Center Groningen |
| Zernike Institute for Advanced Materials, Nijenborgh 4, 9747 AG Groningen, The Netherlands | 44 | Zernike Institute for Advanced Materials |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Groningen Research Institute f.t Study of Culture | 5,290 | no institution |
| Groningen Institute of Archaeology | 1,021 | Institute of Archaeology |
| Groningen Research Institute for Asthma and COPD (GRIAC) | 911 | Institute for Asthma and Allergy |
| Kapteyn Astronomical Institute, Groningen, The Netherlands | 189 | no institution |
| Kapteyn Astronomical Institute, PO Box 800, 9700 AV Groningen, The Netherlands | 162 | no institution |
| Kapteyn Astronomical Institute, Postbus 800, 9700 AV Groningen, The Netherlands | 150 | no institution |
| UMCG - University Medical Center Groningen [Groningen] (PO box 30.001 9700 RB Groningen - Netherlands) | 149 | University Medical Center Groningen |
| Kernfysisch Versneller Instituut, Groningen, The Netherlands | 145 | Zorginstituut Nederland |
| Groningen Research Institute of Pharmacy | 131 | no institution |
| University Hospital Groningen | 96 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
