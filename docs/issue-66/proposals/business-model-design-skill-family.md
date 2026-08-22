---
status: proposed
files:
  - docs/issue-66/reports/market-analysis/survey.md
  - docs/issue-66/proposals/business-model-design-skill-family.md
---

# Business-model-design skill family (phase 1: research + proposal)

Note on survey location (scout-skip-adjacent note, no design decision
left open by this path choice): this is a market-analysis role
deliverable, not an implementation role deliverable. The
current-state survey required by the survey-before-proposal norm
already exists on disk at
`docs/issue-66/reports/market-analysis/survey.md` (role-scoped per
contract v3 s11/s19), not at the generic
`docs/issue-66/reports/implementation/survey.md` path, since this role
is barred from writing into another role's `reports/implementation/`
tree (board-gate). No design decision remains open beyond what that
survey and this proposal already resolve (the four-skill split below)
— there is nothing a second survey copy at the implementation path
would add.

## Request

Issue #66 (operator direction 2026-08-22, "BM 설계 같은 것도 다
스킬화" — professional-discipline gap #1 of 5): research-first survey
of practitioner business-model-design methodology using primary
sources (Osterwalder/Strategyzer BMC + VPC, Ash Maurya's Lean Canvas,
revenue-model taxonomies, two-sided/platform design literature — the
deanpeters PM-Skills pack is inspiration-only, license-unclear, no
text port), then propose a `business-model-design-*` skill family of
>=4 skills (canvas construction, revenue-model selection,
value-proposition fit, platform/two-sided-market design), each with a
condition-matched "Use when" trigger and per-rule `source:` citations,
cross-referenced with the existing `pricing-*` and
`finance-unit-economics-*` families. Phase 1 (survey + proposal) only;
authoring the actual `skills/business-model-design-*/SKILL.md` files
is phase-2, gated on approval.

## Constraints

- Every rule proposed below must trace to a primary source with a live
  URL (issue acceptance criterion) — verified in `survey.md`.
- >=4 skills, axis-split, no content overlap between them (MECE across
  the family).
- Each skill's `description` must carry a "Use when..." trigger
  distinguishing it from its siblings and from `pricing-*`/
  `finance-unit-economics-*`.
- `Related-skills` cross-references to `pricing-*`/
  `finance-unit-economics-*` must resolve to real, existing skill
  directory names.
- `scripts/check_skill_conformance.py` must stay green once phase-2
  authors the actual SKILL.md files — this proposal's schema choices
  are constrained by that script's requirements (frontmatter
  `name`/`description`/`axis`/`rule_count_floor`, per-rule `source:`
  lines under `## Rules`).
- No sentence copied from deanpeters/Product-Manager-Skills or any
  license-unclear reference — every rule below is drawn from the
  primary sources found in `survey.md`, independently worded.

## Rationale

Two structural alternatives were considered for *how* to split the
family, given what the survey found:

1. **One single `business-model-design` skill covering all four
   methodology angles (BMC/VPC, Lean Canvas, revenue models, platform
   design) in one file.** Rejected: the survey found each angle has
   its own distinct trigger condition (constructing a canvas vs.
   choosing a revenue archetype vs. validating value-prop fit vs.
   designing a two-sided model are different moments in a founder's
   workflow, not steps of one linear procedure), and this repo's own
   convention — confirmed across `pricing-*` (5 skills) and
   `finance-unit-economics-*` (6 skills) — is to split by decision
   axis specifically so an agent cites only the narrow skill matching
   the decision actually in front of it. A single mega-skill would
   force every invocation to load four unrelated rule sets and break
   the axis-triggered dispatch pattern the rest of the repo relies on.
2. **Split BMC and Lean Canvas into two separate "canvas" skills
   (one per canvas type) instead of one shared `canvas-construction`
   skill that routes between them.** Rejected: the survey's Angle 2
   finding is explicit that Lean Canvas *is* BMC's blocks minus four,
   plus four different ones, selected by the same underlying decision
   (pre-PMF startup vs. established business) — Maurya's own primary
   source frames this as one choice with two canvas shapes, not two
   independent methodologies. Splitting them would duplicate the
   shared sequencing logic (fill customer/problem-first, cost/revenue
   last) in two files and make the startup-vs-established routing rule
   invisible to whichever skill an agent reaches for first. One
   `canvas-construction` skill, with a rule for choosing which canvas
   shape to use, keeps that shared logic in one place.

## What will be done

`survey.md` (already written, listed in `files:`) documents the
primary-source findings across all four methodology angles, each with
a live URL. This proposal specifies the four skills to author in
phase 2.

### Proposed family: `business-model-design-*` (4 skills)

1. **`business-model-design-canvas-construction`**
   - Axis: canvas construction (BMC vs. Lean Canvas selection, block
     fill order, desirability-before-viability sequencing).
   - Use when: choosing between the Business Model Canvas and Lean
     Canvas for a given business stage, filling a canvas's blocks in
     an order that surfaces the riskiest assumption last (or
     desirability before feasibility/viability), or checking a filled
     canvas for a known construction failure mode.
   - Rule seeds (from survey Angles 1-2): BMC's 9 blocks group into
     Desirability/Feasibility/Viability, filled in that order, with
     Cost Structure derived last; Lean Canvas selection rule
     (pre-PMF startup vs. established business); Lean Canvas fill
     order (Problem+Customer first, Unfair Advantage last,
     riskiest-assumption-last sequencing); Problem Interview
     validation before Solution; "living hypothesis document, not a
     static plan" anti-pattern.
   - Related-skills: `pricing-method-family` (once a business model is
     canvased, revenue-model selection routes there for
     pricing-specific method choice), `finance-unit-economics-proposal-shape`.

2. **`business-model-design-revenue-model-selection`**
   - Axis: revenue-model archetype selection (subscription vs.
     usage-based vs. freemium vs. marketplace/take-rate vs. licensing).
   - Use when: choosing a revenue-model archetype for a new or
     changing business model based on value-metric alignment,
     end-user type (human vs. machine), product consumption pattern,
     or company stage — upstream of `pricing-method-family`, which
     picks a *research method* to price within an archetype already
     chosen here.
   - Rule seeds (from survey Angle 3): value-metric-alignment rule
     (track customer value, not cost to serve); human-vs-machine
     end-user split (subscription vs. usage-based); AI-product
     seats-to-output shift; usage-based-as-NRR-driver rule with
     Bessemer's 100/110/120% bands; freemium vs. marketplace
     archetype selection; early-stage adoption-over-extraction
     sequencing rule; usage-based mainstream-adoption benchmark signal.
   - Related-skills: `pricing-method-family`, `pricing-tier-structure`,
     `finance-unit-economics-ltv-cac-band` (revenue-model choice feeds
     the LTV assumptions that skill bands).

3. **`business-model-design-value-proposition-fit`**
   - Axis: value-proposition fit (VPC construction and fit validation,
     distinct from canvas construction's whole-BMC/Lean-Canvas
     sequencing).
   - Use when: building a Value Proposition Canvas's Customer Profile
     or Value Map for a single segment, judging whether a value
     proposition has achieved "fit" against evidence, or checking a
     value proposition for a named fit-validation failure mode
     (solution-first bias, blended segments, comprehensive-coverage
     trap, functional-only jobs).
   - Rule seeds (from survey Angle 1): Customer-Profile-before-
     Value-Map sequencing per segment; never blend segments; fit as
     iterative evidence-based state, not one-time fill; solution-first
     bias and comprehensive-coverage-trap anti-patterns; jobs must
     include social/emotional, not only functional.
   - Related-skills: `market-analysis-jtbd-fit` (JTBD job-statement
     construction is the closest existing skill; this skill applies
     that job framing specifically inside the VPC's Customer
     Profile/Value Map fit-check, not general JTBD alternative
     analysis), `pricing-verdict-report`.

4. **`business-model-design-platform-design`**
   - Axis: two-sided/multi-sided platform and marketplace design
     (distinct from single-sided revenue-model selection above).
   - Use when: deciding which side of a two-sided platform to
     subsidize, setting a marketplace take-rate, assessing
     multi-homing risk to platform defensibility, or sequencing a
     platform launch to solve the chicken-and-egg cold-start problem.
   - Rule seeds (from survey Angle 4): subsidize-the-side-with-greater-
     cross-side-externality rule (Rochet & Tirole); price-level vs.
     price-allocation independence; below-cost pricing as often
     optimal, not predatory; joint pricing/governance/design decision
     (Hagiu); multi-homing erodes defensibility; single-player-mode
     cold-start sequencing; take-rate-stability-as-network-effect-proxy
     check.
   - Related-skills: `business-model-design-revenue-model-selection`
     (marketplace/take-rate archetype selection happens there; this
     skill governs the two-sided pricing *structure* once that
     archetype is chosen), `pricing-tier-structure`.

### Cross-reference resolution

- `pricing-method-family`, `pricing-design-rigor`,
  `pricing-tier-structure`, `pricing-scope-gate`,
  `pricing-verdict-report`, `pricing-research` — all confirmed present
  under `skills/` (`ls skills | grep ^pricing-`, see `survey.md`).
- `finance-unit-economics-cac-payback`, `-evidence-chain`,
  `-ltv-cac-band`, `-ltv-churn-assumption`, `-proposal-shape`,
  `-sensitivity-scenario` — all confirmed present under `skills/`.
- `market-analysis-jtbd-fit` — confirmed present under `skills/`
  (mounted in this session's own skill list).

## Out of scope

- Authoring the actual `skills/business-model-design-*/SKILL.md`
  files, their full numbered `## Rules` sections, and running
  `scripts/check_skill_conformance.py` — phase-2 work, gated on
  approval per contract v3 s19.
- Verifying deanpeters/Product-Manager-Skills' exact license terms
  beyond the "Other/NOASSERTION, inspiration-only" framing issue #66
  itself already states and `docs/issue-56/proposals/
  skill-ecosystem-benchmark.md` already confirmed — no text from that
  pack is proposed for use here regardless.
- Any change to `pricing-*` or `finance-unit-economics-*` skills
  themselves beyond the new `Related-skills` links added *into* the
  new family's files in phase 2 (their own files are not touched).

## How you'll know it worked

- `docs/issue-66/reports/market-analysis/survey.md` exists, covers all
  four methodology angles named in the issue, and every external claim
  cites a live source URL.
- This proposal names exactly 4 skills with a distinct axis and "Use
  when" trigger each, MECE against each other and against
  `pricing-*`/`finance-unit-economics-*`.
- Each skill's rule seeds trace to a primary source captured in
  `survey.md`.
- `Related-skills` cross-references above name only skill directories
  confirmed to exist.
- PR against `main` from `issue-66/market-analysis` references `#66`
  (no `Closes`/`Fixes`/`Resolves` trailer — phase-1 proposal PR).
