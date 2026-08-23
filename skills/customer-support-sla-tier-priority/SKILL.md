---
name: customer-support-sla-tier-priority
description: >-
  Use when a ticket needs an Impact x Urgency Priority tier and
  first-response/resolution commitment assigned, or when checking whether a
  legacy priority label maps to the ITIL matrix. Trigger on requests like "is
  this P1 or P2", "티켓 우선순위 정해줘", "first-response SLA for this ticket", "Impact
  Urgency matrix". Do NOT use for picking the escalation owner and timeout
  after a breach (use customer-support-escalation-path).
---

# SLA-tier priority decision rules

Axis: sla-tier-priority. Every rule below maps an Impact x Urgency pair to
a Priority tier via the ITIL incident-prioritization matrix convention —
tier values are traceable to that lookup, never asserted by feel.

## Trigger

Apply this skill when assigning a ticket's Impact x Urgency Priority
tier and its first-response/resolution commitment, or when auditing an
existing priority label (including a legacy one) against the ITIL
matrix.

## Procedure

1. When a ticket affects a single user with no deadline pressure
   (Impact: Low, Urgency: Low), assign Priority 4/P4 and commit a
   24-hour first response (rule 1).
2. When an issue affects a single user who is blocked right now (Impact:
   Low, Urgency: High), choose Priority 3/P3 over P4 (rule 2).
3. When multiple users lose access to a core function (Impact: High) but
   a workaround exists (Urgency: Medium), select Priority 2/P2 rather
   than P1 (rule 3).
4. When an incident affects many users AND leaves no workaround (Impact:
   High, Urgency: High), assign Priority 1/P1 and commit a 15-minute
   first response with escalation if unresolved by the 30-minute mark
   (rule 4).
5. Under a P2 commitment, escalate to the Support Team Lead if the
   ticket is not resolved by hour 5 of a 4-hour resolution target
   (rule 5).
6. When a queue carries a legacy "Priority 0 / Blocker" label that
   predates the Impact x Urgency matrix, drop that label rather than
   keeping a sixth tier alongside P1-P4 (rule 6).

## Output shape

One Priority tier (P1-P4) traceable to an (Impact, Urgency) cell, paired
with its first-response/resolution commitment and, when applicable, its
escalation trigger.

## Rules

- When a ticket affects a single user and that user states no deadline
  pressure (Impact: Low, Urgency: Low), assign Priority 4/P4 and commit
  a 24-hour first response — this is the ITIL matrix's lowest-priority
  cell, not a default catch-all bucket. Source: https://www.topdesk.com/en/blog/incident-priority-matrix/
- When an issue affects a single user but that user reports being
  blocked from completing a task right now (Impact: Low, Urgency: High),
  choose Priority 3/P3 over P4 — urgency alone lifts the tier even when
  impact stays narrow, per the matrix's two-axis product, not a
  single-axis read. Source: https://blog.invgate.com/itil-priority-matrix
- When multiple users or a whole team lose access to a core function
  (Impact: High) but a workaround exists so nobody is fully blocked
  (Urgency: Medium), select Priority 2/P2 rather than P1 — reserve P1
  for the Impact-High x Urgency-High cell. Source: https://www.pagerduty.com/resources/digital-operations/learn/incident-priority-matrix/
- When an incident affects many users AND leaves no workaround (Impact:
  High, Urgency: High), assign Priority 1/P1 and commit a 15-minute
  first response with escalation triggered if unresolved by the
  30-minute mark — do not soften this to P2 on the assumption that
  "it'll get fixed anyway." Source: https://www.novelvista.com/blogs/it-service-management/itil-incident-priority-matrix
- Under a P2 commitment, escalate to the Support Team Lead if the
  ticket is not resolved by hour 5 of a 4-hour resolution target —
  never leave escalation unstated once a numeric SLA has been quoted to
  the requester. Source: https://www.topdesk.com/en/blog/incident-priority-matrix/
- **REMOVAL**: when a queue carries a legacy "Priority 0 / Blocker"
  label that predates the Impact x Urgency matrix, drop that label
  rather than keeping a sixth tier alongside P1-P4 — a tier that maps to
  no (Impact, Urgency) cell adds a decision surface agents must
  memorize with no matrix backing it, which is exactly the kind of
  un-traceable tier value this axis's own convention forbids. Source:
  https://www.novelvista.com/blogs/it-service-management/itil-incident-priority-matrix
