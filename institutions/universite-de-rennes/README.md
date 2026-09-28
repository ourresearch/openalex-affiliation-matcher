# Université de Rennes

[OpenAlex I56067802](https://openalex.org/institutions/I56067802) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Université de Rennes itself): 90,371 → 85,499 (−5.4%).
- **Counting its units and predecessors** (the `lineage` filter): 173,443 → 154,283 (−11.0%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (54% of lost works); the largest share of the strings it gained moved up from one of its units (47% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université de Rennes at all, about **89% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **84% do name it** or one of its units.

**11,807 strings lost Université de Rennes** ([removed.csv.gz](removed.csv.gz)), on 19,171 works; **7,268 strings gained it** ([added.csv.gz](added.csv.gz)), on 12,237 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 54% |
| To other institutions (mostly Université Rennes 2, Centre Hospitalier Universitaire de Rennes, Centre National de la Recherche Scientifique) | 41% |
| To no institution | 5% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 18% |
| Up from one of its units or predecessors | 47% |
| From other institutions (mostly Université Rennes 2, Centre Hospitalier Universitaire de Rennes, Hôpital Pontchaillou) | 35% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| UR2 - Université de Rennes 2 (Place du recteur Henri Le Moal - CS 24307 - 35043 Rennes cedex - France) | 1,807 | Université Rennes 2 |
| Université de Rennes 2 | 905 | Université Rennes 2 |
| Université de Rennes 2 - UFR Sciences sociales | 248 | Université Rennes 2 |
| Université de Rennes 2 - UFR Arts, Lettres, Communication | 143 | Université Rennes 2 |
| Université de Rennes I, France | 141 | Université Rennes 1 |
| Université de Rennes I | 134 | Université Rennes 1 |
| Univ. de Rennes I (France) | 104 | Université Rennes 1 |
| Univ. de Rennes I, France | 99 | Université Rennes 1 |
| ERMINE - mEasuRing and ManagIng Network operation and Economic (Campus de beaulieu 35042 Rennes cedex - France) | 90 | ERMINE: Gestion et mesures des opérations et de l'économie des réseaux |
| 35042 Rennes Cedex | 86 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Rennes 1 | 2,414 | Université Rennes 2 |
| ERIMIT - Équipes de Recherches Interlangues : Mémoires, Identités, Territoires (Université Rennes 2 - UFR Langues - Campus Villejean - Place | 228 | Université Rennes 2 |
| University Rennes I, Rennes GEOSCIENCES, FRANCE | 200 | Géosciences Rennes |
| Université Rennes | 132 | no institution |
| Faculté de droit et de science politique [Rennes] | 87 | no institution |
| SeRAIC - Signalisation et Réponses aux Agents Infectieux et Chimiques (Faculté de Pharmacie, Rue du Professeur Léon Bernard, 35000 Rennes -  | 74 | no institution |
| Laboratoire de Geologie - Faculté des sciences de Rennes | 57 | Géosciences Rennes |
| CRIBS - Centre de Recherche en Information Biomédicale sino-français (Rennes - France) | 54 | no institution |
| Laboratoire d'Economie et de Sciences Sociales de Rennes. UHB | 41 | no institution |
| Géosciences Rennes, UMR 6118, Université de Rennes 1, CNRS, 35000 Rennes (France) and JURASSICA Museum, Route de Fontenais 21, CH- 2900 Porr | 35 | Canadian Museum of Nature, Centre National de la Recherche Scientifique, Géosciences Rennes |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
