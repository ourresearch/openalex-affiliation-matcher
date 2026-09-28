# ETH Zurich

[OpenAlex I35440088](https://openalex.org/institutions/I35440088) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to ETH Zurich itself): 261,778 → 308,280 (+17.8%).
- **Counting its units and predecessors** (the `lineage` filter): 276,345 → 324,717 (+17.5%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (51% of lost works); the largest share of the strings it gained had no institution before (37% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for ETH Zurich at all, about **71% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **85% do name it** or one of its units.

**1,458 strings lost ETH Zurich** ([removed.csv](removed.csv)), on 2,083 works; **39,426 strings gained it** ([added.csv.gz](added.csv.gz)), on 76,661 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 51% |
| To its parent institution | 0% |
| To other institutions (mostly University of Zurich, Paul Scherrer Institute, ETH Zürich Foundation) | 22% |
| To no institution | 27% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 37% |
| Up from one of its units or predecessors | 20% |
| Down from its parent institution | 9% |
| From other institutions (mostly École Polytechnique Fédérale de Lausanne, Analytisches Laboratorium, University of Zurich) | 34% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Laboratorium für Festkörperphysik, ETHZ, CH-8093 Zürich, Switzerland | 42 | Laboratory for Solid State Physics |
| Institute for Theoretical Physics, ETH, CH-8093, Zürich, Switzerland | 41 | Institute for Theoretical Physics |
| Theoretical Physics, ETH-Hönggerberg, CH-8093, Zürich, Switzerland | 34 | no institution |
| ETHZ; | 28 | no institution |
| ETH Zürich Foundation | 23 | ETH Zürich Foundation |
| Laboratory for Neutron Scattering, ETHZ & PSI, CH-5232 Villigen,#N#Switzerland | 22 | Paul Scherrer Institute |
| Physical Electronics Laboratory, Zurich, Switzerland | 18 | no institution |
| ETH Zurich Foundation | 13 | ETH Zürich Foundation |
| Geologisches Institut der ETH, ETH Zentrum, 8092, Zürich, Schweiz | 11 | Geological Institute |
| Geologisches Institut, ETH-Zentrum, CH-8092, Zürich, Switzerland | 11 | Geological Institute |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Swiss Federal Institute of Technology | 1,211 | École Polytechnique Fédérale de Lausanne |
| Swiss Federal Institute of Technology, Zurich, Switzerland | 945 | no institution |
| ETH | 836 | no institution |
| Organisch-chemisches Laboratorium der Eidg. Technischen Hochschule, Zürich | 802 | Analytisches Laboratorium |
| Swiss Federal Institute of Technology Zurich | 754 | no institution |
| Organisch‐chemisches Laboratorium der Eidg. Technischen Hochschule, Zürich | 678 | Analytisches Laboratorium |
| Swiss Federal Institute of Technology, Zürich, Switzerland | 577 | no institution |
| Swiss Federal Institute of Technology (Switzerland) | 527 | École Polytechnique Fédérale de Lausanne |
| Swiss Federal Institute of Technology, Zürich | 500 | no institution |
| ETHZ | 484 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
