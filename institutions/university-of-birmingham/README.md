# University of Birmingham

[OpenAlex I79619799](https://openalex.org/institutions/I79619799) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of Birmingham itself): 228,857 → 242,337 (+5.9%).
- **Counting its units and predecessors** (the `lineage` filter): 230,678 → 243,105 (+5.4%).
- **Why:** most of the strings it lost now go to other institutions (73% of lost works), mostly Queen Elizabeth Hospital Birmingham, University Hospitals Birmingham NHS Foundation Trust; most of the strings it gained had no institution before (53% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for University of Birmingham at all, about **81% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **83% do name it** or one of its units.

Net, the works that really are University of Birmingham's (counting its units) went up by about 4.9%.

**993 strings lost University of Birmingham** ([removed.csv](removed.csv)), on 1,552 works; **5,795 strings gained it** ([added.csv](added.csv)), on 11,416 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly Queen Elizabeth Hospital Birmingham, University Hospitals Birmingham NHS Foundation Trust, University of Alabama at Birmingham) | 73% |
| To no institution | 27% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 53% |
| Up from one of its units or predecessors | 5% |
| From other institutions (mostly Aston University, Birmingham City University, The Edgbaston Hospital) | 42% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Birmingham/UK | 131 | no institution |
| Queen Elizabeth Hospital Birmingham, University Hospitals Birmingham NHS Foundation Trust, Birmingham, UK | 50 | University Hospitals Birmingham NHS Foundation Trust, Queen Elizabeth Hospital Birmingham |
| Senior Lecturer, School of Information Studies, University of Central England, Birmingham | 24 | Birmingham City University |
| Queen Elizabeth Hospital Birmingham, University Hospitals Birmingham NHS Foundation Trust, Birmingham, United Kingdom | 23 | University Hospitals Birmingham NHS Foundation Trust, Queen Elizabeth Hospital Birmingham |
| Alabama Univ. Birmingham, United States | 16 | University of Alabama at Birmingham |
| Department of Ophthalmology, Queen Elizabeth Hospital Birmingham, University Hospitals Birmingham NHS Foundation Trust, Birmingham, UK | 14 | University Hospitals Birmingham NHS Foundation Trust, Queen Elizabeth Hospital Birmingham |
| [Alabama Univ., Birmingham, AL, USA] | 14 | University of Alabama at Birmingham |
| Department of Gastroenterology, Queen Elizabeth Hospital Birmingham, University Hospitals Birmingham NHS Foundation Trust, Birmingham, UK | 12 | University Hospitals Birmingham NHS Foundation Trust, Queen Elizabeth Hospital Birmingham |
| Department of Upper Gastrointestinal Surgery, Queen Elizabeth Hospital Birmingham, University Hospitals Birmingham NHS Trust, Birmingham, UK | 12 | Queen Elizabeth Hospital Birmingham |
| University of Alabama at Birmingham, UK | 12 | University of Alabama at Birmingham |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Birmingham U | 425 | Birmingham City University |
| Birmingham Business School | 271 | no institution |
| Aston Institute of Photonic Technologies, Aston University, Birmingham, UK | 234 | Aston University |
| Aston Institute of Photonic Technologies, Aston University, Birmingham B4 7ET, UK | 206 | Aston University |
| Aston Business School, Birmingham, UK | 179 | Aston University |
| School of Computer Science, University of Binningham, Birmingham, UK | 165 | no institution |
| Birmingham Law School | 159 | no institution |
| Aston Institute of Photonic Technologies, Aston University, Birmingham, U.K | 138 | Aston University |
| School of Electronic and Electrical Engineering, University of Binningham, Birmingham, UK | 130 | no institution |
| Aston Institute of Photonic Technologies, Aston University, Birmingham, B4 7ET, UK | 128 | Aston University |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
