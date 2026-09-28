# Statistics Denmark

[OpenAlex I1320355602](https://openalex.org/institutions/I1320355602) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Statistics Denmark itself): 1,134 → 444 (−60.8%).
- **Counting its units and predecessors** (the `lineage` filter): 1,134 → 444 (−60.8%).
- **Why:** most of the strings it lost now go to other institutions (73% of lost works), mostly University of Copenhagen, Danish National Metrology Institute; most of the strings it gained had no institution before (100% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Statistics Denmark at all, about **96% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **33% do name it** or one of its units.

**503 strings lost Statistics Denmark** ([removed.csv](removed.csv)), on 789 works; **6 strings gained it** ([added.csv](added.csv)), on 6 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly University of Copenhagen, Danish National Metrology Institute, Peking University) | 73% |
| To no institution | 27% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 100% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Statistical Research Unit, University of Copenhagen, Denmark | 39 | University of Copenhagen |
| Statistical Research Unit, University of Copenhagen, Copenhagen, Denmark | 32 | University of Copenhagen |
| Danish Fundamental Metrology, Matematiktorvet 307, DK-2800 Kgs. Lyngby, Denmark | 19 | Danish National Metrology Institute |
| Institute of Mathematical Statistics, University of Copenhagen, 5 Universitetsparken, DK-2100, Copenhagen Ø, Denmark | 14 | University of Copenhagen |
| Institute of Mathematical Statistics, University of Copenhagen, Copenhagen Ø, Denmark | 12 | University of Copenhagen |
| Institute of Mathematical Statistics , University of Copenhagen , Copenhagen , Denmark | 11 | University of Copenhagen |
| Institute of Mathematical Statistics, University of Copenhagen, Copenhagen, Denmark | 9 | University of Copenhagen |
| Institute of Statistics, University of Copenhagen, Denmark | 9 | University of Copenhagen |
| Institute of Statistics, University of Copenhagen, Copenhagen K, Denmark | 8 | University of Copenhagen |
| Institute of Statistics, University of Copenhagen, Copenhagen, Denmark | 8 | University of Copenhagen |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| (Oberregierungsrat im Dänischen Statistischen Departement, Kopenhagen) | 1 | no institution |
| 1Direktor des statistischen Bureaus der Stadt Kopenhagen | 1 | no institution |
| 1Direktor des städtischen statistischen Bureaus in Kopenhagen | 1 | no institution |
| Dansk Data , Denmark | 1 | no institution |
| Dansk Data, Denmark | 1 | no institution |
| Oberregierungsrat im Dänischen Statistischen Departement, Kopenhagen | 1 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
