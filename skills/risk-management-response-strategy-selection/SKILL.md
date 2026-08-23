---
name: risk-management-response-strategy-selection
description: >-
  Use when choosing between Avoid, Mitigate, Transfer, and Accept for a risk,
  selecting among candidate Mitigate controls, or auditing an Accept decision
  for missing ownership. Trigger on requests like "should we mitigate or
  accept this", "transfer via insurance?", "리스크 대응 전략 골라줘", "Accept with no
  named owner". Do NOT use for setting the appetite threshold that frames the
  decision (use risk-management-appetite-tolerance-threshold).
metadata:
  axis: response-strategy-selection
  rule_count_floor: 10
---

# Risk response strategy selection

## Trigger

Apply this skill when choosing a response strategy (Avoid, Mitigate,
Transfer, Accept) for a risk, when a risk is complex with multiple
contributing causes, when auditing an existing Accept decision, or when
ranking candidate Mitigate controls.

## Procedure

1. When likelihood x impact lands in the extreme band and a viable
   alternative activity exists, choose Avoid over Mitigate (rule 1).
2. When candidate-control cost is less than the expected value at risk,
   choose Mitigate; when it exceeds that value, choose Accept with
   active monitoring (rule 2).
3. When a third party can bear the consequence more cheaply than
   in-house mitigation, choose Transfer for that portion of the risk
   (rule 3).
4. When a risk is complex with multiple contributing causes, combine
   strategies per cause rather than one label for the whole risk
   (rule 4).
5. When an Accept decision has no named accountable owner and no
   monitoring trigger, strip the Accept label until both are attached
   (rule 5).
6. When selecting a Mitigate control, prefer source-removal over
   protective/add-on over information-only controls, in that order
   (rule 6).

## Output shape

One response strategy (or a per-cause combination of strategies) per
risk, with any Accept decision carrying a named owner and monitoring
trigger, and any selected Mitigate control ranked by the
source-removal > protective > information-only preference order.

## Decision rules

1. When likelihood x impact lands in the "extreme" band (top-right of a
   5x5 matrix) and a viable alternative activity exists, choose Avoid
   (eliminate the risk source or the activity) over Mitigate — Avoid is
   the correct choice specifically when an alternative strategy that
   sidesteps the exposure exists, not merely because severity is high.
   source: https://twproject.com/blog/risk-response-strategies-mitigation-transfer-avoidance-acceptance/
2. When the cost of a candidate control is less than the expected value
   at risk (likelihood x impact-in-currency), choose Mitigate; when
   candidate-control cost exceeds that expected value, choose Accept
   with active monitoring instead — this cost-of-control comparison is
   the deciding test, not severity read in isolation.
   source: https://internalauditor.theiia.org/en/articles/2022/february/risk-acceptance/
3. When a third party (insurer, vendor, partner) can bear the
   consequence more cheaply than in-house mitigation would cost, choose
   Transfer (insurance, hedging, outsourcing, contractual risk-shifting)
   for that portion of the risk, even if the underlying activity is not
   avoidable.
   source: https://decobeconsulting.com/risk-response-strategies-avoid-mitigate-transfer-or-accept/
4. When a risk is complex (multiple contributing causes), combine
   strategies per cause rather than forcing one label onto the whole
   risk — e.g. mitigate the process-failure component while
   transferring the residual financial-loss component via insurance.
   source: https://twproject.com/blog/risk-response-strategies-mitigation-transfer-avoidance-acceptance/
5. Removal: when an Accept decision has no named accountable owner and
   no monitoring trigger attached, do not record it as "Accept" —
   Accept without deliberate ownership is an unmanaged risk masquerading
   as a response decision; strip the Accept label until an owner and
   monitoring trigger are attached.
   source: https://internalauditor.theiia.org/en/articles/2022/february/risk-acceptance/
6. When selecting a Mitigate control, prefer a control that removes or
   reduces the hazard at its source over a protective/add-on control,
   and prefer a protective/add-on control over an information-only
   control (a warning, a monitoring alert, a training note) — rank
   candidate controls in that order and pick the highest-ranked one
   that is feasible, since an information-only control leaves the
   underlying hazard rate unchanged and only shifts the burden onto
   someone noticing and reacting in time.
