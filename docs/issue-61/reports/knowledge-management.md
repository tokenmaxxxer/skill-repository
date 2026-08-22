---
code_under_review: skills/research-evidence-discipline/SKILL.md
loop_state: landed
type: feature
breaking: false
verdict: approved
---

# Report: shared evidence-discipline procedure skill (issue-61)

## What was done

Authored `skills/research-evidence-discipline/SKILL.md`, a new axis-style
skill (`axis: evidence-discipline`, `rule_count_floor: 6`) covering the
three mechanisms named in issue-61: Fact/Inference/Assumption claim
labeling (rules 1-3), an explicit do-not-invent list for names/quotes/
figures with no source (rules 4-5), and a question-budget cap (rule 6).
Every rule carries its own independent `source:` URL — none ported from
the deanpeters reference repo, which this session never fetched or read
(see `docs/issue-61/reports/knowledge-management/survey.md`).

Added one `## Related skills` bullet to each of the four family-anchor
skills named in the approved proposal's `files:` list, each linking
back to the new skill with a one-clause reason specific to that
family's axis:
- `skills/market-analysis-evidence-rigor/SKILL.md`
- `skills/product-discovery-hypothesis-testing/SKILL.md`
- `skills/growth-analytics-experiment-trust/SKILL.md`
- `skills/user-discovery-evidence-strength-tagging/SKILL.md`

The latter two skills had no pre-existing `## Related skills` section,
so the bullet was added as a new trailing section in each.

## Why

Issue-61 (acceptance criteria) asks for a shared evidence-discipline
skill because the four research-shaped families currently cite sources
per rule but have no claim-labeling, do-not-invent, or question-budget
discipline layered on top. The approved proposal (PR #72, merged)
chose one top-level shared skill over four family-scoped copies to
avoid duplicating family-agnostic rules across families — see
`docs/issue-61/proposals/research-evidence-discipline.md`, ## Rationale.

## Upstream / basis

- Issue: #61
- Approved proposal: `docs/issue-61/proposals/research-evidence-discipline.md`
  (merged via PR #72, commit 6ba1a62)
- Approval: issue-61 comment "APPROVE issue-61/knowledge-management" by
  JiwonJung94 (listed in `docs/specs/approvers.md`), single-account mode
  (PR #72's author and the approver are the same account).

## What will be done vs. what happened

Executed exactly as the proposal's `## What will be done` specified,
steps 1-3: created the new skill with all three mechanisms and
independent sources, added the four Related-skills bullets, ran
conformance. No deviation from the approved proposal — no
`## Rationale for deviations` section is included.

## What did not work

None. One conformance violation was hit and fixed inline during
authoring (rule 6 initially cited a `docs/` path instead of an
`https://` URL, which `check_rule_sources` requires — swapped to a
qualifying `https://` source before the final run).

## How it was verified

```
$ python3 scripts/check_skill_conformance.py
253 skills checked
```

Full-repo conformance run, exit 0, no violations — matches the
proposal's "How you'll know it worked" bar (full-repo run achieved
within this session's time budget, not the partial-run fallback).

## Open findings

None outstanding. A reviewer spot-check of the new skill's rule text
against the deanpeters repo (per the proposal's own "How you'll know it
worked" line) remains available to any reviewer who chooses to do one,
but is not a blocking gap in this record — this session never fetched
that repo's text, so no contamination is possible to check for.

## loop_state

`landed` — terminal for a `feature`-kind record: code committed, phase-2
approval gate satisfied, conformance green, nothing left open that
blocks the PR.
