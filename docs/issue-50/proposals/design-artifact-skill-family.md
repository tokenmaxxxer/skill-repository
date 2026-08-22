---
status: proposed
files:
  - skills/design-artifact-storyboard/SKILL.md
  - skills/design-artifact-information-architecture/SKILL.md
  - skills/design-artifact-user-flow/SKILL.md
  - skills/design-artifact-user-scenario/SKILL.md
  - skills/design-artifact-html-demo/SKILL.md
---

# Design-artifact skill family (issue #50)

## Request

Add a condition-matched skill family for authoring UX design artifacts —
storyboard, information architecture, user flow, user scenario/journey,
and HTML/CSS demo construction — each source-anchored (NN/g, ISO
9241-210, design-system/MDN docs), each with a Use-when trigger and
`scripts/check_skill_conformance.py`-passing shape, with research
sources recorded in this PR body. This is program artifact-gate phase
5, independent of phases 1-4.

No scout-skip condition applies: this proposal follows a completed
current-state survey and scout pass, recorded at
`docs/issue-50/reports/ux-engineering/survey.md` and
`docs/issue-50/reports/ux-engineering/scout-brief.md` (this role's own
record area per contract v3 s11 — `docs/issue-50/reports/implementation/`
belongs to a different role and is not used here).

## Constraints

- Must follow the existing conformance shape used by all 240 current
  skills: frontmatter `name`/`description` (with a "use when" trigger
  clause), body `## Trigger` / `## Procedure` / `## Output shape` /
  `## Decision rules`, each decision rule carrying a `source:` line
  with a live http(s) URL.
  `python3 scripts/check_skill_conformance.py` must stay green.
- ≥4 skills required by acceptance; issue names 5 (storyboard, IA,
  user-flow, user-scenario, html-demo) — deliver all 5.
- Each skill must be genuinely condition-matched (a distinct trigger,
  not a reworded duplicate of another skill in the family or of the
  existing `ux-engineering-*` family).
- Phase-1 only: this PR delivers survey + proposal; no `skills/` files
  land until a human Approve reopens phase 2.

## Rationale

Two structural questions needed a decision before writing rules:
naming/namespace, and how many skills to split the "user-scenario"
territory into.

**Naming**: considered folding these five into the existing
`ux-engineering-*` prefix (e.g. `ux-engineering-storyboard`) to keep one
flat namespace. Rejected: the `ux-engineering-*` family's existing 6
skills all govern in-screen, already-scoped decisions (which color,
which control, which nav depth) — reviewed against the actual
`SKILL.md` bodies during the survey. The new family instead governs
which artifact to produce and how to structure it, upstream of any
single screen. Mixing the two under one prefix would make the prefix
stop signaling "in-screen decision" and force every trigger sentence to
carry disambiguating text the axis-based naming currently avoids.
Using a distinct `design-artifact-*` prefix keeps each family's prefix
load-bearing.

**User flow vs. user scenario as one skill or two**: considered
merging user-flow and user-scenario/journey into a single
"user-journey" skill, since a shallow reading of the issue text treats
them as near-synonyms. Rejected after the scout pass: NN/g's own
published distinction (fetched during scouting,
https://www.nngroup.com/articles/user-journeys-vs-user-flows/) treats
these as different-scope artifacts — user flow is micro/single-product/
steps-and-system-responses-only, user journey is macro/multi-channel/
includes emotions-and-thoughts over days-to-months — with different
authoring failure modes (a flow padded with journey-style emotional
narrative becomes unusable as an implementation spec; a journey map
collapsed to flow-level steps loses the cross-channel context it exists
to capture). Collapsing them into one skill would erase exactly the
distinction practitioners rely on to pick the right artifact, so they
stay separate per the issue's original naming.

## What will be done

Phase 2 (after Approve) will author five `SKILL.md` files under
`skills/design-artifact-<name>/`, each following the conformance shape
verified in the survey:

1. **design-artifact-storyboard** — trigger: authoring a
   sequence-of-panels storyboard for a user story/workflow. Rules
   anchored on NN/g's storyboard guidance (chronological panel
   sequence, not a single static screen).
2. **design-artifact-information-architecture** — trigger: structuring/
   labeling a site or app's content hierarchy. Rules anchored on NN/g's
   IA study guide (3-click-rule myth, flat-vs-deep hierarchy tradeoffs,
   label information-scent, polyhierarchies for category outliers).
3. **design-artifact-user-flow** — trigger: diagramming the discrete
   step-by-step interaction path through one product task. Rules
   anchored on NN/g's user-flow definition and wireflow/flowchart
   artifact guidance, explicitly scoped away from journey-map territory.
4. **design-artifact-user-scenario** — trigger: writing a user
   scenario, persona, or cross-channel journey map. Rules anchored on
   ISO 9241-210's HCD process (context-of-use → user profiles →
   as-is scenarios/personas → iterative refinement via
   scenarios+prototypes) and NN/g's journey-map definition.
5. **design-artifact-html-demo** — trigger: building an HTML/CSS demo
   or no-build single-file prototype. Rules anchored on MDN's semantic-
   HTML accessibility baseline (semantic elements over generic divs,
   single h1 / no skipped heading levels, native interactive elements)
   plus responsive-default guidance.

Each skill gets `## Trigger`, `## Procedure`, `## Output shape`, and
`## Decision rules` (≥3 rules per skill, each with `source:` + a
`counter-example:` or `rationale:` line, matching the observed
convention across the 6 existing `ux-engineering-*` skills), plus
`axis:` and `rule_count_floor:` frontmatter for consistency.
`python3 scripts/check_skill_conformance.py` will be run and confirmed
green before the phase-2 record is written. Research sources (the
scout brief's `Sources:` list) will be restated in the phase-2 PR body
per acceptance's "sources recorded in the issue/PR body" requirement.

## Out of scope

- Card-sorting/tree-testing methodology (research method, not artifact-
  authoring rule) — the IA skill cites it as evidence input only.
- Editing or renaming any existing `ux-engineering-*` skill.
- Any actual `skills/design-artifact-*` file — those are phase-2 output,
  gated on Approve.
- A shared/umbrella "design-artifact" index skill — the issue asks for
  5 condition-matched skills, not a meta-skill; each stands on its own
  trigger.

## How you'll know it worked

- `skills/` contains 5 new `design-artifact-*` directories, each with a
  conformant `SKILL.md` (Use-when trigger line, source-anchored rules).
- `python3 scripts/check_skill_conformance.py` exits 0 over the full
  repository (currently 240 skills; will read 245 after phase 2).
- The phase-2 PR body records the research sources used (NN/g, ISO
  9241-210 PDF, MDN — the URLs in this survey's scout brief).
