# Université de Picardie Jules Verne

[OpenAlex I4647051](https://openalex.org/institutions/I4647051) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Université de Picardie Jules Verne itself): 35,654 → 37,022 (+3.8%).
- **Counting its units and predecessors** (the `lineage` filter): 45,606 → 43,036 (−5.6%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (66% of lost works); the largest share of the strings it gained were assigned to other institutions before (41% of gained works), mostly Centre Hospitalier Universitaire Amiens-Picardie, Inserm.

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université de Picardie Jules Verne at all, about **94% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **72% do name it** or one of its units.

Net, the works that really are Université de Picardie Jules Verne's (counting its units) went up by about 3.5%.

**305 strings lost Université de Picardie Jules Verne** ([removed.csv](removed.csv)), on 469 works; **2,326 strings gained it** ([added.csv](added.csv)), on 3,017 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 66% |
| To other institutions (mostly Centre Hospitalier Universitaire Amiens-Picardie, Centre National de la Recherche Scientifique, Inserm) | 21% |
| To no institution | 13% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 29% |
| Up from one of its units or predecessors | 30% |
| From other institutions (mostly Centre Hospitalier Universitaire Amiens-Picardie, Inserm, UniLaSalle) | 41% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| LPMC | 91 | Laboratoire de physique de la matière condensée |
| Groupe de Recherche sur l'Analyse Multimodale de la Fonction Cérébrale - UMR INSERM_S 1105 | 25 | Inserm, Groupe de Recherches sur l’Analyse Multimodale de la Fonction Cérébrale |
| Laboratoire des Technologies Innovantes, Université Jules Vernes d’Amiens, rue des Facultés le Bailly, 800025 Amiens Cedex, France | 5 | Laboratoire des technologies innovantes |
| LAMFA, UMR 7352 CNRS, University of Picardie, 33 rue Saint Leu, 80039 Amiens, France | 4 | Centre National de la Recherche Scientifique, Laboratoire Amiénois de Mathématique Fondamentale et Appliquée |
| Laboratoire de Réactivité et de Chimie des Solides, URA CNRS 1211 Université de Picardie, 33 rue Saint-Leu, 80039 Amiens Cedex, France | 4 | Centre National de la Recherche Scientifique, Laboratoire de Réactivité et Chimie des Solides |
| AGIR EA 4294, 1 Rue des Louvels, 80000 AMIENS (France) | 3 | Agents infectieux, résistance et chimiothérapie |
| Département de Mathématiques, INSSET, Université de Picardie, 02109 St-Quentin, France – and – Laboratoire de Mathématiques Appliquées, UMR  | 3 | Université de Versailles Saint-Quentin-en-Yvelines, Centre National de la Recherche Scientifique, Centre de Mathématiques Appliquées de l'École polytechnique |
| LAMFA, UMR 7352 CNRS, University of Picardie, 33 rue Saint Leu, 80039, Amiens, France | 3 | Centre National de la Recherche Scientifique, Laboratoire Amiénois de Mathématique Fondamentale et Appliquée |
| Laboratoire des Eco-PRocédés, Optimisation et Aide à la Décision, EPROAD EA 4669, IUT de l’Aisne, 48 rue d’Ostende, Saint Quentin 02100, Fra | 3 | Eco-procédés, optimisation et aide à la décision |
| Laboratoire des Technologies Innovantes, Université Jules Vernes d'Amiens, rue des Facultés le Bailly, 800025 Amiens Cedex, France | 3 | Laboratoire des technologies innovantes |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Institut Polytechnique UniLaSalle Beauvais, Département Géosciences, Unité Bassins-Réservoirs-Ressources (B 2 R - U 2 R 7511), UniLaSalle-Un | 57 | UniLaSalle |
| Institut Polytechnique UniLaSalle Beauvais, Département Géosciences, Unité Bassins-Réservoirs-Ressources (B 2 R - U 2 R 7511), UniLaSalle-Un | 57 | UniLaSalle |
| Biologie des Plantes et Innovation - UR UPJV 3900 | 49 | Biologie des Plantes et Innovation |
| Lab. React. Chim. Solides, CNRS, Univ. Picardie Jules Verne, F-80039 Amiens, Fr | 48 | Laboratoire de Réactivité et Chimie des Solides |
| Périnatalité et Risques Toxiques - UMR INERIS_I 1 UPJV | 45 | Périnatalité & Risques Toxiques |
| Department of Cardiology, South Hospital, University of Picardie, Amiens, France | 23 | Centre Hospitalier Universitaire Amiens-Picardie |
| Groupe de Recherche sur l'alcool et les pharmacodépendances - UMR INSERM_S 1247 UPJV | 13 | Groupe de Recherche sur l'Alcool et les Pharmacodépendances |
| University of Picardie, Amiens, France | 13 | no institution |
| Department of Gastroenterology, Amiens University Hospital, Picardie University, Amiens, France | 11 | Centre Hospitalier Universitaire Amiens-Picardie |
| Lab. React. Chim. Solides, CNRS, Univ. Picardie Jules Verne, F‐80039 Amiens, Fr | 11 | Laboratoire de Réactivité et Chimie des Solides |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
