# University of California System

[OpenAlex I2803209242](https://openalex.org/institutions/I2803209242) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of California System itself): 70,045 → 31,140 (−55.5%).
- **Counting its units and predecessors** (the `lineage` filter): 2,625,300 → 2,726,827 (+3.9%).
- **Why:** most of the strings it lost now have no institution (65% of lost works); most of the strings it gained had no institution before (55% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of California System at all, about **31% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **95% do name it** or one of its units.

Net, the works that really are University of California System's (counting its units) went up by about 4.1%.

**15,640 strings lost University of California System** ([removed.csv.gz](removed.csv.gz)), on 63,406 works; **17,501 strings gained it** ([added.csv.gz](added.csv.gz)), on 28,264 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 34% |
| To other institutions (mostly University of Southern California, University of Toronto, California University of Science and Medicine) | 1% |
| To no institution | 65% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 55% |
| Up from one of its units or predecessors | 22% |
| From other institutions (mostly Lawrence Livermore National Laboratory, Bay Institute, Virginia Cooperative Extension) | 23% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| University of California | 39,108 | no institution |
| University of California , , , , | 857 | no institution |
| University of California Press Oakland, California | 345 | no institution |
| Department of Radiology and Biomedical Imaging, University of California San Francisco, San Francisco, CA, USA | 341 | University of California, San Francisco |
| University of California, | 241 | no institution |
| University of California , | 195 | no institution |
| The University of California | 188 | no institution |
| @ucdavis | 144 | University of California, Davis |
| Department of Radiology and Biomedical Imaging, University of California San Francisco, San Francisco, California, USA | 137 | University of California, San Francisco |
| Department of Radiology and Biomedical Imaging, University of California San Francisco, San Francisco, California | 114 | University of California, San Francisco |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Lawrence Radiation Laboratory, University of California, Livermore, California | 638 | Lawrence Livermore National Laboratory |
| university of california, United States | 497 | University of California, Berkeley |
| University of California USA | 414 | no institution |
| Lawrence Radiation Laboratory, University of California, Livermore, California 94550 | 332 | Lawrence Livermore National Laboratory |
| University of California,  USA | 175 | no institution |
| Department of Medicine, University of California | 148 | no institution |
| UC - University of California (United States) | 134 | no institution |
| Universidade da Califórnia | 88 | no institution |
| University of California, CA, USA | 87 | no institution |
| Department of Neurology, University of California | 79 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
