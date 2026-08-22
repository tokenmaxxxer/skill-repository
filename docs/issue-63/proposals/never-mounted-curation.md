---
status: proposed
files:
  - scripts/census_skill_mounts.py
  - docs/issue-63/reports/knowledge-management/curation-table.md
  - skills/decision-records/SKILL.md
  - skills/prior-art-scan/SKILL.md
  - skills/reference-forecast/SKILL.md
  - skills/hypothesis-testing/SKILL.md
  - skills/silent-failure-audit/SKILL.md
  - skills/prose-modes/SKILL.md
  - skills/stride/SKILL.md
  - skills/experiment-trust/SKILL.md
  - skills/launch-readiness/SKILL.md
  - skills/tech-feasibility/SKILL.md
  - skills/blameless-postmortem/SKILL.md
  - skills/security-threat-model-threat-modeling-decision-rules/SKILL.md
  - skills/technical-feasibility-stride-table/SKILL.md
  - skills/incident-response-blameless-language-editing/SKILL.md
  - skills/release-engineering-readiness-checklist/SKILL.md
  - skills/technical-feasibility-verdict-and-timebox-selection/SKILL.md
  - skills/growth-analytics-experiment-trust/SKILL.md
---

Scout-skip condition note (gate path mismatch, not a research skip): the survey-order gate checks for a survey file at the generic path `docs/issue-63/reports/implementation/survey.md`, but `docs/issue-63/reports/implementation/**` belongs to the `implementation` role, not `knowledge-management` — board-gate refuses this role writing there. The actual current-state survey for this pass was written first, in full, at the role-correct path `docs/issue-63/reports/knowledge-management/survey.md`, before this proposal. No research step was skipped; only the gate's hardcoded path is inapplicable to a non-implementation role.

## Request

Skill-repository issue #63: 42 skills in the 248-skill catalog have never mounted (present in zero sessions' skill list). For each, assign one of three verdicts — **route** (sharpen the `Use-when` trigger, keep, add to candidate pool), **reclassify** (mark orchestrator/consult-surface-only — used in conversation-level judgment, never spawned as a mounted role skill), or **merge-retire** (fold into an overlapping skill, supersede, record the supersession) — with a one-line reason each, then execute the mechanical follow-through for verdicts 1 and 3. `design-artifact-*` and `knowledge-work-deck-*` (8 skills, landed 2026-08-22, within the 7-day exclusion window) are out of scope for this pass.

## Constraints

- `scripts/check_skill_conformance.py` must stay green after any `SKILL.md` edit or retirement.
- Retirement must not delete history — supersession gets recorded (per `[[knowledge-management-supersession-lifecycle]]`), not silently dropped.
- Never-mounted alone is not sufficient grounds for merge-retire (curation-pruning rule 10, consulted this session) — merge-retire requires actual redundancy/overlap evidence against another skill, not just zero mounts.
- Phase 1 only: this PR proposes the table and the mechanical plan; it does not execute `SKILL.md` edits or retirements yet (that is phase 2, gated on approval).

## Rationale

**Alternative considered and rejected: treat the issue's `614-log / 42-skill` census as ground truth and classify exactly that list.** Rejected because the census could not be reproduced from the on-disk artifacts available to this session (see `docs/issue-63/reports/knowledge-management/survey.md` — three independent mount-signal searches across 1218 `consult-log.md`, 623 session logs, and 322 task files together surfaced only 31 skills with any observed mount signal, not 206). Fabricating a 42-item list to match the issue's stated count, without being able to verify it against the actual corpus the orchestrator used, would produce verdicts anchored to invented data rather than checkable evidence. Building on unverifiable input this early risks the entire mechanical follow-through (trigger edits, merges, retirements) landing against the wrong skill set.

**Alternative considered and rejected: skip census reproduction entirely and classify by structural analysis alone, presented as authoritative.** Rejected because it would silently paper over the reproduction gap instead of surfacing it — the gap is itself decision-relevant information for whoever approves phase 2.

**Chosen approach:** treat the log-reproduction gap as an open finding, reproduce a runnable census script as this pass's first mechanical deliverable (so the true 42 can be confirmed against a corpus the orchestrator specifies), and in the meantime apply the issue's own stated classification *structure* — family-routable vs. orchestrator/general-methodology-shaped — mechanically against the catalog. That structural test independently reproduces every skill the issue names as an example (`decision-brief`, `diagnose-first`, `fmea`, `premortem`, `adversarial-review`, `stride`, `flow-metrics`, `compliance-scan`, `decision-records`, `agent-coordination`, `blameless-postmortem`), which is the strongest available evidence that the structural proxy tracks the real 42 even without a byte-exact log match. It also caught something the issue's example list didn't call out: `market-recon` looked orphaned by the structural test but is verifiably mounted (8 explicit `Skill`-tool invocations found in logs) — proof the structural proxy alone is not sufficient and needs the census script to correct it before phase 2 executes anything irreversible.

## What will be done

**Phase 1 (this PR):** land the survey, this proposal, and the classification table below. No `SKILL.md` files are edited yet.

**Phase 2 (post-approval), in order:**

1. Write and run `scripts/census_skill_mounts.py` — a script taking a log-corpus root as an argument, scanning for the three mount signals identified in the survey (explicit `Skill`-tool invocations, `skill_judge` picks, role-mapping headers), and emitting a `skill → mount_count` table. Run it against whatever corpus the orchestrator confirms is authoritative; reconcile against the structural-analysis table below — add/drop skills as the real count dictates.
2. For every **route**-verdict skill, sharpen its `SKILL.md` `Use-when`/trigger line with a more condition-matched description (concrete symptom or task shape, not a restated category name) so it clears the BM25 candidate-pool bar more often.
3. For every **reclassify**-verdict skill, add a short note to its `SKILL.md` (or a shared `docs/handbooks/` note) marking it consult-surface-only, so future curation passes don't re-flag it as "never mounted" expecting role-mount behavior it was never meant to have.
4. For every **merge-retire**-verdict skill: fold its unique rules into the surviving skill's `SKILL.md`, add a supersession note on the retired skill pointing at the survivor (per `[[knowledge-management-supersession-lifecycle]]` — mark superseded, do not delete the file outright), and record the pairing in the curation table.
5. Run `scripts/check_skill_conformance.py` and fix any regressions before landing.
6. Update `docs/issue-63/reports/knowledge-management/curation-table.md` with final verdict counts (route / reclassify / merge-retire) and write the phase-2 record at `docs/issue-63/reports/knowledge-management.md`.

**Draft classification (candidate set, pending census-script reconciliation in step 1 above):**

| skill | verdict | reason |
|---|---|---|
| decision-brief | reclassify | escalation-shaped judgment call made at conversation level, no role owns "decide for the user" as a domain |
| diagnose-first | reclassify | applies before any role-specific work starts; gates the reflex to act on a guess, not a role's domain output |
| fmea | reclassify | generic risk-analysis technique invoked when doing risk analysis, not tied to one role's family |
| premortem | reclassify | same shape as fmea — a technique selected by task, not by role |
| adversarial-review | reclassify | orchestrator-level review pattern (used inside verify/judge fan-outs), not a role-mounted skill |
| stride | merge-retire | duplicate of `technical-feasibility-stride-table` and overlaps `security-threat-model-threat-modeling-decision-rules`; fold unique content into `technical-feasibility-stride-table`, supersede |
| flow-metrics | reclassify | process/retro-level metric selection, cross-cutting, no owning role family |
| compliance-scan | reclassify | pre-emptive scan run across roles, not owned by the `legal-compliance-*` family alone |
| decision-records | route | generic ADR-writing need recurs across `implementation`/`architecture` work; sharpen trigger to match "record a decision after it's made" so BM25 picks it up post-decision-brief |
| agent-coordination | reclassify | infra/orchestration-level skill for concurrent-agent sessions, not a domain role's output |
| blameless-postmortem | merge-retire | near-duplicate of `incident-response-blameless-language-editing`; fold into it, supersede standalone |
| overengineering-audit | reclassify | pairs with premature-scaling as a cross-cutting code-quality check, not role-domain-bound |
| parallel-decomposition | reclassify | orchestration-level task-cutting decision, made by the session/orchestrator not a domain role |
| merge-gates | reclassify | orchestration-level, concerns concurrent-branch landing, not a role's deliverable |
| model-routing | reclassify | explicitly orchestrator-level per its own trigger ("use on every non-trivial task... to decide what you do yourself") |
| premature-scaling | reclassify | pairs with overengineering-audit, cross-cutting |
| prior-art-scan | route | fits naturally under tech-feasibility-shaped work; sharpen trigger to name concrete "check for existing solutions before building" moment |
| reference-forecast | route | reference-class forecasting is broader than `capacity-planning-demand-shape-and-forecast-method`; keep standalone but sharpen trigger to distinguish from it |
| launch-readiness | merge-retire | near-duplicate of `release-engineering-readiness-checklist`; fold into it, supersede standalone |
| hypothesis-testing | route | statistical-significance decision rule, distinct from `product-discovery-hypothesis-testing`'s product framing; sharpen trigger to flag that distinction explicitly to avoid mis-routing |
| experiment-trust | merge-retire | duplicate of `growth-analytics-experiment-trust`; retire standalone orphan, supersede pointing at the family-routed copy |
| team-safety-measure | reclassify | culture/retro-level judgment, no owning role |
| tech-feasibility | merge-retire | superseded in substance by the 9-skill `technical-feasibility-*` family; fold any unique umbrella content into `technical-feasibility-verdict-and-timebox-selection`, supersede |
| silent-failure-audit | route | already has a sharp, concrete trigger; needs BM25 pool inclusion tuning, not a rewrite |
| work-in-english | reclassify | policy skill governing all work regardless of role; explicitly orchestrator-level per its own trigger |
| prose-modes | route | cross-cutting writing-style routing; sharpen trigger to name the two axes it routes on, so it's picked before `technical-writing-*` narrows to docs only |
| market-recon | **exclude — already mounted** | 8 explicit `Skill`-tool invocations found in logs; structural proxy false-positived this one, corrected by the census signal |

Remaining catalog skills matching the structural "orphan" test were not exhaustively enumerated here given the phase-1 time budget; the census script (step 1) plus the same route/reclassify/merge-retire criteria close the gap to the confirmed 42 in phase 2.

## Out of scope

- `design-artifact-*` and `knowledge-work-deck-*` (8 skills) — excluded, landed within the 7-day window.
- Re-deriving the original orchestrator's exact `614`-log corpus location — flagged as an open finding for the approver to resolve (point the census script at the right corpus, or confirm the structural proxy is an acceptable substitute).
- Any skill with an observed mount signal (however small) — this pass only classifies zero-mount skills.

## How you'll know it worked

- `docs/issue-63/reports/knowledge-management/curation-table.md` lists every confirmed never-mounted skill with a verdict and reason, verdict counts stated.
- Every route-verdict skill's `SKILL.md` has a condition-sharpened `Use-when` line (diffable in the phase-2 PR).
- Every merge-retire skill has a supersession note pointing at its survivor; no file is silently deleted.
- `python3 scripts/check_skill_conformance.py` exits 0 over the full repo after phase-2 edits land.
