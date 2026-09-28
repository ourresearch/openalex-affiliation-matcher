# Delft University of Technology

[OpenAlex I98358874](https://openalex.org/institutions/I98358874) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Delft University of Technology itself): 181,763 → 184,554 (+1.5%).
- **Counting its units and predecessors** (the `lineage` filter): 181,812 → 184,663 (+1.6%).
- **Why:** most of the strings it lost now have no institution (90% of lost works); most of the strings it gained had no institution before (75% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**997 strings lost Delft University of Technology** ([removed.csv](removed.csv)), on 2,323 works; **3,772 strings gained it** ([added.csv](added.csv)), on 6,498 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Netherlands Organisation for Applied Scientific Research, The Hague University of Applied Sciences, Erasmus MC) | 10% |
| To no institution | 90% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 75% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly Munich University of Applied Sciences, VSL National Metrology Institute, J.M. Burgerscentrum) | 25% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Delft | 419 | no institution |
| Delft, The Netherlands | 260 | no institution |
| Delft , | 122 | no institution |
| Delft, Holland | 75 | no institution |
| Delft, | 47 | no institution |
| CE Delft | 26 | no institution |
| Delft , The Netherlands | 24 | no institution |
| DELFT, The Netherlands | 22 | no institution |
| Delft, the Netherlands | 21 | no institution |
| Delft The Netherlands | 19 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Interuniversity Reactor Institute 2629 JB Delft, The Netherlands | 468 | no institution |
| TUDelft | 120 | no institution |
| Technical University Delft | 117 | no institution |
| @Deltares @TUDelft3d | 68 | Deltares |
| I.T.C., Delft, Netherlands | 50 | no institution |
| @AlgTUDelft | 47 | no institution |
| Delft Hydraulics Laboratory, Delft, The Netherlands | 36 | no institution |
| Laboratorium voor Technische Physica der Technische Hogeschool, Delft | 33 | no institution |
| TuDelft | 33 | no institution |
| Delft Institute of Applied Mathematics | 30 | Institute of Applied Mathematics |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
