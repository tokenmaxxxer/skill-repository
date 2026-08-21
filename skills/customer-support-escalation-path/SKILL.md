---
name: customer-support-escalation-path
description: Use when you need guidance on Escalation-path decision rules.
---

# Escalation-path decision rules

Axis: escalation-path. Every tier below names a trigger, a role/title
owner (never "the team"), and a timeout — the shape the escalation-path
plugin's judgment layer requires beyond the gate's bare word-presence
check.

## Rules

- When a P1 ticket (Impact: High, Urgency: High per sla-tier-priority.md)
  is unresolved 30 minutes after first response, escalate to the Duty
  Manager with a 15-minute acknowledgment timeout — apply the numeric
  SLA table from https://www.novelvista.com/blogs/it-service-management/itil-incident-priority-matrix
  rather than a vague "escalate if it drags on."
- When the Duty Manager does not acknowledge a P1 escalation within 15
  minutes, escalate again to the Support Team Lead with a further
  15-minute timeout — never leave the second tier undefined once the
  first tier's timeout has already lapsed. Source: https://www.pagerduty.com/resources/digital-operations/learn/incident-priority-matrix/
- Under a P2 ticket that breaches its 4-hour resolution target, escalate
  to the Support Team Lead (not "the team") with a 1-hour timeout for
  a revised ETA — name the role explicitly so ownership survives
  personnel turnover. Source: https://blog.invgate.com/itil-priority-matrix
- When a requester reports the same unresolved defect a second time
  inside 7 days, escalate to the on-call Support Team Lead within 4
  business hours regardless of the ticket's own SLA clock — a repeat
  contact is itself an urgency signal the original tier assignment did
  not capture. Source: https://www.topdesk.com/en/blog/incident-priority-matrix/
- **REMOVAL**: drop a standing "CC the whole support channel" escalation
  step once a named-owner tier exists for the same trigger — broadcast
  escalation with no accountable owner is the generic-owner failure
  mode this axis's directive already prohibits, and it adds a
  notification a reader must parse without adding resolution capacity.
  Source: https://www.pagerduty.com/resources/digital-operations/learn/incident-priority-matrix/
