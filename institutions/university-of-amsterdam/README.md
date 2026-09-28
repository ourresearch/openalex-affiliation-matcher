# University of Amsterdam

[OpenAlex I887064364](https://openalex.org/institutions/I887064364) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Amsterdam itself): 256,129 → 244,961 (−4.4%).
- **Counting its units and predecessors** (the `lineage` filter): 257,845 → 245,966 (−4.6%).
- **Why:** most of the strings it lost now go to other institutions (82% of lost works), mostly Amsterdam UMC Location University of Amsterdam, Amsterdam University Medical Centers; most of the strings it gained had no institution before (66% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Amsterdam at all, about **82% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **90% do name it** or one of its units.

**25,349 strings lost University of Amsterdam** ([removed.csv.gz](removed.csv.gz)), on 33,372 works; **6,038 strings gained it** ([added.csv](added.csv)), on 11,969 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 1% |
| To other institutions (mostly Amsterdam UMC Location University of Amsterdam, Amsterdam University Medical Centers, Vrije Universiteit Amsterdam) | 82% |
| To no institution | 17% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 66% |
| Up from one of its units or predecessors | 4% |
| From other institutions (mostly Vrije Universiteit Amsterdam, Amsterdam University Medical Centers, Amsterdam University of Applied Sciences) | 30% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| VU University of Amsterdam - Department of Spatial Economics | 120 | Vrije Universiteit Amsterdam |
| Institute of Physics, University of Amsterdam | 104 | Institute of Physics |
| Department of Urology, AMC University Hospital, Amsterdam, The Netherlands | 83 | Amsterdam UMC Location University of Amsterdam |
| Amsterdam UMC Location University of Amsterdam | 70 | Amsterdam UMC Location University of Amsterdam |
| Amsterdam UMC, location University of Amsterdam, Department of Surgery, Amsterdam, the Netherlands | 61 | Amsterdam UMC Location University of Amsterdam |
| Free University of Amsterdam, Amsterdam, ND North Holland, Netherlands | 59 | Vrije Universiteit Amsterdam |
| Amsterdam University Medical Centre (AUMC) , Amsterdam , | 56 | Amsterdam University Medical Centers |
| Vrije Univ. Amsterdam (The Netherlands) | 52 | Vrije Universiteit Amsterdam |
| Amsterdam UMC location University of Amsterdam | 51 | Amsterdam UMC Location University of Amsterdam |
| Department of Surgery, Amsterdam UMC Location University of Amsterdam, Amsterdam, The Netherlands | 40 | Amsterdam UMC Location University of Amsterdam |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Affiliatie UvA | 1,313 | no institution |
| Amsterdam University | 465 | no institution |
| U. of Amsterdam | 262 | no institution |
| UvA | 195 | University Vascular Associates |
| Albert Egges van Giffen Instituut voor Prae- en Protohistorie, UvA | 164 | no institution |
| Amsterdam University Medical Center, Amsterdam, The Netherlands | 153 | Amsterdam University Medical Centers |
| Universidad de Amsterdam | 97 | no institution |
| Amsterdam Business School, U. of Amsterdam | 93 | no institution |
| Univ. Amsterdam | 61 | no institution |
| Univ. van Amsterdam (Netherlands) | 61 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
