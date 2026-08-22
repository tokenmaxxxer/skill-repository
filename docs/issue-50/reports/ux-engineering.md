---
Subject: issue-50
code_under_review: pending
loop_state: phase-2-complete
type: feature
breaking: false
verdict: pass
---

# Phase-2 record: design-artifact skill family

## What was done

Authored five new skills under `skills/design-artifact-*/`, per the
merged phase-1 proposal (`docs/issue-50/proposals/design-artifact-skill-family.md`,
PR #51):

- `design-artifact-storyboard` — sequence-of-panels storyboard authoring.
- `design-artifact-information-architecture` — content hierarchy/labeling,
  including a rule explicitly refuting the "3-click rule" myth.
- `design-artifact-user-flow` — micro-scope, single-product step diagrams,
  explicitly scoped away from journey-map territory.
- `design-artifact-user-scenario` — macro-scope scenario/persona/journey
  writing grounded in ISO 9241-210's HCD process.
- `design-artifact-html-demo` — semantic-HTML, no-build single-file demo
  construction with accessible/responsive defaults.

Each skill carries `name`/`description` (with a "Use when..." trigger),
`axis:`/`rule_count_floor:` frontmatter, and `## Trigger` / `## Procedure`
/ `## Output shape` / `## Decision rules` bodies with ≥3 source-anchored
rules (at least one `REMOVAL:`-tagged rule per skill), matching the
conformance shape of the existing `ux-engineering-*` family.

`python3 scripts/check_skill_conformance.py` passes over the full
repository: 245 skills checked, 0 failures (240 pre-existing + 5 new).

## Why

Program artifact-gate phase 5 (issue #50): skill-repository has
`ux-engineering-*` skills for in-screen decisions but none for authoring
the design *artifacts* (storyboard, IA, user flow, user scenario) or the
HTML-demo construction step that precede/follow those decisions. This
closes that gap per the issue's frozen Acceptance.

## Upstream

`docs/issue-50/proposals/design-artifact-skill-family.md` (merged via
PR #51), grounded in `docs/issue-50/reports/ux-engineering/survey.md`
and `docs/issue-50/reports/ux-engineering/scout-brief.md`.

## Research sources (restated per acceptance)

- https://www.nngroup.com/videos/ux-storyboard/
- https://www.nngroup.com/articles/user-journeys-vs-user-flows/
- https://www.nngroup.com/articles/ia-study-guide/
- https://www.nngroup.com/reports/topic/information-architecture/
- https://richardcornish.s3.amazonaws.com/static/pdfs/iso-9241-210.pdf
- https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML

## What did not work

None.

## Open findings

None — all five skills pass conformance and match the proposal's
per-skill trigger/scope split (flow vs. scenario distinction preserved
as separate skills, per the proposal's Rationale).

## kind

implementation
