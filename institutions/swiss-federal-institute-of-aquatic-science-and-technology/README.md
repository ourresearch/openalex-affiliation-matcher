# Swiss Federal Institute of Aquatic Science and Technology

[OpenAlex I63664421](https://openalex.org/institutions/I63664421) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Swiss Federal Institute of Aquatic Science and Technology itself): 16,509 → 16,081 (−2.6%).
- **Counting its units and predecessors** (the `lineage` filter): 16,509 → 16,383 (−0.8%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (52% of lost works); the largest share of the strings it gained had no institution before (49% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Swiss Federal Institute of Aquatic Science and Technology at all, about **9% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **85% do name it** or one of its units.

**484 strings lost Swiss Federal Institute of Aquatic Science and Technology** ([removed.csv](removed.csv)), on 836 works; **174 strings gained it** ([added.csv](added.csv)), on 229 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 52% |
| To its parent institution | 0% |
| To other institutions (mostly ETH Zurich, University of Bern, École Polytechnique Fédérale de Lausanne) | 17% |
| To no institution | 31% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 49% |
| Down from its parent institution | 4% |
| From other institutions (mostly ETH Zurich, Bundesamt für Wasserwirtschaft, École Polytechnique Fédérale de Lausanne) | 47% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Lib4RI - Library for the Research Institutes within the ETH Domain: Eawag, Empa, PSI & WSL | 158 | Paul Scherrer Institute, Lib4RI - Library for the Research Institutes within the ETH Domain: Eawag, Empa, PSI & WSL |
| Lib4RI - Library for the Research Institutes within the ETH Domain: Eawag, Empa, PSI & WSL (Dübendorf, Switzerland) | 16 | Lib4RI - Library for the Research Institutes within the ETH Domain: Eawag, Empa, PSI & WSL |
| Swiss Centre for Applied Ecotoxicology Eawag-EPFL, 8600 Dübendorf, Switzerland | 15 | École Polytechnique Fédérale de Lausanne, Swiss Centre for Applied Ecotoxicology |
| Swiss Centre for Applied Ecotoxicology Eawag-EPFL, Dübendorf, Switzerland | 11 | École Polytechnique Fédérale de Lausanne, Swiss Centre for Applied Ecotoxicology |
| Surface Waters - Research and Management, Swiss Federal Institute of Technology,  Zurich, Kastanienbaum, Switzerland | 10 | ETH Zurich |
| Swiss Center for Applied Ecotoxicology (Ecotox Center), EPFL ENAC IIE-GE, 1015 Lausanne, Switzerland | 9 | École Polytechnique Fédérale de Lausanne |
| Swiss Centre for Applied Ecotoxicology (Ecotox Centre), EPFL ENAC IIE-GE, 1015 Lausanne, Switzerland | 7 | École Polytechnique Fédérale de Lausanne, Swiss Centre for Applied Ecotoxicology |
| Swiss Centre for Applied Ecotoxicology Dübendorf Switzerland | 7 | Swiss Centre for Applied Ecotoxicology |
| Swiss Centre for Applied Ecotoxicology Eawag-EPFL, Überlandstrasse 133, 8600 Dübendorf, Switzerland | 7 | École Polytechnique Fédérale de Lausanne, Swiss Centre for Applied Ecotoxicology |
| Swiss Centre for Applied Ecotoxicology Eawag-EPFL Dübendorf; Switzerland | 6 | École Polytechnique Fédérale de Lausanne, Swiss Centre for Applied Ecotoxicology |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Eidg. Anstalt für Wasserversorgung, Abwasserreinigung und Gewässerschutz an der Eidg. Technischen Hochschule, Zürich | 14 | Bundesamt für Wasserwirtschaft |
| Eidgenössische Anstalt für Wasserversorgung | 10 | no institution |
| Eidg. Anstalt für Wasserversorgung, Abwasserreinigung und Gewässerschutz an der ETH, Zürich | 6 | Bundesamt für Wasserwirtschaft, ETH Zurich |
| Eidg. Anstalt für Wasserversorgung, Abwasserreinigung und Gewässerschutz an der Eidgenössischen Technischen Hochschule, Zürich | 4 | no institution |
| Eidg. Anstalt für Wasserversorgung, Abwasserreinigung und Gewässerschutz an der Eidg. Technischen Hochschule, Zürich, | 3 | Bundesamt für Wasserwirtschaft |
| Eidg. Anstalt für Wasserversorgung, Abwasserreinigung und Gewässerschutz an, der ETH, Zürich, | 3 | ETH Zurich |
| Eidgenössischen Anstalt für Wasserversorgung, Abwasserreinigung und Gewässerschutz an der Eidgenössischen Technischen Hochschule, Zürich | 3 | Board of the Swiss Federal Institutes of Technology |
| Institute of Aquatic Sciences Swiss Federal Institute of Technology (Zürich) CH‐8600 Dübendorf, Switzerland | 3 | ETH Zurich |
| Swiss Federal Institute for Water Resources and Water Pollution Control, CH-8600 Dübendorf, Switzerland | 3 | no institution |
| EWAG Energie- und Wasserversorgung AG und VAG Verkehrs-AG | 2 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
