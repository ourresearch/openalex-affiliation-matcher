# Universitat Autònoma de Barcelona

[OpenAlex I123044942](https://openalex.org/institutions/I123044942) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Universitat Autònoma de Barcelona itself): 181,305 → 182,739 (+0.8%).
- **Counting its units and predecessors** (the `lineage` filter): 185,926 → 187,269 (+0.7%).
- **Why:** most of the strings it lost now go to other institutions (64% of lost works), mostly Consejo Superior de Investigaciones Científicas, Hospital de Sant Pau; most of the strings it gained were assigned to other institutions before (51% of gained works), mostly Centre de Recerca Matemàtica, Centre for Research on Ecology and Forestry Applications.

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**2,692 strings lost Universitat Autònoma de Barcelona** ([removed.csv](removed.csv)), on 3,507 works; **4,393 strings gained it** ([added.csv](added.csv)), on 5,976 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 20% |
| To other institutions (mostly Consejo Superior de Investigaciones Científicas, Hospital de Sant Pau, Centre for Research on Ecology and Forestry Applications) | 64% |
| To no institution | 16% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 42% |
| Up from one of its units or predecessors | 7% |
| From other institutions (mostly Centre de Recerca Matemàtica, Centre for Research on Ecology and Forestry Applications, Computer Vision Center) | 51% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| CNM - Centro Nacional de Microelectronica [Spain] (Campus Universidad Autónoma de Barcelona - 08193 Bellaterra, Barcelona - Spain) | 28 | Centro Nacional de Microelectrónica |
| Centre for Research in Agricultural Genomics (CRAG), CSIC-IRTA-UAB-UB, Campus UAB, Bellaterra, Barcelona, Spain | 25 | Center for Research in Agricultural Genomics |
| Division of Biology, Center for Research in Agricultural Genomics (CRAG) CSIC-IRTA-UAB-UB, Spain | 25 | Consejo Superior de Investigaciones Científicas, Center for Research in Agricultural Genomics |
| Universitat Autònoma | 24 | no institution |
| Global Ecology Unit CREAF-CSIC-UAB | 21 | Global Ecology Unit CREAF-CSIC-UAB |
| Inst. Cienc. Mater., CSIC, Univ. Auton. Barcelona, Bellaterra, E-08193 Barcelona, Spain | 21 | Consejo Superior de Investigaciones Científicas |
| Computer Vision Center, UAB, Barcelona, Spain | 20 | Computer Vision Center |
| Centre for Research in Agricultural Genomics (CRAG) CSIC-IRTA-UAB-UB, Campus UAB Bellaterra, 08193 Barcelona, Spain | 19 | Center for Research in Agricultural Genomics |
| UAB,IFAE, Barcelona | 19 | Institute for High Energy Physics |
| Centre for Research in Agricultural Genomics (CRAG) CSIC-IRTA-UAB-UB, Campus UAB Bellaterra, Barcelona, Spain | 18 | Center for Research in Agricultural Genomics |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Campus UAB | 121 | no institution |
| Port d’Informació Científica, Campus UAB | 77 | Port d'Informació Científica |
| Universitat Aut&ograve;noma de Barcelona | 52 | no institution |
| CVC - Computer Vision Center (Centre de visio per computador) (Edifici O - Campus UAB - 08193 Bellaterra (Cerdanyola) - Barcelona, Spain - S | 46 | Computer Vision Center |
| Institute of Environmental Science and Technology (ICTA-UAB) | 40 | no institution |
| Campus de la UAB | 32 | no institution |
| ICTA-UAB | 28 | no institution |
| Department of Telecommunications and Systems Engineering, Universitat Aut&#x00F2;noma de Barcelona, Barcelona, Spain | 22 | no institution |
| CSIC, Global Ecology Unit CREAF-CSIC-UAB, 08913 Bellaterra, Catalonia, Spain | 21 | Centre for Research on Ecology and Forestry Applications, Global Ecology Unit CREAF-CSIC-UAB |
| CSIC, Global Ecology Unit CREAF-CSIC-UAB, Cerdanyola del Vallès 08193, Catalonia, Spain | 20 | Centre for Research on Ecology and Forestry Applications, Global Ecology Unit CREAF-CSIC-UAB |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
