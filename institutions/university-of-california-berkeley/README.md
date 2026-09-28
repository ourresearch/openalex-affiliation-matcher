# University of California, Berkeley

[OpenAlex I95457486](https://openalex.org/institutions/I95457486) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to University of California, Berkeley itself): 500,772 → 508,609 (+1.6%).
- **Counting its units and predecessors** (the `lineage` filter): 519,789 → 518,579 (−0.2%).
- **Why:** most of the strings it lost now have no institution (58% of lost works); most of the strings it gained were assigned to other institutions before (52% of gained works), mostly Lawrence Berkeley National Laboratory, Museum of Vertebrate Zoology.

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**3,238 strings lost University of California, Berkeley** ([removed.csv](removed.csv)), on 8,291 works; **15,263 strings gained it** ([added.csv.gz](added.csv.gz)), on 24,070 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 1% |
| To its parent institution | 28% |
| To other institutions (mostly University of California, San Francisco, Lawrence Berkeley National Laboratory, University of California, Davis) | 13% |
| To no institution | 58% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 42% |
| Up from one of its units or predecessors | 5% |
| Down from its parent institution | 1% |
| From other institutions (mostly Lawrence Berkeley National Laboratory, Museum of Vertebrate Zoology, Berkeley College) | 52% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Berkeley, California | 1,053 | no institution |
| University of California , , , , | 857 | no institution |
| university of california, United States | 497 | University of California System |
| Department of Chemistry, University of California | 265 | no institution |
| Berkeley, California, USA | 208 | no institution |
| Berkeley , California | 107 | no institution |
| Department of Physics, University of California, USA | 91 | no institution |
| Department of Chemistry and Biochemistry, University of California | 83 | no institution |
| California, University La Jolla, Calif., United States | 70 | no institution |
| Department of Psychology, University of California, USA | 51 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| California Univ. Berkeley, CA, United States | 767 | no institution |
| University of California Berkley | 388 | no institution |
| Berkeley Institute for Data Science | 207 | no institution |
| Berkeley, Cal | 172 | Berkeley College |
| Dep. Chem., Lawrence Berkeley Lab., Univ. Calif., Berkeley, CA 94720, USA | 137 | Lawrence Berkeley National Laboratory |
| U.C. BERKELEY | 132 | no institution |
| UCB#TAB# | 107 | no institution |
| University of California - Haas School of Business | 94 | no institution |
| U California - Berkeley, CA, US | 92 | no institution |
| U California, Dept of Psychology, Berkeley, CA, US | 88 | California Department of Education |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
