# University of Göttingen

[OpenAlex I74656192](https://openalex.org/institutions/I74656192) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Göttingen itself): 174,915 → 205,865 (+17.7%).
- **Counting its units and predecessors** (the `lineage` filter): 178,246 → 209,520 (+17.5%).
- **Why:** most of the strings it lost now go to other institutions (78% of lost works), mostly Universitätsmedizin Göttingen, German Centre for Cardiovascular Research; most of the strings it gained were assigned to other institutions before (64% of gained works), mostly Universitätsmedizin Göttingen, Max Planck Institute of Experimental Medicine.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Göttingen at all, about **94% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **53% do name it** or one of its units.

**1,225 strings lost University of Göttingen** ([removed.csv](removed.csv)), on 3,252 works; **32,140 strings gained it** ([added.csv.gz](added.csv.gz)), on 55,770 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 2% |
| To other institutions (mostly Universitätsmedizin Göttingen, German Centre for Cardiovascular Research, Deutsches Zentrum für Luft- und Raumfahrt e. V. (DLR)) | 78% |
| To no institution | 20% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 35% |
| Up from one of its units or predecessors | 1% |
| From other institutions (mostly Universitätsmedizin Göttingen, Max Planck Institute of Experimental Medicine, Nanoscale Microscopy and Molecular Physiology of the Brain Cluster of Excellence 171 — DFG Research Center 103) | 64% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| University Medical Center, Goettingen | 833 | Universitätsmedizin Göttingen |
| Universitatsmedizin Göttingen | 165 | Universitätsmedizin Göttingen |
| University Medical Center Göttingen, Department of Medical Bioinformatics | 85 | Universitätsmedizin Göttingen |
| Department of Cellular Biochemistry, University Medical Center Göttingen, Göttingen, Germany | 54 | Universitätsmedizin Göttingen |
| Department of Neurology, University Medical Center, Göttingen, Germany | 54 | Universitätsmedizin Göttingen |
| Institute of Neuropathology, University Medical Center, Göttingen, Germany | 52 | Universitätsmedizin Göttingen |
| Department of Child and Adolescent Psychiatry and Psychotherapy, University Medical Centre Göttingen, von-Siebold-Str. 5, 37075, Göttingen,  | 42 | Universitätsmedizin Göttingen |
| Department of Neuro- and Sensory Physiology, University Medical Center Göttingen, Göttingen, Germany | 31 | Universitätsmedizin Göttingen |
| University Medical Center Goettingen; | 29 | Universitätsmedizin Göttingen |
| Institute of Pathology, University Medical Center, Göttingen, Germany | 26 | Universitätsmedizin Göttingen |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Universität Göttingen | 1,309 | Universitätsmedizin Göttingen |
| ENI-G, a Joint Initiative of the University Medical Center Göttingen and the Max Planck Institute for Multidisciplinary Sciences, Göttingen, | 1,121 | Max Planck Institute of Experimental Medicine |
| Universität GÖttingen | 777 | Universitätsmedizin Göttingen |
| Universität Göttingen, Göttingen, Deutschland | 518 | Universitätsmedizin Göttingen |
| Universität Göttingen, Deutschland | 405 | Universitätsmedizin Göttingen |
| Department of Psychiatry and Psychotherapy, University Medical Center Göttingen, Göttingen, Germany | 172 | Universitätsmedizin Göttingen |
| Universität Gottingen, Deutschland | 160 | Universitätsmedizin Göttingen |
| Institute of Pathology, University Medical Center Göttingen, Göttingen, Germany | 149 | Universitätsmedizin Göttingen |
| Universität Göttingen, Germany | 132 | Universitätsmedizin Göttingen |
| University of Goettingen and German Primate Center | 128 | German Primate Center |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
