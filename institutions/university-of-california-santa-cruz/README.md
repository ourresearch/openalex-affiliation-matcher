# University of California, Santa Cruz

[OpenAlex I185103710](https://openalex.org/institutions/I185103710) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of California, Santa Cruz itself): 81,507 → 83,449 (+2.4%).
- **Counting its units and predecessors** (the `lineage` filter): 89,546 → 86,979 (−2.9%).
- **Why:** most of the strings it lost now have no institution (56% of lost works); most of the strings it gained had no institution before (72% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of California, Santa Cruz at all, about **92% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **88% do name it** or one of its units.

**603 strings lost University of California, Santa Cruz** ([removed.csv](removed.csv)), on 928 works; **985 strings gained it** ([added.csv](added.csv)), on 3,927 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To its parent institution | 2% |
| To other institutions (mostly University of California Observatories, Universidade Estadual de Santa Cruz, Università Cattolica del Sacro Cuore) | 42% |
| To no institution | 56% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 72% |
| Down from its parent institution | 0% |
| From other institutions (mostly Genomics (United Kingdom), Institute of Particle Physics, Santa Cruz County Office of Education) | 28% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| University of California , Santa | 52 | no institution |
| Lick Observatory, Santa Cruz, Calif | 45 | no institution |
| UNIVERSIDADE ESTADUAL DE SANTA CRUZ | 43 | Universidade Estadual de Santa Cruz |
| Lick Observatory Santa Cruz, Calif., United States | 33 | no institution |
| 3University of California Observatories, 1156 High Street, Santa Cruz, CA 95064, USA | 9 | University of California Observatories |
| #N#        University of California Observatories, 1156 High Street, Santa Cruz, CA 95064, USA | 7 | University of California Observatories |
| UCO/Lick Observatories, 1156 High Street, Santa Cruz, CA 95064, USA | 7 | University of California Observatories |
| UCO/Lick Observatory, Santa Cruz | 7 | University of California Observatories |
| University of California Observatories, 1156 High Street, Sana Cruz, CA 95065, USA | 7 | University of California Observatories |
| UCO/Lick Observatory, Santa Cruz, CA 95064, USA | 6 | University of California Observatories |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| UCSC | 844 | no institution |
| UCSC Genomics Institute & Nimbus Informatics, LLC | 334 | no institution |
| UCSC Genomics Institute | 329 | Genomics (United Kingdom) |
| Santa Cruz Institute for Particle Physics, Santa Cruz, CA 95064, USA | 256 | no institution |
| UC Santa | 238 | no institution |
| @UCSantaCruzComputationalGenomicsLab | 152 | no institution |
| Santa Cruz Institute for Particle Physics | 138 | Institute of Particle Physics |
| Santa Cruz Institute for Particle Physics, Santa Cruz, California 95064, USA | 81 | no institution |
| Santa Cruz Institute for Particle Physics , Santa Cruz, CA 95064, USA | 59 | no institution |
| U California, Dept of Psychology, Santa Cruz, CA, US | 34 | California Department of Education |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
