# Changelog

The matcher uses [semantic versioning](https://semver.org). A **major** version changes what counts as a right
answer (the [labelling rules](benchmarks/README.md#what-right-means)). A **minor** version improves the matcher (a
retrained model, a new source of candidates) and reruns it on every string. A **patch** fixes a known class of
strings. Every release reports its benchmark scores here.

## 1.0.0 (28 September 2026)

First release, replacing the [2023 model](https://github.com/ourresearch/openalex-institution-parsing) on all 165
million affiliation strings in OpenAlex.

- Exact match on [our benchmark](benchmarks/): 89.4% (2023 system: 72.7%).
- Exact match on the external benchmarks, pooled: 88.7% (2023 system: 73.0%).
