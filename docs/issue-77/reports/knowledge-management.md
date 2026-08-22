---
code_under_review: skills/org-design-hiring-rubric-structured-interview/SKILL.md, skills/org-design-role-competency-definition/SKILL.md, skills/org-design-team-shape-selection/SKILL.md
loop_state: landed
type: feature
breaking: false
verdict: approved
---

# Report: organization/HR-design skill family (issue-77)

## What was done

Authored the `org-design-*` family of three skills exactly as named in
the approved proposal
(`docs/issue-77/proposals/org-design-skill-family.md`):

- `skills/org-design-hiring-rubric-structured-interview/SKILL.md`
  (`axis: interview-structure-vs-validity-tradeoff`,
  `rule_count_floor: 3`) — the structured-vs-unstructured definition,
  the honest r=.51/r=.38 validity claim, and the
  complement-not-substitute rule against a work-sample/GMA measure.
- `skills/org-design-role-competency-definition/SKILL.md`
  (`axis: threshold-vs-differentiating-competency`,
  `rule_count_floor: 3`) — the threshold/differentiating tagging rule,
  the untagged-flat-list authoring-defect rule, and the
  falsifiable-performance-expectation (OKR/SMART) rule.
- `skills/org-design-team-shape-selection/SKILL.md`
  (`axis: team-type-and-interaction-mode-by-cognitive-load`,
  `rule_count_floor: 3`) — the four-team-type classification, the
  three-interaction-mode classification, and the
  facilitating-should-end rule.

Each skill carries a distinct condition-matched `description` ("Use
when...", with an explicit "Do NOT use" clause pointing at its nearest
sibling or `team-safety-measure`), a `## Trigger`/`## Procedure`/
`## Output shape`/`## Decision rules` body, and per-rule `source:` +
`counter-example:` lines citing the primary sources captured in
`docs/issue-77/reports/knowledge-management/survey.md`. `## Related
skills` sections cross-reference `team-safety-measure` and
`partnerships-bd-negotiation-positioning` (both confirmed present
under `skills/`) plus the sibling `org-design-*` skills, matching the
proposal's chaining plan.

## Why

Issue-77 (professional-discipline gap #3) named an empty state: no
skill covered hiring rubrics, role/competency definition, or
team-shape selection; `team-safety-measure` was the only adjacent
skill. The approved proposal chose a 3-skill axis split (hiring rubric
vs. role/competency vs. team shape) over a 4-skill split with a
free-standing OKR/SMART skill, or a single merged
hiring-and-role-design skill — see
`docs/issue-77/proposals/org-design-skill-family.md`, `## Rationale`,
for both rejected alternatives and why each was rejected.

## Upstream / basis

- Issue: #77
- Approved proposal: `docs/issue-77/proposals/org-design-skill-family.md`
  (merged via PR #78, commit 8d9ddc3)
- Approval: issue-77 comment "APPROVE issue-77/knowledge-management" by
  JiwonJung94 (listed in `docs/specs/approvers.md`), single-account mode
  (PR #78's author and the approver are the same account).

## What will be done vs. what happened

Executed exactly as the proposal's `## What will be done` specified:
authored the three named skills with the named axes, "Use when"
triggers, rule seeds traced to the survey's four scouted angles (Angle
4's OKR/SMART lineage folded into the role/competency skill's rule 3,
per the proposal's Rationale), and the `Related-skills` cross-references
named in the proposal. No existing skill file (`team-safety-measure`,
`partnerships-bd-*`) was touched, matching the proposal's `## Out of
scope`. No fourth free-standing OKR/SMART skill was created. No
deviation from the approved proposal — no `## Rationale for deviations`
section is included.

An earlier attempt in this branch's history (commits `f64b74a`,
`619387b`, `a00288d`, `8776c68`) duplicated the already-merged phase-1
content and left only `consult-log.md` timeout-error entries beyond
that; that stray PR (#80) was closed unmerged. This record supersedes
that dead end: the branch was reset to `origin/main` (which already
carries the merged phase-1 commit `8d9ddc3`) before phase-2 authoring
started, so no duplicate or error-only commit is part of this PR's
history.

## Doc-placement ladder

- [x] `docs/issue-77/reports/knowledge-management/survey.md` — phase-1, already committed (PR #78).
- [x] `docs/issue-77/proposals/org-design-skill-family.md` — phase-1, already committed (PR #78).
- [x] `docs/issue-77/reports/knowledge-management.md` — this record, phase-2.
- [x] `skills/org-design-hiring-rubric-structured-interview/SKILL.md` — new skill, phase-2.
- [x] `skills/org-design-role-competency-definition/SKILL.md` — new skill, phase-2.
- [x] `skills/org-design-team-shape-selection/SKILL.md` — new skill, phase-2.

## What did not work

None in this pass. (A prior session's attempt hit repeated
`skill_judge` consult timeouts, visible in `docs/issue-77/reports/
consult-log.md`, and produced no skill files — see the note under
`## What will be done vs. what happened` above for how this pass
recovered from that.)

## How it was verified

```
$ python3 scripts/check_skill_conformance.py
259 skills checked
```

Full-repo conformance run, exit 0, no violations — matches the issue's
acceptance criterion ("conformance green over the full repo").

## Skill-verdict log (issue #2039)

- skill-verdict: knowledge-management-curation-pruning — not-applicable: this task authors new org-design skills, not a review of an uncited or flagged knowledge-library entry.
- skill-verdict: knowledge-management-structure-findability — not-applicable: skill placement/naming here follows this repo's own SKILL.md schema and sibling-family convention (verified against `ux-engineering-service-design-*`), not the Diátaxis document-type classification this skill governs.
- skill-verdict: knowledge-management-taxonomy-tagging — not-applicable: no controlled-vocabulary term is being added, merged, or scoped; `axis:` values here are this repo's own skill-schema field, not a taxonomy tag.
- skill-verdict: knowledge-management-supersession-lifecycle — not-applicable: no existing knowledge-library entry is being replaced, dropped, or edited; these are net-new skill files.
- skill-verdict: knowledge-management-pattern-extraction — not-applicable: no retrospective is being mined for a candidate lesson; the three skills' rules were sourced directly from primary literature in the phase-1 survey, not extracted from an issue retrospective.
- skill-verdict: market-analysis-mece-proposal — not-applicable: this session is phase-2 (skill authoring against an already-approved and merged proposal), not drafting or restructuring a phase-1 proposal's section set.
- skill-verdict: finance-unit-economics-ltv-cac-band — not-applicable: no LTV:CAC ratio, CAC band, or unit-economics content is involved in an org-design skill family.

## Open findings

None outstanding.

## loop_state

`landed` — terminal for a `feature`-kind record: code committed,
phase-2 approval gate satisfied, conformance green, nothing left open
that blocks the PR.
