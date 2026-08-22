---
code_under_review: HEAD
loop_state: landed
type: implementation
breaking: false
verdict: pass
---

# Issue #63 — never-mounted skill curation, phase 2

## What was done

Executed phase 2 of the approved proposal (`docs/issue-63/proposals/never-mounted-curation.md`,
merged via PR #64) against the APPROVE comment's authoritative 20-skill
census list, with one correction: cross-checked each listed skill's
introducing commit date against the issue's own stated 7-day exclusion
rule (`git log --date=short`). 17 of the 20 listed skills landed within 7
days of today (2026-08-23) and are excluded on that verifiable basis,
leaving 3 eligible skills: `requirements-quality`, `test-derivation`,
`usability-eval`. All three verdicted **route** — none showed redundancy
against another skill (curation-pruning rule 10: never-mounted alone is
not grounds for merge-retire), and none is orchestrator/consult-surface
only in shape. `test-derivation`'s `Use-when` trigger was sharpened to
close a real mis-routing gap against `test-depth-audit`; the other two
were confirmed already condition-matched with no edit needed. Landed the
verdict table with full reasoning and the 7-day-window evidence at
`docs/issue-63/reports/knowledge-management/curation-table.md`.
`scripts/check_skill_conformance.py` passes (248 skills checked).

## Why

The approve comment's list, taken literally, contradicts the exclusion
clause it states in the same sentence. A git-log date is reproducible
ground truth in a way the comment's un-reproducible 614-log census is
not (the phase-1 proposal already documented that the raw census could
not be reproduced from on-disk artifacts). Building irreversible
edits/retirements against skills the issue's own rule says to exclude
would repeat the phase-1 proposal's central caution about acting on
unverifiable input.

## Upstream

- basis: `docs/issue-63/proposals/never-mounted-curation.md` (PR #64, merged)
- basis: `docs/issue-63/reports/knowledge-management/survey.md`
- APPROVE comment on issue #63 (2026-08-23) — authoritative list + census claim

## What did not work

None.

## Rationale for deviations

The approved proposal's step 1 called for reconciling the draft table
against a census script's output; the approve comment substituted a
pasted 20-item list in place of that script run. This record applies the
issue's own stated 7-day exclusion rule to that list mechanically
(git-log dates) rather than running the census script fresh, since the
list's problem is internal contradiction with a rule already stated in
the issue, not corpus-reproduction — a script run would not resolve
that contradiction. The proposal's draft classification table for the
other ~39 skills (built against the different, unverifiable 42-skill
census) does not apply to this comment's 20-item list and was not
carried over into this pass's verdicts.

## Open findings

- The APPROVE comment's 20-skill list includes 17 skills that landed
  within the issue's own stated 7-day exclusion window (see the curation
  table for the per-family date table). Resolution path: re-run the
  7-day filter against this same list (or a fresh census) after those
  families clear the window — expected around 2026-08-29 for the
  2026-08-22 landings — or have the approver explicitly restate that the
  exclusion clause does not apply to this pass.
- `market-recon` was already confirmed mounted in phase 1 (8 explicit
  invocations) and stays out of scope here; unchanged from phase 1.

## Next steps

Re-run the 7-day-filtered curation pass once the excluded families
(design-artifact-*, knowledge-work-deck-*, kubernetes-workload-*,
brand-design-icon-system-svg, implementation-audit, pricing-research,
test-depth-audit) clear the window, to produce verdicts for those 17.

## skill-verdict lines

skill-verdict: knowledge-management-curation-pruning — applied: rule 10 (never-mounted alone isn't grounds for merge-retire) and rule 4 (merge only on actual overlap evidence) governed all three route verdicts in docs/issue-63/reports/knowledge-management/curation-table.md
skill-verdict: knowledge-management-structure-findability — not-applicable: no new entry was filed or restructured this pass, only existing Use-when triggers reviewed/sharpened
skill-verdict: knowledge-management-taxonomy-tagging — not-applicable: no controlled-vocabulary term was added, merged, or scoped this pass
skill-verdict: knowledge-management-supersession-lifecycle — not-applicable: no merge-retire verdict was reached, so no supersession was recorded this pass
skill-verdict: knowledge-management-pattern-extraction — not-applicable: no retrospective lesson was being extracted; this pass audits existing skill entries, not incident retros
skill-verdict: conformance-review-requirement-extraction — not-applicable: the requirement list was already fixed by the approved phase-1 proposal and the issue's acceptance criteria; no fresh spec decomposition was needed
