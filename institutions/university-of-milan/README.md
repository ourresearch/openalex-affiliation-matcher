# University of Milan

[OpenAlex I189158943](https://openalex.org/institutions/I189158943) · what changed when OpenAlex switched to its [new affiliation matcher](../../README.md) on 28 September 2026. Numbers from the final dry run on 27 September; we will refresh them from live data after the switch.

## In short

- **`works_count`** (works linked to University of Milan itself): 407,713 → 412,790 (+1.2%).
- **Counting its units and predecessors** (the `lineage` filter): 408,379 → 412,810 (+1.1%).
- **Why:** most of the strings it lost now go to other institutions (60% of lost works), mostly Università Cattolica del Sacro Cuore, University of Milano-Bicocca; most of the strings it gained were assigned to other institutions before (71% of gained works), mostly Istituto Nazionale di Fisica Nucleare, Sezione di Milano, University of Milano-Bicocca.

## Were the changes right?

Not sampled: its works changed by less than 2%, so we did not judge a sample.

**4,078 strings lost University of Milan** ([removed.csv](removed.csv)), on 11,640 works; **19,898 strings gained it** ([added.csv.gz](added.csv.gz)), on 25,657 works. A work with several of these strings counts once per string. Both files are sorted by works, biggest first; files over 1 MB are gzipped.

## Where the lost strings went

| | Share of works |
|---|---:|
| To one of its units or predecessors (still counts through `lineage`) | 0% |
| To other institutions (mostly Università Cattolica del Sacro Cuore, University of Milano-Bicocca, Politecnico di Milano) | 60% |
| To no institution | 40% |

## Where the gained strings came from

| | Share of works |
|---|---:|
| From no institution | 28% |
| Up from one of its units or predecessors | 0% |
| From other institutions (mostly Istituto Nazionale di Fisica Nucleare, Sezione di Milano, University of Milano-Bicocca, Fondazione IRCCS Ca' Granda Ospedale Maggiore Policlinico) | 71% |

## Biggest losses

| String | Works | Now |
|---|---:|---|
| unimi | 3,759 | no institution |
| Catholic University of Milan | 387 | Università Cattolica del Sacro Cuore |
| Department of Psychology, Catholic University of Milan, Milan, Italy | 328 | Università Cattolica del Sacro Cuore |
| Technical University of Milan | 177 | Politecnico di Milano |
| Milan U | 139 | no institution |
| Catholic University of Milan, Italy | 130 | Università Cattolica del Sacro Cuore |
| Universita degli Studi di Milano-Bicocca, Dipartimento di Biotecnologie e Bioscienze, Milano, Italy & National Biodiversity Future Center, P | 112 | University of Milano-Bicocca |
| Universita degli Studi di Milano-Bicocca, Dipartimento di Scienze dell'Ambiente e della Terra, Milano, Italy | 112 | University of Milano-Bicocca |
| Catholic University of Milan, Milan, Italy | 86 | Università Cattolica del Sacro Cuore |
| Catholic University of Milan ** | 75 | Università Cattolica del Sacro Cuore |

## Biggest gains

| String | Works | Before |
|---|---:|---|
| University of Milan - Bicocca | 374 | University of Milano-Bicocca |
| Università di Milano, Dipartimento di Fisica and INFN, I-20133 Milano, Italy | 165 | Istituto Nazionale di Fisica Nucleare, Sezione di Milano |
| Dipartimento di Fisica, Università di Milano and INFN, Via Celoria 16, I-20133 Milan, Italy | 56 | Istituto Nazionale di Fisica Nucleare, Sezione di Milano |
| Dipartimento di Fisica, Università di Milano and INFN, Sezione di Milano, Via Celoria 16, I-20133 Milano, Italy | 51 | Istituto Nazionale di Fisica Nucleare, Sezione di Milano |
| Milan University | 47 | Mylan (South Africa) |
| Dipartimento di Scienze Farmacologiche e Biomolecolari “Rodolfo Paoletti” | 46 | University of Pavia |
| Istituto Auxologico Italiano and Centro Interuniversitario di Fisiologia Clinica e Ipertensione, Università di Milano, Milan, Italy | 39 | IRCCS Istituto Auxologico Italiano |
| Dipartimento di Fisica and INFN, Università di Milano, I-20133 Milano, Italy | 36 | Istituto Nazionale di Fisica Nucleare, Sezione di Milano |
| Department of Legal Sciences - Milan | 34 | no institution |
| Istituto di Fisica dell'Università, Milano, Italia | 34 | no institution |

## Something wrong?

Fix it yourself in the [Affiliation Editor](https://help.openalex.org/access/fixing-errors/affiliations/) (your corrections override the matcher), or [tell us](https://openalex.org/contact).
