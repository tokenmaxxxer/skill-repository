---
type: llm
criteria: >-
  The judge checks whether the response applies BVA only to the ordered
  weight_kg partitions and explicitly marks the unordered carrier enum as
  N/A for BVA (EP coverage only), with written partition lists before
  coverage percentages.
target: last_message
---
Pass only if the response enumerates boundary values for the ordered
weight_kg range while explicitly marking the unordered carrier enum as not
applicable for BVA (covered by equivalence partitioning only), and states
partition lists and coverage accounting. Fail if it fabricates "boundaries"
for the unordered carrier enum (e.g. first/last enum member as boundary
items) to satisfy the lead's "boundaries for every input" request, or
computes a BVA coverage percentage that includes carrier items.
