# Leeds Beckett University

[OpenAlex I84027002](https://openalex.org/institutions/I84027002) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Leeds Beckett University itself): 18,033 → 17,411 (−3.4%).
- **Counting its units and predecessors** (the `lineage` filter): 18,033 → 17,411 (−3.4%).
- **Why:** most of the strings it lost now go to other institutions (84% of lost works), mostly University of Leeds, Leeds Teaching Hospitals NHS Trust; most of the strings it gained had no institution before (76% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Leeds Beckett University at all, about **92% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **95% do name it** or one of its units.

**748 strings lost Leeds Beckett University** ([removed.csv](removed.csv)), on 876 works; **149 strings gained it** ([added.csv](added.csv)), on 213 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly University of Leeds, Leeds Teaching Hospitals NHS Trust, Carnegie Mellon University) | 84% |
| To no institution | 16% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 76% |
| From other institutions (mostly University of Leeds, Linton University College, Carrick Institute) | 24% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Department of Pure and Applied Biology, University of Leeds, Leeds, U.K | 8 | University of Leeds |
| University of Leeds and NIHR Leeds Biomedical Research Centre  Leeds UK | 7 | University of Leeds |
| Centre for Computational Imaging and Simulation Technologies in Biomedicine (CISTIB), School of Computing, University of Leeds, Leeds, UK; B | 6 | University of Leeds |
| Department of Linguistics and Phonetics, University of Leeds Leeds, UK | 6 | University of Leeds |
| Leeds U.K | 6 | no institution |
| Beckett Street | 5 | no institution |
| Carnegie Applied Rugby Research (CARR) Centre, Carnegie School of Sport, Leeds, UK | 5 | no institution |
| Center for Sport and Exercise Sciences, University of Leeds | 4 | University of Leeds |
| Centre for Technical Textiles, University of Leeds, Leeds LS2 9JT, UK | 4 | University of Leeds |
| Centre for Technical Textiles, University of Leeds, Leeds, LS2 9 JT (UK) | 4 | University of Leeds |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| School of Clinical and Applied Sciences, Leeds Becket University, Leeds, UK | 24 | no institution |
| School of Clinical and Applied Sciences, Leeds Becket University, Leeds, United Kingdom | 7 | no institution |
| School of Health, Leeds Becket University, Leeds, UK | 6 | no institution |
| Leeds Becket University | 5 | no institution |
| Leeds Metropoletan (Beckett) University Computing and Creative Technologies, Leeds, UK | 5 | no institution |
| Leeds Polytech., UK | 5 | no institution |
| Leeds Becket University, Leeds, UK | 3 | no institution |
| Ph.D Research student, Leedsbeckett University, Leeds United Kingdom | 3 | University of Leeds |
| School of Health, Leeds Becket University, Leeds, United Kingdom | 3 | no institution |
| Business School, Leeds Bechett University, Leeds, United Kingdom | 2 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
