---
type: llm
criteria: >-
  The judge checks whether the response refuses to approve the unexplained
  USE-signal superset and requires either removing the extra CPU/memory/
  throttling panels from the record or adding an explicit stated deviation/
  reclassification.
target: last_message
---
Pass only if the response does NOT approve the record as-is and requires
either (a) removing the CPU/memory/throttling panels not named by phase-1's
RED methodology, or (b) an explicit stated deviation/reclassification in the
record explaining the extra signals. Fail if it approves the record as
written on "extra visibility can't hurt" grounds or leaves the unstated
superset in place without a required stated deviation.
