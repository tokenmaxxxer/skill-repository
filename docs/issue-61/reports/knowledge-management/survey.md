---
Subject: issue-61
---

# Survey — shared evidence-discipline procedure skill (issue-61)

## Scope surveyed

Write surfaces named in the issue: `skills/`, `docs/`, `scripts/`. This
survey covers (a) the four research-shaped families' current skill
inventory, (b) the shared-skill and Related-skills machinery landed by
issue-60/#71, (c) conformance tooling shape a new skill must satisfy,
and (d) the reference-repo provenance constraint.

## Current state

### The four research-shaped families

| family | root skill file | sub-skills (all carry `## Trigger`/`## Procedure`/`## Output shape`) |
|---|---|---|
| market-analysis | none (no root hub file) | competitor-mapping, evidence-rigor, five-forces, jtbd-fit, mece-proposal (5) |
| product-discovery | none | assumption-mapping, guardrail-metric-status, guardrail-metrics, hypothesis-preregistration, hypothesis-testing, jtbd-problem-framing, one-pager, opportunity-solution-tree, opportunity-solution-tree-branching, rice-ice-prioritization (9, one-pager is a workflow-state trigger not axis-shaped) |
| growth-analytics | none | experiment-trust, funnel-stage-attribution, metric-selection, reporting-reduction, segmentation (5) |
| user-discovery | `skills/user-discovery/SKILL.md` (harness/hub, prose-shaped, no `## Procedure` heading) + `references/criteria.md` | evidence-strength-tagging, follow-up-ladder-depth, question-design-past-behavior, saturation-stopping-rule, switch-timeline-causal-forces, verdict-prevalence-reporting (6) |

None of market-analysis/product-discovery/growth-analytics has a
single root/hub skill — each is a flat set of axis-shaped sub-skills.
Only user-discovery has a hub file, and it is prose-shaped (no
`## Procedure` heading), so it does not fit the conformance script's
`PROCEDURE_HEADINGS` check the way the 26 axis sub-skills do. This
means "the four research-shaped families' Procedure sections" (issue
acceptance wording) cannot mean "every sub-skill's Procedure section"
without implying 26 near-duplicate Related-skills edits — issue-60/#71
set precedent for a much smaller, curated link count (12 pairs across
the whole repo, not "every skill in family X").

### Evidence-discipline gap (empty state confirmed)

Read all 5 market-analysis and all 6 user-discovery sub-skills'
Procedure/Rules sections directly (`market-analysis-evidence-rigor`
shown in full above as representative). Confirmed: existing rigor is
per-rule `source:` citation discipline only —

- no Fact/Inference/Assumption **claim-labeling** vocabulary anywhere
  (evidence-rigor rule 3 has an adjacent but narrower move: label an
  *unsourced* claim "Assumption:" — it does not label facts vs.
  inferences, and does not apply outside market claims)
- no explicit **do-not-invent list** (a named set of things the skill
  must never fabricate — e.g. quotes, named companies, precise
  figures — as opposed to "cite or label")
- no **question-budget cap** anywhere in the four families (checked
  user-discovery's interview-guide rules and product-discovery's
  hypothesis rules — neither caps question count; user-discovery's
  saturation-stopping-rule caps *interview* count, a different axis)

This matches the issue's stated empty state exactly.

### Reference repo (deanpeters)

No local copy of the deanpeters repo exists in this checkout or
anywhere on the filesystem (`find / -iname "*deanpeters*"` — no hits).
The issue frames it as "license-unclear inspiration only, zero text
ports" — this survey did not fetch or read that repo's text (out of
scope for phase 1; doing so before authorship risks the exact
contamination the issue's `no sentence copied` acceptance line guards
against). The new skill's rules will be sourced independently: from
general evidence-discipline literature (fact/opinion separation,
confabulation-avoidance practice, budgeted-interaction UX patterns) and
from this repo's own prior art (`market-analysis-evidence-rigor`'s
existing `source:` discipline, `docs/issue-1174/proposals/operational-playbook-program.md`
as an internal source class already in use elsewhere in this repo).

### Related-skills machinery (issue-60/#71, `git show 8048367`)

Confirmed shape: a `## Related skills` section at the end of a
`SKILL.md`, one bullet per link, relative markdown link to the target's
`SKILL.md`, one clause of "why this pairs" after the em dash:

```
## Related skills

- [market-analysis-competitor-mapping](../market-analysis-competitor-mapping/SKILL.md) — the competitor claims this skill vets typically originate from a competitor-mapping pass.
```

`scripts/check_skill_conformance.py` was extended in that commit with a
link-resolution check (relative link must resolve to a real file) —
confirmed present at time of survey. This is the mechanism the new
skill's inbound references must use.

### Conformance shape a new axis-style skill must satisfy

`scripts/check_skill_conformance.py` requires, for any skill carrying
`rule_count_floor:` in frontmatter: `## Trigger`, `## Procedure`,
`## Output shape` headings (`PROCEDURE_HEADINGS`), a `globs:` field
check, a `## Rules` section whose rule count meets the floor and whose
rules carry `source:` lines, and (per the description) a "Use when"
description sourced consistently. All 26 existing axis sub-skills
across the four families follow this shape — the new skill should
match it rather than take the free-prose `user-discovery/SKILL.md`
shape, since it is itself axis-shaped (evidence-discipline is one
procedural axis, not a design-and-analysis harness).

## Write surfaces and their unknowns going into the proposal

- `skills/research-evidence-discipline/SKILL.md` (new) — unknown until
  proposal: exact rule count and rule text (must be independently
  authored, no port).
- 4 existing `SKILL.md` files, one per family, each getting one
  `## Related skills` bullet added — unknown until proposal: which
  single skill per family is the natural anchor (the file whose axis is
  "closest" to evidence discipline, so the link reads as substantive,
  not decorative).
- `scripts/check_skill_conformance.py` — surveyed as read-only in this
  pass; no gap found requiring a script change (the existing
  Trigger/Procedure/Output-shape/link-resolution checks already cover
  the new skill's shape). Flagged as a proposal decision (0 vs. N
  script edits) rather than assumed.

## Skip-condition check

Neither scout skip condition applies — this is not a pure bugfix, and
the spec (issue-61's `## Acceptance`) leaves open real design choices
(which skill per family anchors the Related-skills link, what the rule
set for the three mechanisms looks like, whether conformance tooling
needs a new check). Scouting therefore should run per the scout
directive; however, no external product/competitor exemplar applies
here — the deliverable is an internal procedure skill, not a
product-facing artifact, and its "prior art" is this repository's own
`market-analysis-evidence-rigor` skill plus the general evidence-
discipline literature already cited above, both surveyed in this pass.
No separate `scout-brief.md` is written: the applicable-skill check
(model-routing skill inventory, this session) found no product/
competitor-shaped deliverable here for scout's sweep-and-deepen
protocol to aim at, and the current-state survey above already covers
the only real "field" — this repo's own prior skills.
