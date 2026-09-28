# Université Paris-Saclay

[OpenAlex I277688954](https://openalex.org/institutions/I277688954) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) (version 3.0) on 28 September 2026. Measured on the live data on 28 September, against the assignments just before the switch.

## In short

- **`works_count`** (works linked to Université Paris-Saclay itself): 209,367 → 167,514 (−20.0%).
- **Counting its units and predecessors** (the `lineage` filter): 680,190 → 621,316 (−8.7%).
- **Why:** most of the strings it lost now go to one of its units or predecessors, which still count for it through `lineage` (78% of lost works); most of the strings it gained moved up from one of its units (62% of gained works).

## Were the changes right?

Before the switch, we had Claude Opus 5.5 judge random samples of these strings, without saying whether each was added or removed: of the works that no longer count for Université Paris-Saclay at all, about **72% did not name it** or any of its units, so losing them fixed an error; of the works that newly count for it, about **77% do name it** or one of its units.

**33,931 strings lost Université Paris-Saclay** ([removed.csv.gz](removed.csv.gz)), on 61,467 works; **5,753 strings gained it** ([added.csv.gz](added.csv.gz)), on 7,749 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 78% |
| To other institutions (mostly Centre National de la Recherche Scientifique, Inserm, Assistance Publique – Hôpitaux de Paris) | 14% |
| To no institution | 9% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 10% |
| Up from one of its units or predecessors | 62% |
| From other institutions (mostly Institut Gustave Roussy, Inserm, Bicêtre Hospital) | 28% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| Paris 11 | 2,701 | no institution |
| Université Paris-Sud | 1,581 | Université Paris-Sud |
| University of Paris-Sud | 1,270 | Université Paris-Sud |
| Université Paris-Sud, Orsay, France | 1,121 | Université Paris-Sud |
| Université Paris-Sud - Paris 11 | 1,095 | Université Paris-Sud |
| Universite Paris Sud | 909 | Université Paris-Sud |
| UP11 - Université Paris-Sud - Paris 11 (Bâtiment 300 - 91405 Orsay cedex - France) | 773 | Université Paris-Sud |
| Laboratoire de Physique des Solides, Université Paris Sud, 91405 Orsay, France | 438 | Université Paris-Sud, Laboratoire de physique des Solides |
| Institut des Sciences Moléculaires d’Orsay (ISMO), CNRS, Univ. Paris-Sud, Univ. Paris-Saclay, Orsay, France | 362 | Université Paris-Sud, Centre National de la Recherche Scientifique, Institut des Sciences Moléculaires d'Orsay |
| Laboratoire de Physique des Solides, Université Paris-Sud, 91405 Orsay, France | 337 | Université Paris-Sud, Laboratoire de physique des Solides |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| IPS2 (UMR_9213 / UMR_1403) - Institut des Sciences des Plantes de Paris-Saclay (Institute of Plant Sciences - Paris-Saclay Bâtiment 630, ru | 253 | Institut des Sciences des Plantes de Paris Saclay |
| ComUE Paris-Saclay | 247 | no institution |
| Universit&#x00E9; Paris-Saclay, CNRS, CentraleSup&#x00E9;lec, Laboratoire des Signaux et Syst&#x00E8;mes, Gif-sur-Yvette, France | 74 | Laboratoire des signaux et systèmes, Centre National de la Recherche Scientifique |
| QuaCS - Quantum Computation Structures (ENS Paris Saclay, 4, avenue des Sciences, 91190 Gif-sur-Yvette, France - France) | 49 | QUACS: Structures de calcul quantique |
| CNRS, CentraleSup&#x00E9;lec, Laboratoire des Signaux et Syst&#x00E8;mes, Universit&#x00E9; Paris-Saclay, Gif-sur-Yvette, France | 43 | Laboratoire des signaux et systèmes, Centre National de la Recherche Scientifique |
| Faculté de Médecine Paris-Saclay (63 Rue Gabriel Péri, 94270 Le Kremlin-Bicêtre - France) | 29 | Bicêtre Hospital |
| Universit&#x00E9; Paris-Saclay, CNRS, CentraleSup&#x00E9;lec, Laboratoire des signaux et syst&#x00E8;mes, Gif-sur-Yvette, France | 23 | Laboratoire des signaux et systèmes, Centre National de la Recherche Scientifique |
| CentraleSupelec, University Paris-Saclay, Gif-sur-Yvette, France | 22 | CentraleSupélec |
| Laboratoire de Mathématiques de Versailles, University Paris-Saclay, Versailles, Yvelines, France | 18 | Université de Versailles Saint-Quentin-en-Yvelines |
| Université de Paris Saclay, Departement de Biologie _ Versailles-Saint Quentin, 55 Avenue de Paris, 78035 Versailles Cedex, France | 18 | Université de Versailles Saint-Quentin-en-Yvelines, Université Paris Cité |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
