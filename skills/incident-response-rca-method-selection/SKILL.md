---
name: incident-response-rca-method-selection
description: >-
  Use when choosing which root-cause-analysis method to apply to an incident —
  5 Whys, fishbone, or fault tree — or converting a fishbone into a causal
  chain. Applies to the rca-method-selection axis. Trigger on requests like "5
  whys or fault tree here", "run RCA on this outage", "fishbone to causal
  chain", "이 장애 근본원인 분석 방법 골라줘". Adds a second chain rooted at the
  detection/response delay when the incident escalated because it was caught
  slowly. Do NOT use for deciding how deep the postmortem needs to go for its
  tier (use incident-response-severity-classification-scoping).
metadata:
  axis: rca-method-selection
  rule_count_floor: 4

---

# RCA method selection

Decision rules for which root-cause-analysis method to apply
(this skill spec's `root_cause (root-cause-analysis, 5-Whys/causal-chain)`
field / `incident-response-rca-method-gate`). Layer 1 (practitioner:
Google SRE workbook), layer 2 (named methods: 5 Whys, fishbone, fault
tree), layer 3 (RCA-method-comparison literature).

## Trigger

Apply this skill when deciding which root-cause-analysis method fits an
incident's causal shape — a single linear failure, a detection/response
delay, several parallel contributing factors, or an early-investigation
brainstorm — or when a fishbone diagram has been drawn and needs
converting into a causal chain, distinguishing it from
severity-classification-scoping (how deep the RCA needs to go, not which
method to use at that depth).

## Procedure

1. When the failure runs down one relatively linear causal path, use a
   5-Whys causal chain (rule 1).
2. When the incident escalated because it was not caught quickly, run a
   second, separate 5-Whys chain rooted at the detection/response delay
   (rule 2).
3. When several independent contributing factors combined to cause the
   incident, supplement with a fault tree instead of forcing a single
   5-Whys chain (rule 3).
4. When causes are not yet obvious, open with a fishbone diagram to
   generate breadth, then apply 5 Whys to the 2-3 most likely branches
   (rule 4).
5. When distinguishing primary cause from contributing factors in the
   record, frame contributing factors as 2-5 systemic, blame-neutral
   causes rather than isolating one single root cause (rule 5).
6. When a fishbone diagram has been drawn but the write-up stops there,
   do not submit the fishbone itself as the RCA — convert its top
   branches into 5-Whys chain(s) before finalizing (rule 6).

## Output shape

One or more causal chains (5-Whys and/or fault tree) rooted at the
failure and, when detection was slow, a second chain rooted at the
detection/response delay, plus a primary-cause/contributing-factors
split with 2-5 systemic, blame-neutral contributing factors.

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

## Related skills

- [incident-response-timeline-construction](../incident-response-timeline-construction/SKILL.md) — before selecting an RCA method, timeline-construction should have already fixed the incident's event sequence.
