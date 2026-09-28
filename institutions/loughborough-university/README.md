# Loughborough University

[OpenAlex I143804889](https://openalex.org/institutions/I143804889) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Loughborough University itself): 94,183 → 90,393 (−4.0%).
- **Counting its units and predecessors** (the `lineage` filter): 99,706 → 94,982 (−4.7%).
- **Why:** most of the strings it lost now go to other institutions (72% of lost works), mostly University of Nottingham, AstraZeneca (United Kingdom); most of the strings it gained had no institution before (59% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Loughborough University at all, about **98% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **89% do name it** or one of its units.

**4,454 strings lost Loughborough University** ([removed.csv](removed.csv)), on 6,086 works; **733 strings gained it** ([added.csv](added.csv)), on 1,360 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly University of Nottingham, AstraZeneca (United Kingdom), University of Oxford) | 72% |
| To no institution | 28% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 59% |
| Up from one of its units or predecessors | 3% |
| From other institutions (mostly Loughborough College, British University in Egypt, English Institute of Sport) | 38% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| School of Biosciences, University of Nottingham, Sutton Bonington Campus, Loughborough, Leicestershire LE12 5RD, UK | 61 | University of Nottingham |
| School of Biosciences, University of Nottingham, Sutton Bonington Campus, Loughborough, Leicestershire, LE12 5RD, UK | 47 | University of Nottingham |
| Alliance for a Sustainable Amazon, Potomac, MD, USA & School of Biosciences, University of Nottingham, Sutton Bonington Campus, Nr Loughboro | 42 | University of Nottingham |
| School of Biosciences , University of Nottingham , Sutton Bonington Campus, Loughborough, Leicestershire, LE12 5RD, UK | 34 | University of Nottingham |
| AstraZeneca R&D Charnwood, Bakewell Road, Loughborough LE11 5RH, UK | 29 | no institution |
| AstraZeneca R&D Charnwood, Loughborough, UK | 28 | no institution |
| Alliance for a Sustainable Amazon, Potomac, MD, USA & School of Biosciences, University of Nottingham, Sutton Bonington Campus, Nr Loughboro | 27 | University of Nottingham |
| AstraZeneca R&D Charnwood , Loughborough, UK | 23 | no institution |
| Dep. Med. Chem., AstraZeneca R&D Charnwood, Loughborough, Leicestershire LE11 5RH, UK | 17 | AstraZeneca (United Kingdom) |
| AstraZeneca R&D Charnwood, Loughborough, Leicestershire LE11 5RH, UK | 16 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Loughborough | 209 | no institution |
| Loughborough University - The British University in Egypt | 47 | British University in Egypt |
| Department of Electronic and Electrical Engineering [Loughborough] | 39 | no institution |
| Loughborough Business School | 38 | Loughborough College |
| #N#        Loughborough#N# | 22 | Loughborough College |
| Department of Management StudiesLoughborough University of Technology | 17 | no institution |
| Loughborough Grammar School | 14 | Grammar School |
| Loughborough U., School of Business and Economics | 14 | Loughborough College |
| Department of Chemical Engineering University of Technology Loughborough Leicestershire England | 13 | no institution |
| Department of Electronic and Electrical Engineering, Lougborough University of Technology, UK | 11 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
