---
name: incident-response-action-item-quality
description: Use when you need guidance on Action item quality and prioritization. Applies to the action-item-quality axis.
axis: action-item-quality
rule_count_floor: 4
---

# Action item quality and prioritization

Decision rules for the `action_items (owner+verb+outcome+deadline)`
field and `incident-response-action-item-gate`. Layer 1 (practitioner:
PagerDuty postmortem docs, incident.io), layer 2 (named framework:
severity-vs-effort prioritization), layer 3 (subtraction-neglect —
Adams, Converse, Hales & Klotz, *Nature* 594, 2021 — applied to backlog
pruning).

## Rules

1. When writing an action item, open with a directive verb (implement,
   document, add, remove) naming a named owner and a concrete outcome
   and a deadline — an item missing any of these four is not checkable
   by a reader who was not present, which is exactly what
   `incident-response-action-item-gate`'s shape check requires. source:
   https://www.pagerduty.com/resources/insights/learn/how-to-write-postmortem/

2. When setting a deadline for a SEV1-driven action item, target
   completion within 15 days of the incident; for a SEV2-driven item,
   target 30 days — PagerDuty's internal policy ties deadline urgency to
   the severity that produced the item, not a flat default across all
   incidents. source: https://www.pagerduty.com/resources/digital-operations/learn/incident-postmortem/

3. When the postmortem meeting produces more than ~5 candidate action
   items, prioritize by a severity-vs-effort matrix — do first: high
   risk-reduction, low effort; batch with routine maintenance: low
   severity, low effort; challenge/likely cut: low severity, high effort
   unless it addresses a recurring pattern — prioritize by risk
   reduction, not by whoever spoke loudest in the meeting. source:
   https://rootly.com/incident-postmortems/meeting-guide

4. When an action item is explicitly deprioritized rather than executed,
   record the decision and its reason in the postmortem ("we decided not
   to do this because the risk is low and the effort is high") instead
   of silently dropping it from the list — an unrecorded drop is
   indistinguishable from a forgotten commitment to a later reader.
   source: https://incident.io/blog/why-do-post-mortem-action-items-fail-how-to-make-incident-follow-ups-actually-get-done

5. When the completed-within-30-days rate across recent action items
   falls under ~50%, treat that as a signal the list itself is
   over-generated, not that execution needs to be pushed harder — the
   next postmortem's action-item count should shrink, not repeat the
   same generation habit that produced an unexecutable backlog. source:
   https://incident.io/blog/why-do-post-mortem-action-items-fail-how-to-make-incident-follow-ups-actually-get-done

6. **REMOVAL**: when drafting the action-item list, actively look for
   items to cut before finalizing — three to five well-defined items
   that address root causes are more valuable than a large list, and
   people "systematically overlook subtractive changes," so a pass that
   only adds candidate items without a deliberate cutting pass will
   over-produce by default, especially under the cognitive load of a
   live postmortem meeting. source: https://www.nature.com/articles/s41586-021-03380-y
