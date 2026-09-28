# William & Mary

[OpenAlex I16285277](https://openalex.org/institutions/I16285277) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to William & Mary itself): 38,452 → 37,484 (−2.5%).
- **Counting its units and predecessors** (the `lineage` filter): 38,452 → 37,484 (−2.5%).
- **Why:** most of the strings it lost now go to other institutions (94% of lost works), mostly Virginia Institute of Marine Science, Marquette University; most of the strings it gained had no institution before (51% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for William & Mary at all, about **10% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **98% do name it** or one of its units.

Net, the works that really are William & Mary's (counting its units) went down by about 2.2%.

**1,423 strings lost William & Mary** ([removed.csv](removed.csv)), on 2,053 works; **362 strings gained it** ([added.csv](added.csv)), on 557 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly Virginia Institute of Marine Science, Marquette University, National Oceanic and Atmospheric Administration) | 94% |
| To no institution | 6% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 51% |
| From other institutions (mostly Virginia Institute of Marine Science, George Mason University, Virginia Sea Grant) | 49% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| NOAA National Systematics Laboratory, National Museum of Natural History, Smithsonian Institution, Washington, D. C. 20560, U. S. A. & Depar | 9 | Virginia Institute of Marine Science, Smithsonian Institution, National Oceanic and Atmospheric Administration, National Museum of Natural History, NOAA National Systematics Laboratory |
| School of Marine Science, Virginia Institute of Marine Science, College of William and Mary, Gloucester Point, Virginia 23062, USA | 9 | Virginia Institute of Marine Science |
| Virginia Institute of Marine Science School of Marine Science, College of William and Mary, 23062, Gloucester Point, Virginia | 9 | Virginia Institute of Marine Science |
| Virginia Institute of Marine Science and College of William and Mary, Gloucester Pt., VA 23062, USA jacque. h. carter @ gmail. com; https: / | 9 | Virginia Institute of Marine Science |
| College of William and Mary, Virginia Institute of Marine Science, Gloucester Point, VA, 23062, USA | 8 | Virginia Institute of Marine Science |
| Department of Physical Sciences, Virginia Institute of Marine Science, School of Marine Science, College of William and Mary, Gloucester Poi | 8 | Virginia Institute of Marine Science |
| Dept. Physical Science, Virginia Institute of Marine Sciences The College of William &amp; Mary  Gloucester Point VA USA | 8 | Virginia Institute of Marine Science |
| Mason School of Business, Williamsburg, VA, USA | 8 | no institution |
| School of Marine Science , Virginia Institute of Marine Science , College of William and Mary , Gloucester Point , Virginia 23062 , USA | 8 | Virginia Institute of Marine Science |
| School of Marine Science, Virginia Institute of Marine Science, College of William and Mary, Gloucester Point, Virginia 23062 | 8 | Virginia Institute of Marine Science |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| College of William | 42 | no institution |
| Virginia Institute of Marine Science, College of William and Mary, Gloucester Point,,USA | 24 | Virginia Institute of Marine Science |
| Virginia Institute of Marine Science , School of Marine Science College of William and Mary , Gloucester Point, Virginia, 23062, USA | 23 | Virginia Institute of Marine Science |
| Virginia Institute of Marine Science, William &amp; Mary  Gloucester Point Virginia USA | 20 | no institution |
| - Mason School of Business | 14 | George Mason University |
| Virginia Institute of Marine Science, School of Marine Science College of William and Mary Gloucester Point Virginia USA | 11 | Virginia Institute of Marine Science |
| College of William and Mary Virginia Institute of Marine Science Virginia USA | 8 | Virginia Institute of Marine Science |
| Department of School Psychology and Counselor Education College of William &amp; Mary | 8 | no institution |
| The College of William | 7 | no institution |
| Department of Economics College of William and Mary | 6 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
