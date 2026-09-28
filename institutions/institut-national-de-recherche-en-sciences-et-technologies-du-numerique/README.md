# Institut national de recherche en sciences et technologies du numérique

[OpenAlex I1326498283](https://openalex.org/institutions/I1326498283) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Institut national de recherche en sciences et technologies du numérique itself): 149,610 → 129,397 (−13.5%).
- **Counting its units and predecessors** (the `lineage` filter): 305,041 → 295,695 (−3.1%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (61% of lost works); most of the strings it gained moved up from one of its units (70% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Institut national de recherche en sciences et technologies du numérique at all, about **58% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **84% do name it** or one of its units.

Net, the works that really are Institut national de recherche en sciences et technologies du numérique's (counting its units) went up by about 1.4%.

**16,526 strings lost Institut national de recherche en sciences et technologies du numérique** ([removed.csv.gz](removed.csv.gz)), on 31,475 works; **4,549 strings gained it** ([added.csv](added.csv)), on 5,546 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 61% |
| To other institutions (mostly Centre National de la Recherche Scientifique, Université Paris-Saclay, Université Côte d'Azur) | 32% |
| To no institution | 7% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 11% |
| Up from one of its units or predecessors | 70% |
| From other institutions (mostly Centre de Recherche en Informatique, Centre National de la Recherche Scientifique, Lyon 1 Université) | 19% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Web-Instrumented Man-Machine Interactions, Communities and Semantics | 397 | WIMMICS: Web-Instrumented huMan-Machine Interactions, Communities and Semantics |
| INRIA Sophia Antipolis, | 251 | Centre Inria d'Université Côte d'Azur |
| Inria, Rennes, France | 214 | Centre Inria de l'Université de Rennes |
| Inria Paris | 209 | Centre Inria de Paris |
| Univ Rennes, Inria, CNRS, IRISA, Rennes, France | 185 | Université de Rennes, Centre National de la Recherche Scientifique, Institut de Recherche en Informatique et Systèmes Aléatoires, Centre Inria de l'Université de Rennes |
| Université de Lorraine, CNRS, Inria, LORIA, Nancy, France | 178 | Université de Lorraine, Centre National de la Recherche Scientifique, Laboratoire Lorrain de Recherche en Informatique et ses Applications |
| Université de Lorraine, CNRS, Inria, LORIA, F-54000 Nancy, France | 173 | Université de Lorraine, Centre National de la Recherche Scientifique, Laboratoire Lorrain de Recherche en Informatique et ses Applications |
| Inria-Rennes, France#TAB# | 167 | Centre Inria de l'Université de Rennes |
| Inria Centre de Recherche de Paris | 142 | Centre Inria de Paris |
| LEMON - Littoral, Environment: MOdels and Numerics (Inria, team LEM0N Bât 5 – CC05 017 860 rue Saint-Priest 34095 Montpellier Cedex 5 Fr | 140 | LEMON: Littoral, Environnement, Modèles et Outils Numériques |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Inst. Nat. de Recherche en Inf. et Autom., Le Chesnay, France | 99 | no institution |
| MOAIS - PrograMming and scheduling design fOr Applications in Interactive Simulation (Inria Grenoble - Rhône-Alpes 655 avenue de l'Europe -  | 79 | Centre Inria de l'Université Grenoble Alpes |
| Athena EPI, Inria Sophia-Antipolis | 75 | Athena Research and Innovation Center In Information Communication & Knowledge Technologies, Centre Inria d'Université Côte d'Azur |
| PRIVATICS - Privacy Models, Architectures and Tools for the Information Society (Centre Inria de l'Université Grenoble Alpes 655, avenue de | 55 | Centre Inria de l'Université Grenoble Alpes, Université Grenoble Alpes, PRIVATICS: Modèles, architectures et outils pour la protection de la vie privée dans la société de l'information |
| SED [Grenoble] - Service Expérimentation et Développement (Service Expérimentation et Développement Inria 655, avenue de l'Europe 38 334 Sai | 42 | Centre Inria de l'Université Grenoble Alpes |
| E-MOTION - Geometry and Probability for Motion and Action (Inria Grenoble Rhône-Alpes 655 avenue de l'Europe - Montbonnot 38334 Saint Ismier | 32 | Centre Inria de l'Université Grenoble Alpes |
| 𝐈𝐍𝐑𝐈𝐀🇫🇷 Nat. Inst. for DigitSci & Tech | 30 | NTL Institute for Applied Behavioral Science |
| INRIA-Saclay, Team Parietal | 26 | Centre Inria de Saclay |
| Institut National de Recherche en Informatique et Automatique, Le Chesnay, France | 20 | Centre de Recherche en Informatique |
| APACHE - Parallel algorithms and load sharing (Centre de recherche Inria 655 avenue de l'Europe 38330 Montbonnot Saint-Martin - France) | 16 | Centre Inria de l'Université Grenoble Alpes |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
