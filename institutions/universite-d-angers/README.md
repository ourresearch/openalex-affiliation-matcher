# Université d'Angers

[OpenAlex I49451733](https://openalex.org/institutions/I49451733) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Université d'Angers itself): 32,707 → 32,895 (+0.6%).
- **Counting its units and predecessors** (the `lineage` filter): 78,082 → 64,545 (−17.3%).
- **Why:** most of the strings it lost now go to other institutions (64% of lost works), mostly Centre Hospitalier Universitaire d'Angers, Inserm; the largest share of the strings it gained moved up from one of its units (41% of gained works).

## Were the changes right?

We did not judge a sample of the changes for Université d'Angers.

**5,458 strings lost Université d'Angers** ([removed.csv](removed.csv)), on 8,303 works; **5,120 strings gained it** ([added.csv.gz](added.csv.gz)), on 8,082 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 8% |
| To other institutions (mostly Centre Hospitalier Universitaire d'Angers, Inserm, Centre National de la Recherche Scientifique) | 64% |
| To no institution | 27% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 23% |
| Up from one of its units or predecessors | 41% |
| From other institutions (mostly Inserm, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement, Centre National de la Recherche Scientifique) | 37% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Angers | 1,154 | no institution |
| Angers University Hospital, Angers, France | 98 | no institution |
| (IRHS ; INRAE, Institut Agro Rennes-Angers, Université Angers) | 56 | Institut Agro Rennes-Angers, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement |
| University Hospital of Angers, Angers, France | 54 | no institution |
| University of Angers - Centre d'Etudes Prospectives d'Economie Mathematique Appliquees a la Planification (CEPREMAP) | 53 | no institution |
| 49045 Angers | 35 | no institution |
| Univ Angers, Inserm, CNRS, MINT, SFR ICAT, F-49000 Angers, France | 32 | Inserm, Centre National de la Recherche Scientifique, Micro et Nanomédecines translationnelles |
| 49033 ANGERS Cédex 01, France | 29 | no institution |
| Clinical Hematology, Angers University Hospital, Angers, France | 27 | Centre Hospitalier Universitaire d'Angers |
| Angers/FR | 22 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| Laboratoire Angevin de Recherche en Ingénierie des Systèmes | 483 | Laboratoire Angevin de Recherche en Mathématiques |
| Laboratoire d'Etudes et de Recherche en Informatique d'Angers | 356 | Laboratoire de Recherche en Informatique |
| Langues, Littératures, Linguistique des Universités d'Angers et du Mans | 266 | 3L.AM - Langues, Littératures, Linguistique des Universités d’Angers et du Mans |
| Laboratoire de Photonique d'Angers | 250 | Laboratoire Angevin de Recherche en Mathématiques |
| Langues, Littératures, Linguistique des universités d'Angers et du Mans | 202 | 3L.AM - Langues, Littératures, Linguistique des Universités d’Angers et du Mans |
| Esthua Faculté de Tourisme, Culture et Hospitalité (7, allée François Mitterrand  BP 40455 49004 ANGERS Cedex 01 - France) | 63 | no institution |
| Department of Geriatric Medicine and Memory Clinic, Research Center on Autonomy and Longevity, University Hospital, Angers, France | 46 | no institution |
| QUASAV - SFR UA 4207 QUAlité et SAnté du Végétal (Département Biologie & Sciences de la vie, UFR Sciences - 2, Boulevard Lavoisier, 49045 AN | 31 | no institution |
| Univ Angers, Institut Agro, INRAE, IRHS, SFR QUASAV, Angers, France | 29 | Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement, L'Institut Agro |
| (Université d'Angers, Ecole Supérieure d'Agriculture d'Angers) | 28 | École supérieure des agricultures |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
