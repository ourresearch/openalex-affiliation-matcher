# Wellcome Trust

[OpenAlex I87048295](https://openalex.org/institutions/I87048295) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Wellcome Trust itself): 34,576 → 21,056 (−39.1%).
- **Counting its units and predecessors** (the `lineage` filter): 131,753 → 111,975 (−15.0%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (67% of lost works); the largest share of the strings it gained were assigned to other institutions before (46% of gained works), mostly European Bioinformatics Institute, Wellcome Library.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Wellcome Trust at all, about **81% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **72% do name it** or one of its units.

**12,550 strings lost Wellcome Trust** ([removed.csv.gz](removed.csv.gz)), on 22,942 works; **2,483 strings gained it** ([added.csv](added.csv)), on 4,221 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 67% |
| To other institutions (mostly European Bioinformatics Institute, University of Dundee, University of Oxford) | 27% |
| To no institution | 6% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 15% |
| Up from one of its units or predecessors | 39% |
| From other institutions (mostly European Bioinformatics Institute, Wellcome Library, Bioinformatics Institute) | 46% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Cancer Genome Project, Wellcome Trust, Sanger Institute | 234 | Wellcome Sanger Institute |
| The Wellcome Trust Centre for the History of Medicine at UCL | 190 | Wellcome Trust Centre for the History of Medicine |
| KEMRI-Wellcome Trust Research Programme | 159 | Kenya Medical Research Institute, KEMRI-Wellcome Trust Research Programme |
| Wellcome Trust Centre for Neuroimaging, University College London, London, UK | 150 | University College London, Wellcome Centre for Human Neuroimaging |
| Wellcome Trust/Cancer Research UK Gurdon Institute, University of Cambridge, UK | 136 | University of Cambridge, The Gurdon Institute |
| Wellcome Trust-MRC Institute of Metabolic Science, University of Cambridge, Cambridge, UK | 86 | University of Cambridge, Wellcome/MRC Institute of Metabolic Science |
| Wellcome/MRC Cambridge Stem Cell Institute | 85 | Wellcome/MRC Cambridge Stem Cell Institute |
| Wellcome Trust Centre for Neuroimaging, Institute of Neurology, University College London, London, UK | 79 | University College London, Wellcome Centre for Human Neuroimaging, UCL Queen Square Institute of Neurology |
| Oxford University Clinical Research Unit, Wellcome Trust Major Overseas Programme, Ho Chi Minh City, Vietnam | 77 | Oxford University Clinical Research Unit |
| Wellcome Trust Centre for Neuroimaging, University College London, United Kingdom | 75 | University College London, Wellcome Centre for Human Neuroimaging |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Wellcome Institute | 456 | Wellcome Library |
| Wellcome Institute for the History of Medicine, London | 204 | University College London, Wellcome Trust Centre for the History of Medicine |
| Wellcome Institute for the History of Medicine | 187 | University College London, Wellcome Trust Centre for the History of Medicine |
| Wellcome Institute for the History of Medicine London | 78 | University College London, Wellcome Trust Centre for the History of Medicine |
| Wellcome Institute for the History of MedicineLondon | 74 | University College London, Wellcome Trust Centre for the History of Medicine |
| Wellcome Trust Research Laboratories, Nairobi, Kenya | 41 | Kenya Medical Research Institute |
| JDRF/Wellcome Diabetes and Inflammation Laboratory, Wellcome Centre for Human Genetics, Nuffield Department of Medicine, NIHR Oxford Biomedi | 24 | Centre for Human Genetics, University of Oxford |
| Wellcome Trust Research Laboratories, P.O. Box 43640, Nairobi, Kenya | 19 | Kenya Medical Research Institute |
| Wellcome Genome Campus | 14 | no institution |
| The Wellcome Institute for the History of Medicine | 13 | University College London, Wellcome Trust Centre for the History of Medicine |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
