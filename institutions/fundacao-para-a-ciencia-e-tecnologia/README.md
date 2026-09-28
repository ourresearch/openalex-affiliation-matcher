# Fundação para a Ciência e Tecnologia

[OpenAlex I7883018](https://openalex.org/institutions/I7883018) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Fundação para a Ciência e Tecnologia itself): 3,833 → 1,746 (−54.4%).
- **Counting its units and predecessors** (the `lineage` filter): 7,398 → 3,904 (−47.2%).
- **Why:** most of the strings it lost now go to other institutions (80% of lost works), mostly University of Lisbon, Universidade Nova de Lisboa; most of the strings it gained had no institution before (54% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Fundação para a Ciência e Tecnologia at all, about **94% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **31% do name it** or one of its units.

**1,790 strings lost Fundação para a Ciência e Tecnologia** ([removed.csv](removed.csv)), on 2,778 works; **367 strings gained it** ([added.csv](added.csv)), on 480 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To its parent institution | 0% |
| To other institutions (mostly University of Lisbon, Universidade Nova de Lisboa, University of Algarve) | 80% |
| To no institution | 20% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 54% |
| From other institutions (mostly Universidade Nova de Lisboa, University of Lisbon, Fundação de Ciência e Tecnologia) | 46% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| FCT/UNESP | 171 | Universidade Estadual Paulista (Unesp) |
| FCT/UNESP, Presidente Prudente | 61 | Universidade Estadual Paulista (Unesp) |
| FCT | 42 | no institution |
| Laboratório para a Ciência da Computação e Informática | 41 | Laboratório para a Ciência da Computação e Informática |
| FCT/UNL | 39 | no institution |
| FCT I FCCN | 33 | no institution |
| Centro de Matemática e Aplicações (CMA), FCT, UNL, Portugal | 23 | Universidade Nova de Lisboa, Centro de Matemática e Aplicações |
| Fundo Regional para a Ciência e Tecnologia | 20 | Fundo Regional para a Ciência e Tecnologia |
| FCT  | 18 | no institution |
| FCT, Universidade Nova de Lisboa | 17 | Universidade Nova de Lisboa |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Fundação de Ciência e Tecnologia | 15 | Fundação de Ciência e Tecnologia |
| 8GQP-CG, Grupo Quaternário e Pré- História do Centro de Geociências (uIandD 73 e FCT), Mação, Portugal | 9 | no institution |
| DEE, FCT, Universidade Nova de Lisboa, Portugal | 7 | Universidade Nova de Lisboa |
| Lab. Eng. Bioq., FCT/UNL, 2825, Monte da Caparica, Portugal | 7 | no institution |
| CITI, Departamento de Informática, FCT, Universidade Nova de Lisboa, Portugal | 6 | Universidade Nova de Lisboa |
| DEE, FCT-UNL, Portugal | 5 | no institution |
| FCT/UNL, P-2829-516 Caparica, Portugal | 5 | no institution |
| Lab. Eng. Bioq., FCT/UNL, 2825 Monte da Caparica, Portugal | 5 | no institution |
| Laboratório de Engenharia Bioquímica, FCT/UNL, P-2825 Monte da Caparica, Portugal | 4 | no institution |
| CENTRA and Department of Physics, FCT, University of the Algarve, Campus de Gambelas, 8005-139 Faro, Portugal | 3 | University of Algarve |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
