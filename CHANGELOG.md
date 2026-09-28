# Changelog

The matcher uses [semantic versioning](https://semver.org). A **major** version changes what counts as a right
answer (the [labelling rules](benchmarks/README.md#what-right-means)) or replaces the approach. A **minor** version
improves the matcher (a retrained model, a new source of candidates) and reruns it on every string. A **patch** fixes a
known class of strings. Every release reports its benchmark scores here.

## 3.0.0 (28 September 2026)

A new matcher (find candidates, score each one, choose the set), replacing V2 on all 165 million affiliation strings
in OpenAlex.

- Exact match on [our benchmark](benchmarks/): 89.4% (V2 with its hand-written rules and curations: 72.7%).
- Exact match on the external benchmarks, pooled: 88.7% (V2: 73.0%).

## 2.0 (March 2023)

The second OpenAlex institution tagger: could name several institutions per string, and only institutions with a ROR
ID. Later joined by hand-written rules and a pass through ROR's matcher.
[Code and write-up](https://github.com/ourresearch/openalex-institution-parsing/tree/main/V2).

## 1.0 (June 2022)

The first OpenAlex institution tagger, trained on Microsoft Academic Graph data to replace MAG's own affiliation
parsing. [Code](https://github.com/ourresearch/openalex-institution-parsing/tree/main/V1).
