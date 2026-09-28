# Massachusetts Institute of Technology

[OpenAlex I63966007](https://openalex.org/institutions/I63966007) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Massachusetts Institute of Technology itself): 405,944 → 439,668 (+8.3%).
- **Counting its units and predecessors** (the `lineage` filter): 431,707 → 460,589 (+6.7%).
- **Why:** the largest share of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (43% of lost works); most of the strings it gained were assigned to other institutions before (64% of gained works), mostly Moscow Institute of Thermal Technology, Broad Institute.

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Massachusetts Institute of Technology at all, about **77% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **70% do name it** or one of its units.

**2,988 strings lost Massachusetts Institute of Technology** ([removed.csv](removed.csv)), on 9,720 works; **24,939 strings gained it** ([added.csv.gz](added.csv.gz)), on 60,183 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 43% |
| To other institutions (mostly Broad Institute, Harvard–MIT Division of Health Sciences and Technology, Harvard University) | 32% |
| To no institution | 24% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 21% |
| Up from one of its units or predecessors | 15% |
| From other institutions (mostly Moscow Institute of Thermal Technology, Broad Institute, MIT Media Lab) | 64% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| 1050 Massachusetts Avenue Cambridge , MA 02138 | 1,148 | no institution |
| MIT Lincoln Lab. Lexington, MA, USA | 341 | MIT Lincoln Laboratory |
| Ragon Institute of MGH, MIT and Harvard, Cambridge, MA, USA | 267 | Ragon Institute of MGH, MIT and Harvard |
| Harvard-MIT Division of Health Sciences and Technology, Cambridge, MA, USA | 220 | Harvard–MIT Division of Health Sciences and Technology |
| Ragon Institute of MGH, MIT, and Harvard, Cambridge, MA, USA | 199 | Ragon Institute of MGH, MIT and Harvard |
| Broad Institute of Harvard and MIT, Cambridge, Massachusetts, USA | 162 | Broad Institute |
| Harvard-MIT Division of Health Sciences and Technology, Cambridge, MA 02139, USA | 139 | Harvard–MIT Division of Health Sciences and Technology |
| MIT Lincoln Laboratory; | 118 | MIT Lincoln Laboratory |
| MIT - CSAIL, Cambridge, MA#TAB# | 110 | MIT Computer Science and Artificial Intelligence Laboratory |
| CSAIL, MIT, Cambridge, MA, USA | 104 | MIT Computer Science and Artificial Intelligence Laboratory |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| MIT | 12,994 | Moscow Institute of Thermal Technology |
| MIT, LNS | 1,102 | no institution |
| MIT CSAIL | 1,074 | MIT Computer Science and Artificial Intelligence Laboratory |
| (MIT) | 941 | Moscow Institute of Thermal Technology |
| @mit | 724 | Moscow Institute of Thermal Technology |
| MIT Sloan School of Management | 674 | no institution |
| -MIT | 578 | Moscow Institute of Thermal Technology |
| MIT Media Lab | 415 | Human Media, MIT Media Lab |
| MIT Media Lab, Cambridge, MA, USA | 261 | Human Media, MIT Media Lab |
| MIT Media Lab, Cambridge, MA | 252 | Human Media, MIT Media Lab |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
