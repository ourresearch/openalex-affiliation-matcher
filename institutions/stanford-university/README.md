# Stanford University

[OpenAlex I97018004](https://openalex.org/institutions/I97018004) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Stanford University itself): 560,639 → 585,866 (+4.5%).
- **Counting its units and predecessors** (the `lineage` filter): 611,284 → 629,701 (+3.0%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (95% of lost works); the largest share of the strings it gained moved up from one of its units (49% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Stanford University at all, about **80% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **94% do name it** or one of its units.

**13,931 strings lost Stanford University** ([removed.csv.gz](removed.csv.gz)), on 22,863 works; **39,646 strings gained it** ([added.csv.gz](added.csv.gz)), on 74,391 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 95% |
| To other institutions (mostly University of California, San Francisco, University of Pennsylvania, University of Washington) | 2% |
| To no institution | 2% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 32% |
| Up from one of its units or predecessors | 49% |
| From other institutions (mostly Stanford Health Care, Palo Alto University, Internet Society) | 19% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Stanford University Medical Center, Stanford, CA | 649 | Stanford Medicine |
| Stanford University Medical Center, Stanford, California | 306 | Stanford Medicine |
| Stanford University Medical Center, Stanford, California, USA | 155 | Stanford Medicine |
| Stanford Univ. School of Medicine (United States) | 137 | Stanford Medicine |
| Stanford University Medical Center, Stanford, CA; | 119 | Stanford Medicine |
| Stanford University Medical Center Stanford, CA | 117 | Stanford Medicine |
| [Stanford Linear Accelerator Center] | 100 | SLAC National Accelerator Laboratory |
| Division of Gastroenterology and Hepatology, Stanford University Medical Center, Palo Alto, CA, USA | 85 | Stanford Medicine |
| Department of Radiology, Stanford University Medical Center, Stanford, California | 67 | Stanford Medicine |
| Division of Gastroenterology and Hepatology, Stanford University Medical Center, Palo Alto, California, USA | 64 | Stanford Medicine |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Stanford | 2,094 | Stanford Medicine |
| Stanford Law School | 1,888 | Stanford Medicine |
| Stanford Graduate School of Business | 1,817 | no institution |
| Stanford U | 1,169 | no institution |
| Stanford Law School, 559 Nathan Abbott Way, Stanford, CA 94305-8610, United States | 878 | Stanford Medicine |
| Stanford Linear Accelerator Center, University of Stanford, Stanford, CA, USA | 794 | Stanford Synchrotron Radiation Lightsource, SLAC National Accelerator Laboratory |
| Information Systems Laboratory, University of Stanford, Stanford, CA, USA | 771 | no institution |
| Stanford Graduate School of Business, 655 Knight Way, Stanford, CA 94305-5015, United States | 758 | Stanford Medicine |
| (Stanford) | 472 | Stanford Medicine |
| Center for Integrated Systems, University of Stanford, Stanford, CA, USA | 470 | Stanford SystemX Alliance |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
