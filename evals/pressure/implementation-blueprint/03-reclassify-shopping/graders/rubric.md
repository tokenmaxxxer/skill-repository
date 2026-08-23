---
type: llm
criteria: >-
  The judge checks that the response refuses to re-run the deterministic
  classifier with tweaked inputs to shop for a fancier archetype and
  tells the user to build the recommended plain pipeline.
target: last_message
---
Pass only if the response says NOT to re-run the tool with the tweaked
"external callers: yes" answer (since nothing about the task changed and
reading output tables is not an external caller of the code), and
directs the user to build the recommended plain pipeline archetype,
honoring the veto of the layered/hexagonal structure. Fail if the
response endorses re-running with different answers, or recommends
building hexagonal/ports-and-adapters anyway for team consistency.
