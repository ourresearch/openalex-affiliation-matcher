# University Hospitals Sussex NHS Foundation Trust

[OpenAlex I4210151332](https://openalex.org/institutions/I4210151332) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University Hospitals Sussex NHS Foundation Trust itself): 7,651 → 4,822 (−37.0%).
- **Counting its units and predecessors** (the `lineage` filter): 14,555 → 13,051 (−10.3%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (92% of lost works); the largest share of the strings it gained moved up from one of its units (47% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University Hospitals Sussex NHS Foundation Trust at all, about **76% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **98% do name it** or one of its units.

Net, the works that really are University Hospitals Sussex NHS Foundation Trust's (counting its units) went up by about 1.8%.

**2,275 strings lost University Hospitals Sussex NHS Foundation Trust** ([removed.csv](removed.csv)), on 4,097 works; **226 strings gained it** ([added.csv](added.csv)), on 270 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 92% |
| To other institutions (mostly National Health Service, West Suffolk NHS Foundation Trust, Brighton and Sussex Medical School) | 2% |
| To no institution | 6% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 38% |
| Up from one of its units or predecessors | 47% |
| From other institutions (mostly University of Sussex, East Sussex County Council, Sussex County Community College) | 16% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Brighton and Sussex University Hospitals NHS Trust, Brighton, UK | 333 | Brighton and Sussex University Hospitals NHS Trust |
| Brighton and Sussex University Hospitals NHS Trust | 189 | Brighton and Sussex University Hospitals NHS Trust |
| Brighton and Sussex University Hospitals’ NHS Trust | 178 | Brighton and Sussex University Hospitals NHS Trust |
| Brighton and Sussex University Hospitals NHS Trust, Brighton, United Kingdom | 66 | Brighton and Sussex University Hospitals NHS Trust |
| Brighton and Sussex University Hospitals NHS Trust, UK | 60 | Brighton and Sussex University Hospitals NHS Trust |
| Brighton and Sussex University Hospitals, NHS Trust, Brighton, UK | 46 | Brighton and Sussex University Hospitals NHS Trust |
| Brighton & Sussex University Hospitals NHS Trust, Brighton, UK | 38 | Brighton and Sussex University Hospitals NHS Trust |
| Brighton and Sussex University Hospitals | 33 | Brighton and Sussex University Hospitals NHS Trust |
| Sussex Cardiac Centre, Brighton and Sussex University Hospitals NHS Trust, Brighton, UK | 27 | Brighton and Sussex University Hospitals NHS Trust |
| Brighton and Sussex University Hospitals NHS Trust Brighton UK | 25 | Brighton and Sussex University Hospitals NHS Trust |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Sussex Cardiac Centre, University Hospitals Sussex, Brighton, United Kingdom | 16 | no institution |
| Sussex Cardiac Centre, University Hospitals Sussex, Brighton, UK | 5 | no institution |
| University Hospital Sussex, Brighton, UK | 5 | no institution |
| University Hospital Sussex | 4 | no institution |
| Brighton &amp; Sussex University Hospitals, Brighton, UK | 3 | no institution |
| Princess Royal Hospital, Brighton, UK | 3 | Princess Royal Hospital |
| Department of Biochemistry, Royal Sussex Country Hospital, Eastern Road, Brighton, Sussex BN2 5BE Great Britain | 2 | Royal Sussex County Hospital |
| Department of Emergency Medicine , Royal Sussex County Hospital , University Hospitals Sussex , Eastern Road , Brighton BN2 5BE , UK | 2 | Royal Sussex County Hospital |
| Department of Emergency Medicine, Royal Sussex County Hospital, University Hospitals Sussex, Eastern Road, Brighton BN2 5BE, UK; | 2 | Royal Sussex County Hospital |
| Department of Neurosurgery, University Hospital Sussex, Brighton, United Kingdom | 2 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
