---
name: incident-response-rca-method-selection
description: Use when you need guidance on RCA method selection. Applies to the rca-method-selection axis.
axis: rca-method-selection
rule_count_floor: 4
---

# RCA method selection

Decision rules for which root-cause-analysis method to apply
(this rulebook's `root_cause (root-cause-analysis, 5-Whys/causal-chain)`
field / `incident-response-rca-method-gate`). Layer 1 (practitioner:
Google SRE workbook), layer 2 (named methods: 5 Whys, fishbone, fault
tree), layer 3 (RCA-method-comparison literature).

## Rules

1. When the failure runs down one relatively linear causal path (a
   single service's proximate trigger led directly to the outage), use
   a 5-Whys causal chain — it is fast, needs no setup, and Google's own
   workbook has teams "work through at least one 5 Whys chain from the
   primary failure." source: https://sre.google/workbook/postmortem-analysis/

2. When the incident escalated because it was not caught quickly (long
   detection or response delay), run a SECOND 5-Whys chain rooted at the
   detection/response delay, separate from the failure chain — the
   Google SRE workbook names this as a distinct required chain, not an
   extension of the first, because "why did it fail" and "why didn't we
   catch it" are different causal chains with different fixes. source:
   https://sre.google/workbook/postmortem-analysis/

3. When several independent contributing factors combined to cause the
   incident (parallel causation, not one line of dominoes), do not force
   a single 5-Whys chain — supplement with a fault tree, which
   represents parallel causation and, per OSHA 1910.119(e)(2)(vi), is
   built for exactly this shape of investigation. source:
   https://www.soter.com/blog/5-whys-vs-fishbone-vs-fault-tree

4. When the team needs to brainstorm candidate causes broadly across
   people/process/tooling/environment before narrowing (early
   investigation, causes not yet obvious), open with a fishbone diagram
   to generate breadth, then apply 5 Whys to the 2-3 most likely
   fishbone branches to get chain depth — the two methods are
   complementary stages, not competing alternatives. source:
   https://fivewhys.ai/blog/root-cause-analysis-methods-compared

5. When distinguishing primary cause from contributing factors in the
   record (`incident-response-rca-method-gate` requires this
   distinction), frame contributing factors as 2-5 systemic,
   blame-neutral causes (process gaps, tooling limits, documentation
   gaps) rather than isolating one single "root cause" — current SRE
   theory treats "root cause" as often misleading for complex incidents
   because failures usually arise from multiple interacting conditions.
   source: https://incident.io/blog/sre-incident-postmortem-best-practices

6. **REMOVAL**: when a fishbone diagram has been drawn but the write-up
   stops there, do not submit the fishbone itself as the RCA — a
   fishbone "doesn't establish causal relationships between branches," so
   presenting raw fishbone output as the primary_cause/contributing
   factors distinction skips the causal-chain step the gate actually
   requires; cut the unconverted fishbone from the final record and
   replace it with the 5-Whys chain(s) run on its top branches. source:
   https://www.soter.com/blog/5-whys-vs-fishbone-vs-fault-tree
