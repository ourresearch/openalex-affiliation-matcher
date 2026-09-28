# The Open University

[OpenAlex I204136569](https://openalex.org/institutions/I204136569) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to The Open University itself): 55,035 → 59,241 (+7.6%).
- **Counting its units and predecessors** (the `lineage` filter): 55,035 → 59,241 (+7.6%).
- **Why:** most of the strings it lost now go to other institutions (79% of lost works), mostly Open University of the Netherlands, San Raffaele University of Rome; most of the strings it gained had no institution before (79% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for The Open University at all, about **81% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **98% do name it** or one of its units.

Net, the works that really are The Open University's (counting its units) went up by about 9.3%.

**738 strings lost The Open University** ([removed.csv](removed.csv)), on 1,455 works; **1,605 strings gained it** ([added.csv](added.csv)), on 6,606 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly Open University of the Netherlands, San Raffaele University of Rome, Open University of Israel) | 79% |
| To no institution | 21% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 79% |
| From other institutions (mostly Universidade Aberta, Open Knowledge (United Kingdom), The Open Group) | 21% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| (Open University of the Netherlands.) | 290 | Open University of the Netherlands |
| The Open University of Hong Kong | 45 | Hong Kong Metropolitan University |
| Wyższa Szkoła Zarządzania – Polish Open University | 45 | Polish Open University |
| Shanghai Open University | 31 | Shanghai Open University |
| Moscow State Open Univ., Russia | 29 | Moscow State Open University |
| Department of Human Sciences and Quality of Life Promotion, San Raffaele Roma Open University, 00166 Rome, Italy | 25 | San Raffaele University of Rome |
| Department of Human Sciences and Promotion of the Quality of Life, San Raffaele Roma Open University | 20 | San Raffaele University of Rome |
| Educational Technology Expertise Center, Open University of The Netherlands, Heerlen, The Netherlands#TAB# | 14 | Open University of the Netherlands |
| Faculty of Psychology and Educational Sciences; Open University of the Netherlands; Heerlen the Netherlands | 13 | Open University of the Netherlands |
| [Open University of the Netherlands, Heerlen, Netherlands] | 12 | Open University of the Netherlands |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Open University | 3,751 | no institution |
| Open University  >  >  >  > | 527 | Universidade Aberta |
| The Open U | 35 | The Open Group |
| Qualified nurse, academic lawyer and senior lecturer, Open University | 29 | no institution |
| Department of Biological Sciences (Milton Keynes MK7 6AA - United Kingdom) | 25 | no institution |
| Knowledge Media Institute, Open University, UK | 25 | Open Knowledge (United Kingdom) |
| School of Physical Sciences [Milton Keynes] | 22 | no institution |
| Institute of Educational Technology, Open University, UK | 20 | no institution |
| School of Education, Open University | 19 | no institution |
| Associate Lecturer, Open University | 18 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
