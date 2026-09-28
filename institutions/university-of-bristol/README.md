# University of Bristol

[OpenAlex I36234482](https://openalex.org/institutions/I36234482) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of Bristol itself): 225,960 → 253,739 (+12.3%).
- **Counting its units and predecessors** (the `lineage` filter): 228,071 → 254,608 (+11.6%).
- **Why:** the largest share of the strings it lost now have no institution (50% of lost works); most of the strings it gained had no institution before (59% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Bristol at all, about **32% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **95% do name it** or one of its units.

**615 strings lost University of Bristol** ([removed.csv](removed.csv)), on 747 works; **4,690 strings gained it** ([added.csv](added.csv)), on 15,433 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 3% |
| To other institutions (mostly University Of Bristol Dental Hospital, University of the West of England, BrisSynBio) | 48% |
| To no institution | 50% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 59% |
| Up from one of its units or predecessors | 1% |
| From other institutions (mostly At Bristol, National Composites Centre, University Of Bristol Dental Hospital) | 41% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| H. H. Wills Physics Laboratory , Royal Fort , Tyndall Avenue, Bristol BS8 1TL, United Kingdom | 12 | no institution |
| School of Mathematics, University Walk, Bristol BS8 1TW, U.K | 7 | no institution |
| Bristol Synthetic Biology Centre BrisSynBio, 24 Tyndall Ave, Bristol BS8 1TQ, UK | 6 | BrisSynBio |
| Long Ashton Research Station, Bristol, BS18 9AF | 6 | no institution |
| University of Bristol Dental Hospital, Bristol, UK | 6 | University Of Bristol Dental Hospital |
| University of West of England, Bristol, Faculty of Business & Law, Bristol Business School (BBS), Avon BS7 0JU, United Kingdom | 6 | University of the West of England |
| University of the West of England Bristol Business School, , Bristol, | 6 | University of the West of England |
| Bristol Vet Specialists , Bristol, | 5 | no institution |
| University of Bristol Dental Hospital | 5 | University Of Bristol Dental Hospital |
| BrisSynBio, Life Sciences Building, Tyndall Avenue, Bristol BS8 1TQ, U.K | 4 | BrisSynBio |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Bristol Doctoral College | 1,707 | no institution |
| Bristol Medical School (PHS) | 1,608 | no institution |
| Bristol Medical School (THS) | 1,142 | no institution |
| Bristol Composites Institute (ACCIS) | 772 | National Composites Centre |
| Bristol Veterinary School | 649 | At Bristol |
| Bristol Population Health Science Institute | 586 | no institution |
| The Bristol Centre for Nanoscience and Quantum Information | 409 | no institution |
| Bristol Dental School | 300 | University Of Bristol Dental Hospital |
| Bristol Glaciology Centre | 217 | At Bristol |
| Bristol Poverty Institute | 217 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
