---
name: incident-response-action-item-quality
description: >-
  Use when drafting, prioritizing, or cutting a postmortem's action-item list
  — writing items, setting deadlines, or deciding what to drop. Applies to the
  action-item-quality axis. Trigger on requests like "write the postmortem
  action items", "owner verb outcome deadline check", "prioritize the
  follow-up list", "포스트모템 액션 아이템 정리해줘". Sets severity-tied deadlines (15 days
  for SEV1, 30 for SEV2) and cuts the list to 3-5 root-cause-addressing items.
  Do NOT use for finding the causes those items address (use
  incident-response-rca-method-selection).
metadata:
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

## Trigger

Apply this skill when drafting or reviewing a postmortem's action-item
list — writing new items, setting deadlines, prioritizing a candidate
list, or deciding whether to cut an item — distinguishing it from
rca-method-selection (finding causes) and severity-classification-scoping
(how deep the whole document should be).

## Procedure

1. When writing an action item, require a directive verb, a named
   owner, a concrete outcome, and a deadline in the same item (rule 1).
2. Set the deadline from the incident's severity: 15 days for a
   SEV1-driven item, 30 days for a SEV2-driven item (rule 2).
3. When more than ~5 candidate items exist, prioritize by a
   severity-vs-effort matrix rather than meeting-room volume (rule 3).
4. When deprioritizing an item, record the decision and its reason
   instead of silently dropping it from the list (rule 4).
5. When the recent completion rate falls under ~50%, treat that as a
   signal to shrink the next list, not to push execution harder (rule 5).
6. Before finalizing the list, run a deliberate cutting pass and keep
   only the 3-5 well-defined, root-cause-addressing items (rule 6).

## Output shape

A short action-item list (typically 3-5 items), each with owner, verb,
outcome, and deadline, prioritized by severity-vs-effort, with any
deprioritized candidate recorded alongside its cut reason.

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
