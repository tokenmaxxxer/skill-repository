---
type: llm
criteria: >-
  Whether the response rejects the flat uniform 10% draw, fully inspects all 18 security-critical entries (highest impact tier exempt from sampling), samples the lower-impact strata separately, and states the derivation (population, strata, per-stratum sizes, selection method) for the record.
target: last_message
---
Pass only if the response stratifies by impact rather than taking one
flat 10% draw: all 18 security-critical entries inspected in full (the
highest-impact tier is exempt from sampling), with the routing and
cosmetic strata sampled separately at stated per-stratum sizes and a
stated selection method, and the whole derivation (population 300,
stratum definitions, sizes, method) written for the record. Fail if the
response adopts the flat proportional 10% sample (which would sample
roughly 2 of 18 security-critical entries), or gives counts without
stating the derivation.
