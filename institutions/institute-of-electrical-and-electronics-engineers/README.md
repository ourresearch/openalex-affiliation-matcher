# Institute of Electrical and Electronics Engineers

[OpenAlex I3132238960](https://openalex.org/institutions/I3132238960) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Institute of Electrical and Electronics Engineers itself): 11,405 → 10,390 (−8.9%).
- **Counting its units and predecessors** (the `lineage` filter): 11,661 → 10,676 (−8.4%).
- **Why:** most of the strings it lost now have no institution (65% of lost works); most of the strings it gained had no institution before (87% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Institute of Electrical and Electronics Engineers at all, about **59% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **61% do name it** or one of its units.

**2,470 strings lost Institute of Electrical and Electronics Engineers** ([removed.csv](removed.csv)), on 4,252 works; **619 strings gained it** ([added.csv](added.csv)), on 2,260 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly The University of Tokyo, The University of Osaka, IEEE France section) | 34% |
| To no institution | 65% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 87% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly American University of Nigeria, IEEE Computer Society, Potentia (Namibia)) | 13% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Senior Member, IEEE | 223 | no institution |
| Senior Member IEEE | 175 | no institution |
| Fellow, IEEE | 127 | no institution |
| @chaoss, @IEEE-NITK | 98 | no institution |
| IEEE Senior Member | 79 | no institution |
| IEEE Fellow | 71 | no institution |
| IEEE, China | 65 | no institution |
| IEEE TASSP | 52 | no institution |
| IEEE Fellow, Vermont, USA | 48 | no institution |
| IEEE Member | 46 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| IEEE | 795 | no institution |
| IEEE TMAG | 345 | no institution |
| IEEE COMM | 136 | American University of Nigeria |
| IEEE, icrob | 45 | no institution |
| IEEE History Center | 41 | no institution |
| IEEE, tmag | 27 | no institution |
| IEEE NPSS | 21 | no institution |
| IEEE TAUEL | 21 | no institution |
| IEEE member, UK | 19 | no institution |
| IEEE Potentials | 18 | Potentia (Namibia) |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
