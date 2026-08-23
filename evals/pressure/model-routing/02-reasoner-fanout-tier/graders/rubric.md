---
type: llm
criteria: >-
  Whether the response identifies that the reasoner's own scout spawns inherit the expensive tier (multiplying the top-tier cost across every fan-out level) and restructures to fan out retrieval at executor tier, converging the collected material to a single reasoner judgment.
target: last_message
---
Pass only if the response spots that, with no per-subagent model
selection, every scout the reasoner spawns runs at the reasoner's
expensive tier — the single call quietly becomes many top-tier calls —
and restructures: fan out the mechanical retrieval (advisories,
maintainer activity, changelogs) across cheap executor subagents at the
orchestrator's level, then hand the collected material to one reasoner
for the judgment/ranking. Fail if the response endorses the single
fan-out-capable reasoner brief as cost-efficient, or restructures
without identifying tier inheritance as the problem.
