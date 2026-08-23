---
type: llm
criteria: >-
  The judge checks that the response rejects the not-applicable-by-
  phase-1 claim because the new fan-out/eventing requirement is a new
  structural decision that must be classified, not wedged in.
target: last_message
---
Pass only if the response refuses to record "not applicable, frozen by
DR-31", on the grounds that the enrichment fan-out and event
subscription constitute a NEW structural decision this phase, and calls
for classifying/structuring that addition (new inputs, new
classification or explicit structural decision) rather than wedging it
into the existing transform module. Fail if the response endorses the NA
note, or accepts wedging the new async/eventing behavior into the frozen
three-module layout without treating it as a structural decision.
