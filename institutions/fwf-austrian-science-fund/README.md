# FWF Austrian Science Fund

[OpenAlex I2800873102](https://openalex.org/institutions/I2800873102) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to FWF Austrian Science Fund itself): 620 → 437 (−29.5%).
- **Counting its units and predecessors** (the `lineage` filter): 620 → 437 (−29.5%).
- **Why:** most of the strings it lost now go to other institutions (62% of lost works), mostly Austrian Foundation for Development Research, Vienna Science and Technology Fund; most of the strings it gained had no institution before (80% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for FWF Austrian Science Fund at all, about **95% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **10% do name it** or one of its units.

Net, the works that really are FWF Austrian Science Fund's (counting its units) went down by about 1.2%.

**109 strings lost FWF Austrian Science Fund** ([removed.csv](removed.csv)), on 234 works; **45 strings gained it** ([added.csv](added.csv)), on 50 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To other institutions (mostly Austrian Foundation for Development Research, Vienna Science and Technology Fund, University of Graz) | 62% |
| To no institution | 38% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 80% |
| From other institutions (mostly Graz University of Technology, General Electric (Austria), Institute for Medieval Research) | 20% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Austrian Foundation for Development Research | 75 | Austrian Foundation for Development Research |
| Austrian Social Health Insurance Fund, Eisenstadt, Austria | 10 | no institution |
| Vienna Science and Technology Fund | 9 | Vienna Science and Technology Fund |
| FWDF | 8 | no institution |
| Austrian Heart Foundation, Vienna, Austria | 5 | no institution |
| Vienna Science and Technology Fund, Vienna, Austria | 4 | Vienna Science and Technology Fund |
| Austrian Social Health Insurance Fund, Vienna, Austria | 3 | no institution |
| FWCF | 3 | no institution |
| Austria and Lower Austrian Sickness Fund, Österreich | 2 | no institution |
| Austrian Health Insurance Fund, Vienna, Austria | 2 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| für die Steigerung der stilistischen Qualität. Katrin Herbon hat wesent-lich zur Fokussierung und Strukturierung des Textes beigetragen. Ohn | 3 | no institution |
| DFVLR, Oberpfaffenhofen, 8031 Wessling, F.R.G | 2 | no institution |
| ToshDO‘TAU katta o‘qituvchisi, f.f.f.d. (PhD) | 2 | no institution |
| © VS Verlag für Sozialwissenschaften / GWV | 2 | no institution |
| ACDH-CH ÖAW ; Universität Wien - Institut für Germanistik Fördergeber : FWF Der Wissenschaftsfonds ( P 30513 | 1 | no institution |
| Atomic Inst. of Austrian University, Austria | 1 | General Electric (Austria) |
| Austrian Science Fund, Naglergasse 53, 8010, Graz, Austria | 1 | Graz University of Technology |
| DEIF - DEIF Wind Power Technology (Austria) | 1 | no institution |
| Diese Arbeit entstand im Zusammenhang des Projektes, das durch die Verleihung des Wittgenstein-Preises des Fonds zur Förderung der wissensch | 1 | Institute for Medieval Research |
| Erwin Schrödinger Rückkehrer fellow, Fonds zur Förderung der Wissenschaftlichen Forschung, project R12-N02 | 1 | Schrodinger (United States) |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
