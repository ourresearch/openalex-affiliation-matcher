# The University of Queensland

[OpenAlex I165143802](https://openalex.org/institutions/I165143802) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to The University of Queensland itself): 293,181 → 294,678 (+0.5%).
- **Counting its units and predecessors** (the `lineage` filter): 298,750 → 297,289 (−0.5%).
- **Why:** most of the strings it lost now go to other institutions (71% of lost works), mostly Queensland University of Technology, Ochsner Medical Center; most of the strings it gained had no institution before (53% of gained works).

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**1,361 strings lost The University of Queensland** ([removed.csv](removed.csv)), on 1,559 works; **4,288 strings gained it** ([added.csv](added.csv)), on 5,705 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 4% |
| To other institutions (mostly Queensland University of Technology, Ochsner Medical Center, Ochsner Health System) | 71% |
| To no institution | 25% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 53% |
| Up from one of its units or predecessors | 6% |
| From other institutions (mostly Ochsner Medical Center, Indian Institute of Technology Delhi, Royal Brisbane and Women's Hospital) | 41% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| AndroUrology Centre, Brisbane, QLD 4000, Australia | 11 | no institution |
| Inorganic Materials Research Program , School of Physical and Chemical Sciences , Queensland University of Technology , GPO Box 2434 , Brisb | 11 | Queensland University of Technology |
| University of Oxford/Queensland | 9 | University of Oxford |
| John Ochsner Heart and Vascular Institute, Ochsner Clinical School-The University of Queensland School of Medicine, New Orleans, Louisiana,  | 7 | Ochsner Medical Center |
| School of Clinical Sciences, Queensland University of Technology, Brisbane, Queensland, Australia. Electronic address: crispen.chamunyonga@q | 7 | Queensland University of Technology |
| Department of Cardiovascular Diseases, John Ochsner Heart and Vascular Institute, Ochsner Clinical School-The University of Queensland Schoo | 6 | Ochsner Health System, Ochsner Medical Center |
| University of Brisbane, Brisbane, Australia | 6 | Brisbane City Council |
| Department of Cardiovascular Diseases, John Ochsner Heart and Vascular Institute, Ochsner Clinical School the University of Queensland Schoo | 5 | no institution |
| John Ochsner Heart and Vascular Institute, Ochsner Clinical School-The University of Queensland School of Medicine, New Orleans, LA, USA | 5 | Ochsner Medical Center |
| , Queensland , Australia | 4 | no institution |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| The University of Queensland Medical School, Ochsner Clinical School, New Orleans, LA | 84 | Ochsner Medical Center |
| Queensland Brain Institute | 68 | Allen Institute for Brain Science |
| UQ | 53 | no institution |
| Sch. of Inf. Technol. & Electr. Eng., Queensland Univ., St. Lucia, QLD, , Australia | 36 | no institution |
| School of Chemical Engineering and Australian Institute for Bioengineering and Nanotechnology (AIBN) | 35 | no institution |
| Dep. Chem., Univ. Queensl., Brisbane, Queensl. 4072, Australia | 29 | no institution |
| Department of Social and Preventive MedicineUniversity of Queensland | 28 | no institution |
| Department of SurgeryUniversity of Queensland | 27 | no institution |
| U Queensland, School of Psychology, Brisbane, QLD, Australia | 25 | no institution |
| TC Beirne School of Law | 21 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
