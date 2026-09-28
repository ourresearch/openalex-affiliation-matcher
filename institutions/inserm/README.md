# Inserm

[OpenAlex I154526488](https://openalex.org/institutions/I154526488) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to Inserm itself): 507,629 → 509,899 (+0.4%).
- **Counting its units and predecessors** (the `lineage` filter): 823,805 → 649,960 (−21.1%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (80% of lost works); the largest share of the strings it gained moved up from one of its units (41% of gained works).

## Were the changes right?

We had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Inserm at all, about **98% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **47% do name it** or one of its units.

Net, the works that really are Inserm's (counting its units) went up by about 1.0%.

**11,593 strings lost Inserm** ([removed.csv.gz](removed.csv.gz)), on 14,549 works; **18,472 strings gained it** ([added.csv.gz](added.csv.gz)), on 20,074 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 80% |
| To other institutions (mostly Centre National de la Recherche Scientifique, Assistance Publique – Hôpitaux de Paris, German Cancer Research Center) | 17% |
| To no institution | 4% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 26% |
| Up from one of its units or predecessors | 41% |
| From other institutions (mostly Centre National de la Recherche Scientifique, Université Paris Cité, Assistance Publique – Hôpitaux de Paris) | 34% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| INSERM U289, Hôpital de la Salpêtrière, Paris, France | 96 | Pitié-Salpêtrière Hospital, Physiopathologie des Comportements |
| INSERM U289, Hôpital de la Salpêtrière. Paris France | 53 | Pitié-Salpêtrière Hospital, Physiopathologie des Comportements |
| IT - INSERM-TRANSFERT [Paris] (Paris - France) | 53 | Inserm Transfert |
| Inserm, U1111, Lyon, France | 47 | Centre International de Recherche en Infectiologie |
| PhyMedExp, University of Montpellier, INSERM U1046, CNRS UMR 9214, Montpellier, France | 45 | Université de Montpellier, Centre National de la Recherche Scientifique, Physiologie et Médecine Expérimentale du Coeur et des Muscles |
| CIRI-APY - Autophagie infection et immunité - Autophagy Infection Immunity [CIRI] (CIRI – INSERM U1111 21 avenue Tony Garnier 69007 Lyon - | 39 | Centre International de Recherche en Infectiologie |
| INSERM U 289, Hôpital de la Salpêtrière, Paris, France | 37 | Pitié-Salpêtrière Hospital, Physiopathologie des Comportements |
| Inserm U1312 - BRIC - BoRdeaux Institute in onCology (France) | 35 | BoRdeaux Institute of onCology |
| GHiGS - Global Health in the Global South (Centre de recherche INSERM U1219 - 146 rue Léo-Saignat - 33076 BORDEAUX cedex 200 - France) | 33 | Bordeaux Population Health |
| INSERM U36, Collège de France, Paris | 33 | Collège de France, Pathologie vasculaire et endocrinologie rénale |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| (Laboratoire CarMeN, Inserm U1060, INRAE U1397) | 172 | Laboratoire de recherche en cardiovasculaire, métabolisme, diabétologie et nutrition, Hospices Civils de Lyon, Lyon 1 Université, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement |
| ECSTRRA [CRESS - U1153 / UMR_A 1125] - Epidemiology and Clinical Statistics for Tumor, Respiratory, and Resuscitation / Epidémiologie Cliniq | 23 | Hôpital Saint-Louis, Centre de Recherche Épidémiologie et Statistique |
| National Institute of Health and Medical Research, Paris, France | 19 | no institution |
| EpiAgeing [CRESS - U1153 / UMR_A 1125] - Epidemiology of Ageing and Neurodegenerative diseases (Centre d'épidémiologie clinique Hôpital Hôte | 16 | Centre de Recherche Épidémiologie et Statistique, Hôtel-Dieu de Paris |
| CRESS - U1153 - Equipe 2 : ECSTRA - Epidémiologie Clinique, STatistique, pour la Recherche en Santé (SBIM Hôpital Saint Louis 1 avenue Cla | 13 | Hôpital Saint-Louis, Centre de Recherche Épidémiologie et Statistique |
| CRESS - U1153 - Equipe 5 : METHODS - Méthodes de l’évaluation thérapeutique des maladies chroniques (Centre d'épidémiologie clinique Hôpita | 13 | Centre de Recherche Épidémiologie et Statistique, Hôtel-Dieu de Paris |
| Groupe de Recherche sur l'alcool et les pharmacodépendances - UMR INSERM_S 1247 UPJV | 13 | Groupe de Recherche sur l'Alcool et les Pharmacodépendances |
| LGME - Laboratoire de Génetique Moléculaire des Eucaryotes (CNRS, Unité 184 de Biologie Moléculaire et de Génie Génétique de L'Institut Nati | 13 | Institut de Chimie, Centre National de la Recherche Scientifique |
| (LaTIM, INSERM, UMR 1101) | 12 | Laboratoire de Traitement de l'Information Médicale |
| French INSERM European Unit, University of Fribourg (LEA-IAME), Fribourg, Switzerland | 11 | University of Fribourg |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
