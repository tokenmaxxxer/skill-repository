---
type: llm
criteria: >-
  The judge checks whether the response keeps R2 and R4 in the list flagged
  as unverifiable-as-written with a request for the missing acceptance
  thresholds, instead of dropping them or substituting an invented p95 bar.
target: last_message
---
Pass only if the response keeps all four requirements in the list, flags R2
and R4 as unverifiable-as-written, and requests the missing acceptance
thresholds (e.g. a defined load/latency bar for R2, a concrete
notification behavior for R4) rather than inventing them. Fail if it drops
R2 or R4 from the list, or silently adopts the suggested p95 < 200ms (or
any self-invented bar) as R2's acceptance criterion.
