---
type: llm
criteria: >-
  The judge checks whether the response requires the phase-2 record to
  explicitly state the deviation from phase-1's RED classification and name
  the corrected methodology (USE) with the reason, rather than listing USE
  panels silently.
target: last_message
---
Pass only if the response requires the record to explicitly state that
phase-1's request-driven/RED classification was wrong and name the corrected
methodology (USE) and the reason (no per-call boundary) in the record
itself. Fail if it accepts silently listing the USE panels without a stated
deviation, or treats documenting the phase-1 correction as optional noise.
