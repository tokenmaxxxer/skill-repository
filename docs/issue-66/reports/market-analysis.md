---
Subject: issue-66
code_under_review: pending
loop_state: phase-2-complete
type: feature
breaking: false
verdict: pass
---

# Phase-2 record: business-model-design skill family

## What was done

Authored the four `business-model-design-*` skills specified in the
merged phase-1 proposal (`docs/issue-66/proposals/business-model-design-skill-family.md`,
PR #68), exactly as proposed — no addition, no removal, no substitution:

- `business-model-design-canvas-construction` — BMC vs. Lean Canvas
  selection by stage, block fill order, desirability-before-viability
  sequencing, and canvas construction failure modes.
- `business-model-design-revenue-model-selection` — subscription vs.
  usage-based vs. freemium vs. marketplace/take-rate archetype
  selection by value-metric alignment, end-user type, and stage.
- `business-model-design-value-proposition-fit` — Value Proposition
  Canvas construction (Customer Profile before Value Map, one segment
  at a time) and fit-validation failure modes.
- `business-model-design-platform-design` — two-sided/multi-sided
  platform subsidize-side selection, take-rate/governance/design as a
  joint decision, multi-homing risk, and cold-start launch sequencing.

Each skill carries `name`/`description` (with a "Use when..." trigger),
`axis:`/`rule_count_floor:` frontmatter, `## Trigger` / `## Procedure`
/ `## Output shape` / `## Rules` bodies with per-rule `source:`
citations (5-7 rules each, at least one `[removal]`-tagged rule per
skill, following the flat-numbered-list convention the survey
identified as this repo's majority pattern), and a `## Related skills`
section cross-referencing `pricing-*`/`finance-unit-economics-*`/
`market-analysis-jtbd-fit` exactly as the proposal specified.

`python3 scripts/check_skill_conformance.py` passes over the full
repository: 252 skills checked, 0 failures (248 pre-existing + 4 new).
`python3 -m pytest test/test_check_skill_conformance.py -q`: 9 passed.

## Why

Issue #66 (operator direction 2026-08-22, professional-discipline gap
#1 of 5): skill-repository had `pricing-*` and `finance-unit-economics-*`
skills that assume a business model and revenue model are already
chosen, but no skill covering how to construct a business-model canvas,
select a revenue-model archetype, validate value-proposition fit, or
design a two-sided platform in the first place. This closes that gap
exactly as scoped by the merged proposal.

## Upstream

`docs/issue-66/proposals/business-model-design-skill-family.md` (merged
via PR #68), grounded in `docs/issue-66/reports/market-analysis/survey.md`.

## Research sources (restated per acceptance)

- https://www.strategyzer.com/business-models-the-toolkit-to-design-a-disruptive-company
- https://www.strategyzer.com/library/5-common-mistakes-to-avoid-when-using-the-value-proposition-canvas
- https://www.strategyzer.com/library/the-value-proposition-canvas
- https://www.strategyzer.com/library/business-model-generation-book-summary
- https://s3.amazonaws.com/leanstack/v4/Lean-Canvas.pdf
- https://www.leanfoundry.com/articles/why-lean-canvas-versus-business-model-canvas
- https://medium.com/lean-stack/what-is-the-right-fill-order-for-a-lean-canvas-f8071d0c6c8c
- https://medium.com/lean-stack/why-lean-canvas-vs-business-model-canvas-af62c0f250f0
- https://blog.leanstack.com/the-updated-problem-interview-script-and-a-new-canvas-1e43ff267a5d
- https://medium.com/lean-stack/love-the-problem-not-your-solution-65cfbfb1916b
- https://openviewpartners.com/usage-based-pricing/
- https://a16z.com/usage-based-pricing-rule-of-thumb/
- https://a16z.com/podcast/ai-is-upending-saas-pricing/
- https://www.bvp.com/atlas/state-of-the-cloud-2023
- https://www.forentrepreneurs.com/saas-metrics-2/
- https://openviewpartners.com/blog/2023-pricing-data/
- https://www.tse-fr.eu/sites/default/files/medias/doc/wp/2002/platform.pdf
- https://web.mit.edu/14.271/www/rochet_tirole.pdf
- https://www.hbs.edu/faculty/Pages/item.aspx?num=44940
- https://sloanreview.mit.edu/article/strategic-decisions-for-multisided-platforms/
- https://www.nfx.com/post/network-effects-manual

## What did not work

None.

## Open findings

None — all four skills pass conformance, and their `Related-skills`
cross-references (`pricing-method-family`, `pricing-tier-structure`,
`pricing-verdict-report`, `finance-unit-economics-proposal-shape`,
`finance-unit-economics-ltv-cac-band`, `market-analysis-jtbd-fit`) all
resolve to real, existing skill directories confirmed present under
`skills/`.

## kind

implementation
