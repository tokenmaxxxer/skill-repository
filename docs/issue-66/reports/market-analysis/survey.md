# Survey: business-model-design methodology (canvas / lean canvas / revenue-model / platform)

Subject: issue-66. Scout stage used parallel fan-out (4 concurrent
`Agent` calls, one per methodology angle: BMC+VPC, Lean Canvas,
revenue-model taxonomy, two-sided platform design), one round, no
further deepening needed (saturation reached: each angle returned
5-8 primary-sourced, decision-rule-shaped findings with live URLs,
enough to seed >=4 skills at this repo's citation bar).

## This repo's current write surface (from `skills/pricing-*` and
`skills/finance-unit-economics-*`)

- No `business-model-design-*` family exists yet (empty state
  confirmed: `ls skills | grep business-model` returns nothing).
- Adjacent families already cover pricing method selection
  (`pricing-method-family`, `pricing-design-rigor`,
  `pricing-tier-structure`, `pricing-scope-gate`,
  `pricing-verdict-report`, `pricing-research`) and unit-economics
  (`finance-unit-economics-cac-payback`, `-ltv-cac-band`,
  `-ltv-churn-assumption`, `-sensitivity-scenario`,
  `-evidence-chain`, `-proposal-shape`) — both assume a business
  model and revenue model are already chosen; neither covers how to
  construct a business-model canvas, select a revenue-model archetype
  in the first place, validate value-proposition fit, or design a
  two-sided/platform model. This is the gap issue #66 names.
- Fixed schema confirmed from `skills/pricing-design-rigor/SKILL.md`:
  frontmatter `name`, `description` ("Use when..." trigger),
  `axis`, `rule_count_floor`; body `## Trigger`, `## Procedure`,
  `## Output shape`, `## Rules` (numbered, each rule ending in a
  `source: <url>` citation line). `scripts/check_skill_conformance.py`
  enforces this mechanically (frontmatter + per-rule source when a
  `## Rules` section with `### N.` blocks exists — note:
  `pricing-design-rigor` uses a flat numbered list under `## Rules`
  rather than `### N.` sub-headings; this family will follow the same
  flat-numbered-list convention, matching the majority of surveyed
  skills).
- `docs/issue-56/proposals/skill-ecosystem-benchmark.md` (same role,
  prior issue) already benchmarked deanpeters/Product-Manager-Skills
  as license "Other/NOASSERTION" — confirms issue #66's own framing
  (deanpeters is inspiration-only, no text port) rather than requiring
  a fresh license check here.

## Angle 1 — Osterwalder/Strategyzer Business Model Canvas + Value
Proposition Canvas

- BMC's 9 blocks split into three functional groups — Desirability
  (Customer Segments, Value Propositions, Channels, Customer
  Relationships), Feasibility (Key Resources, Key Activities, Key
  Partnerships), Viability (Revenue Streams, Cost Structure) — filled
  customer-first, cost/revenue last (Cost Structure is a *derived*
  block, computed only after Key Resources/Activities/Partnerships are
  defined).
  Source: https://www.strategyzer.com/business-models-the-toolkit-to-design-a-disruptive-company
- VPC construction: fill the Customer Profile (jobs, pains, gains) for
  ONE segment at a time before designing the Value Map (products &
  services, pain relievers, gain creators) for that same segment —
  never the reverse, and never blend two segments (e.g. payer vs.
  user) into one profile.
  Source: https://www.strategyzer.com/library/5-common-mistakes-to-avoid-when-using-the-value-proposition-canvas
- "Fit" is an iterative, evidence-based state (Value Map adjusted
  against real customer evidence), not a one-time fill-and-done
  artifact; named failure modes include solution-first bias
  (cherry-picking jobs/pains your existing solution already covers)
  and the "comprehensive coverage trap" (addressing every job instead
  of prioritizing the top ones).
  Source: https://www.strategyzer.com/library/the-value-proposition-canvas ,
  https://www.strategyzer.com/library/5-common-mistakes-to-avoid-when-using-the-value-proposition-canvas
- Jobs must include social/emotional jobs, not only functional tasks —
  a named completeness failure mode when jobs are captured too
  narrowly.
  Source: https://www.strategyzer.com/library/5-common-mistakes-to-avoid-when-using-the-value-proposition-canvas

## Angle 2 — Lean Canvas (Ash Maurya / LeanStack)

- 9 blocks: Problem, Customer Segments, UVP, Solution, Channels,
  Revenue Streams, Cost Structure, Key Metrics, Unfair Advantage —
  swaps BMC's four "running-a-business" blocks (Key Partners, Key
  Activities, Key Resources, Customer Relationships) for four
  "starting-a-business" blocks (Problem, Solution, Key Metrics,
  Unfair Advantage), reframing the question from "how do I run this"
  to "is there a real business here."
  Source: https://s3.amazonaws.com/leanstack/v4/Lean-Canvas.pdf ,
  https://www.leanfoundry.com/articles/why-lean-canvas-versus-business-model-canvas
- Fill order runs riskiest-assumption-last: Problem+Customer Segments
  together first (the "outer pillars" — a problem only exists in the
  context of a specific customer), then UVP, then Solution, then
  Channels, then Revenue+Cost together, then Key Metrics, then Unfair
  Advantage last.
  Source: https://medium.com/lean-stack/what-is-the-right-fill-order-for-a-lean-canvas-f8071d0c6c8c
- Model selection rule: Lean Canvas for sketching a brand-new,
  pre-product-market-fit engine (startup); BMC for fine-tuning an
  engine already running (established business).
  Source: https://medium.com/lean-stack/why-lean-canvas-vs-business-model-canvas-af62c0f250f0
- Validate Problem+Customer via a Problem Interview before writing
  Solution — extract problems indirectly (get the full story of the
  interviewee's last relevant experience) rather than asking leading,
  jargon-laden questions ("avoid the word 'problem'").
  Source: https://blog.leanstack.com/the-updated-problem-interview-script-and-a-new-canvas-1e43ff267a5d
- Named top failure mode ("Innovator's Bias"): falling in love with
  the first solution before the problem is validated; treat the
  canvas as a living hypothesis document, not a static one-time plan.
  Source: https://medium.com/lean-stack/love-the-problem-not-your-solution-65cfbfb1916b

## Angle 3 — Revenue-model taxonomy / selection

- Core value-metric rule: choose a pricing metric that scales with
  customer value received (not cost to serve) — must correlate
  strongly with value, share in customer success, allow starting
  small and scaling, and grow monotonically for the average customer.
  Source: https://openviewpartners.com/usage-based-pricing/
- Human-vs-machine end-user rule: usage-based/metered pricing fits
  products whose end user is other software (usage tracks cleanly to
  a metric); subscription fits products with human end users (humans
  dislike monitoring usage/spend).
  Source: https://a16z.com/usage-based-pricing-rule-of-thumb/
- AI-product rule: shift the pricing metric from seats/users to
  output (work performed) as AI automates the underlying task,
  because a seat-based metric stops tracking value once the human is
  no longer the unit of work.
  Source: https://a16z.com/podcast/ai-is-upending-saas-pricing/
- Usage-based pricing is the standard choice when consumption
  naturally grows with customer success (metered, expands net dollar
  retention automatically); Bessemer's benchmark bands NRR as 100%
  good / 110% better / 120%+ best.
  Source: https://www.bvp.com/atlas/state-of-the-cloud-2023
- Freemium fits low-marginal-cost, high-virality products, trading
  revenue predictability for reach (small paying subset + free-user
  network value); marketplace/take-rate fits businesses whose value-add
  is matching two transacting sides, not producing the good/service
  itself — priced as a % of transaction value, not a flat fee.
  Source: https://www.strategyzer.com/library/business-model-generation-book-summary
- Stage-sequencing rule: early-stage pricing should optimize for
  adoption/customer count over per-customer extraction; raise price
  only once value delivery is proven.
  Source: https://www.forentrepreneurs.com/saas-metrics-2/
- Market-maturity signal: usage-based pricing is now mainstream
  (39%+ adoption in recent SaaS surveys), displacing pure seat pricing
  as products become infrastructure-like — usable as a benchmark
  signal for whether usage-based is a viable default in a category.
  Source: https://openviewpartners.com/blog/2023-pricing-data/

## Angle 4 — Two-sided / multi-sided platform design

- Foundational pricing-structure rule: subsidize the side generating
  the greater cross-side network externality; recover margin on the
  side with lower price elasticity — total price level and price
  *allocation* between sides are independent levers (a platform can
  hold total price fixed and still change volume/profit by shifting
  the split).
  Source: https://www.tse-fr.eu/sites/default/files/medias/doc/wp/2002/platform.pdf
  (Rochet & Tirole, "Platform Competition in Two-Sided Markets"),
  https://web.mit.edu/14.271/www/rochet_tirole.pdf
- Below-cost/zero pricing on one side is often optimal (not
  predatory) when that side's participation is what attracts the
  profitable side (e.g. cardholders subsidized, merchants pay).
  Source: https://www.tse-fr.eu/sites/default/files/medias/doc/wp/2002/platform.pdf
- Platform strategy must jointly decide pricing, governance, and
  design across sides — treating "which side to subsidize" as an
  isolated pricing question misses the bundle.
  Source: https://www.hbs.edu/faculty/Pages/item.aspx?num=44940 ,
  https://sloanreview.mit.edu/article/strategic-decisions-for-multisided-platforms/
  (Hagiu)
- Multi-homing rule: increased multi-homing on one side (e.g. sellers
  dual-listing across marketplaces) shifts pricing/steering power
  toward the other side and erodes platform defensibility.
  Source: https://www.nfx.com/post/network-effects-manual
- Cold-start rule: launch sequencing should start from whether the
  product has a viable "single-player mode" delivering standalone
  value before the network exists, to solve chicken-and-egg.
  Source: https://www.nfx.com/post/network-effects-manual (single-player-mode
  framing traced to a16z network-effects content)
- Defensibility-ceiling check: evaluate network-effect strength via
  the demand-value curve against supply growth, and whether it
  saturates (asymptotic marketplace) before assuming compounding
  network effects; track take-rate stability alongside trips-per-user
  and utilization as a bundle, not take-rate alone.
  Source: https://www.nfx.com/post/network-effects-manual

## Gap line

Field must-bes this repo already meets structurally: axis-scoped
condition-matched triggers, fixed Trigger/Procedure/Output-shape/Rules
body schema, per-rule `source:` citation discipline (matches or
exceeds every methodology surveyed — none of BMC/VPC, Lean Canvas,
revenue-model, or platform-design literature ships a machine-checkable
per-rule citation format of its own; that is this repo's own
convention, applied here).

Field must-bes this repo is missing (the actual gap issue #66 names):
no skill addresses canvas construction (BMC/VPC sequencing and
desirability-before-viability ordering), no skill addresses revenue-
model archetype selection (value-metric alignment, human-vs-machine
end-user split, stage-sequencing), no skill addresses value-proposition
fit validation (Customer Profile before Value Map, fit as iterative
evidence, named failure modes), and no skill addresses platform/
two-sided-market design (subsidize-side selection, multi-homing risk,
cold-start sequencing). All four gaps are covered by primary sources
found above at this repo's citation bar (Strategyzer, LeanStack/Ash
Maurya, a16z/OpenView/Bessemer/Strategyzer/David Skok, Rochet-Tirole/
Hagiu/NfX respectively) — proposal below routes each gap to one
proposed skill.
