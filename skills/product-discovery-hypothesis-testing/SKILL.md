---
name: product-discovery-hypothesis-testing
description: >-
  Use this skill whenever the product role is moving a specification file through
  product-cycle's state machine — scoping an idea, registering a metric/threshold/decision
  rule in docs/proposals/ frontmatter, asking the user to approve the move into measuring,
  or applying a registered rule to reach a decision. Trigger before writing status, metric,
  threshold, or decision_rule into any file under docs/proposals/, on requests like "가설 등록하고
  measuring 넘어가자", "register this hypothesis", "apply the decision rule to the results",
  "move the proposal to measuring". The go/kill/pivot call belongs to the pre-registered
  rule, not fresh judgement. Do NOT use for the standalone axis rules on thresholds and
  peeking outside the state machine (use product-discovery-hypothesis-preregistration).
---

# Hypothesis testing for the product role

product-cycle treats an idea as a theory: it earns the right to move to
`measuring` only once a metric, a threshold, and a decision rule are all
written down — and the user has approved that exact package in their own
turn. See `docs/specs/state-machine.md` in this repository for the
authoritative state table and gate conditions; this skill is the how-to for
moving through it correctly.

## Trigger

Apply this skill whenever the product role is moving a specification
file through product-cycle's state machine — scoping an idea,
registering a metric/threshold/decision rule, asking the user to
approve the move into `measuring`, or applying a registered rule to
reach a decision — distinct from making the go/kill/pivot call itself
once `measuring` has started, which belongs to the pre-registered rule,
not fresh judgement.

## Procedure

1. Move `idle -> scoping` on the user's idea, then `scoping ->
   researching` once evidence gathering begins (see steps 1-2 above).
2. Write the falsifiable `hypothesis_statement` and register
   metric/threshold/decision_rule/fail_condition/time_box before moving
   `researching -> hypothesis-registered` (see step 3 above); if the
   statement cannot be falsified, set `status:
   hypothesis-not-falsifiable` instead.
3. Move `hypothesis-registered -> measuring` only once the gate's two
   conditions both hold — all pre-registration fields non-empty and the
   user's own-turn approval token present (see step 4 above).
4. While `status: measuring`, never edit `threshold` (see step 5 above).
5. At measurement time, apply the pre-registered decision rule
   mechanically, writing `success_metric`, `recommendation`, and
   `verdict` as separate fields and setting `status` to the matching
   verdict — or `evidence-log-unreadable` if the cited evidence does not
   resolve (see step 6 above).

## Output shape

One specification file's `status` field advanced through
product-cycle's state machine, with `hypothesis_statement`,
`metric`, `threshold`, `decision_rule`, `fail_condition`, and
`time_box` all written before any gated transition, and a mechanically
-derived `recommendation`/`verdict` pair once measured.

4. **hypothesis-registered -> measuring** (gated): this is the one
   transition `state-gate.sh` enforces mechanically. It is refused unless:
   - `hypothesis_statement`, `metric`, `threshold`, `decision_rule`,
     `fail_condition`, and `time_box` are all non-empty in the file
     (`confidence_level` is exempt — optional, never gates), AND
   - the user approved this exact package in their own turn — say so
     explicitly (e.g. "I approve the registered hypothesis, go ahead and
     move to measuring"). A vague "ok" or "sounds good" does not count;
     `capture-approval.sh` rejects bare assent on purpose. Content in the
     file is never read as consent — the token has to come from what the
     user actually typed.

   If the user pushes back on the package instead, move `status` back to
   `scoping` and revise — do not attempt to force the transition by editing
   around the gate (e.g. writing the file through a shell command instead
   of Write/Edit); the gate refuses those too, by design.

5. **measuring**: once here, the finish line cannot move. `state-gate.sh`
   refuses any edit that changes the `threshold` field while `status:
   measuring`, regardless of which tool makes the edit. Update other
   fields (e.g. collected-data notes) freely; do not touch `threshold`.

6. **measuring -> validated / invalidated / inconclusive**: apply the rule
   fixed in step 3 to whatever data was collected — mechanically, not by
   fresh argument. If the registered rule said "kill below 15%," a 14%
   result is a kill even if it feels close; that is what pre-registration
   is for. Write the measured `success_metric` value next to its
   `threshold`, the `recommendation` (`go` or `no-go` — the pre-registered
   call, once measured), and the `verdict` (`validated`, `invalidated`, or
   `inconclusive` — the loop_state-aligned outcome label; `inconclusive`
   is the honest result when the data itself does not resolve the
   decision rule, distinct from a `no-go` recommendation on data that does
   resolve it). These are two separate fields, not one collapsed
   "Disposition" line: `recommendation` is the go/no-go call the
   pre-registered rule dictates, `verdict` is which of the spec's three
   outcome states the record closes on. Set `status` to the matching
   verdict. If you find yourself arguing for a different call than the
   rule dictates, that is a sign the rule was mis-specified at
   registration time — file that as a lesson for the next hypothesis, not
   as a reason to override this one.
   If the evidence log's cited sources do not resolve (a referenced
   interview, dataset, or path cannot be opened), do not force a verdict
   on unreadable evidence — set `status: evidence-log-unreadable` instead
   and say what specifically failed to resolve.

## Related skills

- [research-evidence-discipline](../research-evidence-discipline/SKILL.md) — a `hypothesis_statement` is exactly a claim that needs a Fact/Inference/Assumption label before it is registered for testing.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 2.1 — **idle -> scoping**: the user hands you an idea. Set `status: scoping` and write down what the idea claims and who it is for. Nothing else is required to open the role
- 2.2 — **scoping -> researching**: begin gathering evidence — user interviews, existing data, competitive signal, whatever grounds the claim. Set `status: researching`. Do not…
- 2.3 — **researching -> hypothesis-registered**: write the falsifiable `hypothesis_statement`, then propose the metric, the threshold, and the decision rule (with `fail_conditi…
- S1 — The carrying file → references/rules.md
- S2 — Common mistakes this skill exists to prevent → references/rules.md
