# University of California, Riverside

[OpenAlex I103635307](https://openalex.org/institutions/I103635307) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of California, Riverside itself): 110,665 → 110,596 (−0.1%).
- **Counting its units and predecessors** (the `lineage` filter): 110,665 → 110,904 (+0.2%).
- **Why:** most of the strings it lost now have no institution (62% of lost works); most of the strings it gained had no institution before (74% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**464 strings lost University of California, Riverside** ([removed.csv](removed.csv)), on 928 works; **595 strings gained it** ([added.csv](added.csv)), on 1,048 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 17% |
| To its parent institution | 1% |
| To other institutions (mostly La Sierra University, University of California, Los Angeles, United States Department of Agriculture) | 20% |
| To no institution | 62% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 74% |
| Down from its parent institution | 1% |
| From other institutions (mostly California Department of Education, University of California, Berkeley, Institute of Geophysics) | 26% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Riverside, California | 111 | no institution |
| Riverside, Calif | 36 | no institution |
| University of California, Citrus Experiment Station, Riverside, California | 32 | Citrus Research Center and Agricultural Experiment Station |
| Riverside, California, USA | 28 | no institution |
| Riverside, CA USA | 26 | no institution |
| University of California, Citrus Experiment Station, Riverside | 25 | Citrus Research Center and Agricultural Experiment Station |
| Department of Biological Control, University of California Citrus Experiment Station, Riverside | 22 | Citrus Research Center and Agricultural Experiment Station |
| Department of Biology, LaSierra University, Riverside, CA, USA | 22 | La Sierra University |
| Consultant,         Riverside, California, USA | 15 | no institution |
| University of California Citrus Experiment Station, Riverside, Calif | 15 | Citrus Research Center and Agricultural Experiment Station |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| UCR | 176 | no institution |
| Lee Kong Chian Natural History Museum, Department of Biological Sciences, National University of Singapore, 117377, Singapore. & Department  | 87 | no institution |
| Lee Kong Chian Natural History Museum, Department of Biological Sciences, National University of Singapore, 117377, Singapore. & Department  | 40 | no institution |
| U California, Dept of Psychology, Riverside, CA, US | 31 | California Department of Education |
| U California, School of Education, Riverside, CA, US | 11 | California Department of Education |
| U California, School of Education, Riverside, US | 11 | no institution |
| University of California Fullerton, Riverside, CA, USA | 9 | no institution |
| (UCR) | 6 | no institution |
| CBio3 Laboratory, School of Chemistry, UCR | 6 | no institution |
| UNED-UCR | 6 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
