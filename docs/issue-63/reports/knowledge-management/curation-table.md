# Curation table — never-mounted skill pass (issue #63, phase 2)

## Open finding: the APPROVE comment's 20-item list conflicts with its own exclusion clause

The APPROVE comment (2026-08-23) says to use its 20-skill orchestrator-census
list "as the authoritative enumeration, excluding families landed within 7
days as the issue states" — but the list it then pastes includes exactly the
families that clause excludes. Checked against `git log --date=short` on
each `SKILL.md`'s introducing commit (ground truth, reproducible):

| family | landed | days before 2026-08-23 | within 7-day window? |
|---|---|---|---|
| design-artifact-* (5) | 2026-08-22 | 1 | yes — excluded |
| knowledge-work-deck-* (3) | 2026-08-22 | 1 | yes — excluded |
| kubernetes-workload-* (5) | 2026-08-22 | 1 | yes — excluded |
| brand-design-icon-system-svg | 2026-08-22 | 1 | yes — excluded |
| implementation-audit | 2026-08-21 | 2 | yes — excluded |
| pricing-research | 2026-08-21 | 2 | yes — excluded |
| test-depth-audit | 2026-08-21 | 2 | yes — excluded |
| requirements-quality | 2026-07-16 | 38 | no |
| test-derivation | 2026-07-16 | 38 | no |
| usability-eval | 2026-07-16 | 38 | no |

17 of the 20 listed skills landed within the issue's own stated 7-day
exclusion window and are held out of this pass on that basis — a verifiable,
repo-derived fact takes precedence over the list's literal contents where
the list's own stated rule says otherwise. This mirrors the phase-1
proposal's already-approved handling of the `market-recon` false-positive:
verify before acting on a census figure the session cannot fully
reproduce. Resolution path: re-run this table's 7-day filter at the next
review cycle once these families clear the window, or the approver can
restate explicitly that the exclusion clause does not apply this pass.

## Verdicts — 3 skills eligible after the 7-day filter

| skill | verdict | reason |
|---|---|---|
| requirements-quality | route | `Use-when` already condition-matched (EARS/QUS-specific Korean+English trigger phrases, explicit binary-check scope) and actively cross-referenced as a handoff target from `adversarial-review` (surface/mock findings) and `test-derivation` (no-requirements case). No overlap found justifying merge; no orchestrator-only shape — it is a concrete audit deliverable a role invokes directly. No edit needed. |
| test-derivation | route | Same shape: sharp trigger, active incoming references from `requirements-quality` and `test-depth-audit` (existing-suite handoff). One real gap found and fixed: its `Do NOT use` list named `requirements-quality` and non-functional testing but not the "existing tests, verify what they check" case that actually belongs to `test-depth-audit` — sharpened in `skills/test-derivation/SKILL.md` to close that mis-routing gap. |
| usability-eval | route | Already condition-matched (formative-vs-summative split stated up front, explicit sample-size heuristic) and is itself the cross-reference target from `experiment-trust` and `user-discovery` for the "existing design, evaluative" case. No overlap found justifying merge; no edit needed. |

**Verdict counts: route 3, reclassify 0, merge-retire 0.**

No merge-retire or reclassify verdicts were reached this pass — the 7-day
filter removed every skill this pass had evidence to judge as
orchestrator-only or redundant (that evidence lived in the phase-1
proposal's draft table, which covered the different, unverifiable 42-skill
census and does not carry over to this comment's list). Re-running this
table once the excluded families clear their 7-day window is the natural
next step for those verdicts.

## Conformance

`python3 scripts/check_skill_conformance.py` → `248 skills checked`, exit 0.
