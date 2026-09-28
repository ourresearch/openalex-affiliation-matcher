# École Polytechnique Fédérale de Lausanne

[OpenAlex I5124864](https://openalex.org/institutions/I5124864) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to École Polytechnique Fédérale de Lausanne itself): 179,090 → 160,521 (−10.4%).
- **Counting its units and predecessors** (the `lineage` filter): 180,884 → 161,551 (−10.7%).
- **Why:** most of the strings it lost now go to other institutions (95% of lost works), mostly ETH Zurich, Laboratory of Physical Chemistry; most of the strings it gained were assigned to other institutions before (56% of gained works), mostly École Normale Supérieure - PSL, École Polytechnique.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for École Polytechnique Fédérale de Lausanne at all, about **96% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **90% do name it** or one of its units.

Net, the works that really are École Polytechnique Fédérale de Lausanne's (counting its units) went up by about 0.3%.

**17,059 strings lost École Polytechnique Fédérale de Lausanne** ([removed.csv.gz](removed.csv.gz)), on 26,058 works; **2,391 strings gained it** ([added.csv](added.csv)), on 3,306 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To its parent institution | 0% |
| To other institutions (mostly ETH Zurich, Laboratory of Physical Chemistry, University of Zurich) | 95% |
| To no institution | 4% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 42% |
| Up from one of its units or predecessors | 0% |
| Down from its parent institution | 2% |
| From other institutions (mostly École Normale Supérieure - PSL, École Polytechnique, University of Lausanne) | 56% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Swiss Federal Institute of Technology | 1,211 | ETH Zurich |
| Swiss Federal Institute of Technology (Switzerland) | 527 | ETH Zurich |
| Swiss Federal Inst. of Technology,Switzerland | 471 | ETH Zurich |
| Swiss Federal Institute of Technology, Switzerland | 221 | ETH Zurich |
| Swiss Federal institute of Technology (ETH) | 133 | ETH Zurich |
| Swiss Federal Institute of Technology (ETH) | 99 | ETH Zurich |
| Institute of Toxicology, Swiss Federal Institute of Technology, Schwerzenbach | 79 | no institution |
| Swiss Federal Institute of Technology, Zu¨rich, Switzerland | 43 | ETH Zurich |
| Institute of Molecular Systems Biology, Swiss Federal Institute of Technology, Switzerland | 31 | ETH Zurich, Institute for Molecular Systems Biology |
| Swiss Federal Institute of Technology (ETH)#TAB# | 29 | ETH Zurich |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Ecole Polytech. Fed. De Lausanne, Lausanne, Switzerland | 84 | École Normale Supérieure - PSL |
| Bluebrain project, EFPL | 28 | no institution |
| Swiss Plasma Center (SPC) | 22 | no institution |
| Ecole Polytech. Fed. de Lausanne#TAB# | 16 | École Normale Supérieure - PSL |
| Ecole Polytech. Federate de Lausanne, Lausanne | 14 | École Normale Supérieure - PSL |
| Lab. d''Electromagn. et d''Acoust., Ecole Polytech. Federale de Lausanne, Switzerland | 14 | École Normale Supérieure - PSL |
| Laboratoire de Polymères, Département des Matériaux, École Polytechnique Fédérale de Laussanne, Suisse | 13 | École Polytechnique |
| Sch. of Comput. & Commun. Sci., Ecole PolyTech. Fed. de Lausanne, Lausanne | 13 | École Normale Supérieure - PSL |
| EFPL, Switzerland | 12 | no institution |
| Laboratory of Heat and Mass Transfer (LTCM), Switzerland | 12 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
