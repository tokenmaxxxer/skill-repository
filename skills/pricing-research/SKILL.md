---
name: pricing-research
description: >-
  Use whenever someone needs to set, test, or audit a price or price range for a
  defined product — choosing and running a willingness-to-pay method honestly,
  routing between the Van Westendorp Price Sensitivity Meter (PSM) family and
  the conjoint/discrete-choice (CBC) family by what the pricing decision
  actually needs to know, and reporting numbers with the labels their evidence
  base supports. Trigger on requests like "가격 얼마로 정해야 할까", "지불의사 조사해줘", "how
  much should we charge", "design a conjoint study", "price sensitivity meter".
  Also trigger when a team is about to hand off pricing numbers as if they
  answer a question the method never collected data for. Do NOT use for
  competitor pricing (route to market-recon), for pricing with no enumerable
  product yet, or for the single upstream question of whether to field anything
  at all (use pricing-scope-gate).
---

# Pricing Research (Willingness to Pay)

## Trigger

Use whenever someone needs to set, test, or audit a price or price range
for a defined product, or is about to pick a pricing method, design one,
or hand off pricing numbers as if they answer a question the method
didn't collect data for. Do NOT use for competitor pricing (route to
`market-recon`), for pricing decisions with no enumerable product yet
(too early), or for general market-sizing questions with no price
variable at their center.

## Procedure

### Step 1 — Scope gate

Confirm: is the question about willingness to pay / price setting, and is there a defined product
or feature bundle whose attributes (or, for PSM, whose single concept) can be enumerated?

**Gate — three exit branches, each recorded in writing**:
- If the question is really "what does the market charge," exit and route to `market-recon`.
- If nothing about the offer is fixed enough to enumerate, exit — it's too early.
- If an adequate number already exists — a prior study on the **same** offer, covering the **same**
  price range, whose method passes Steps 2-5 — exit and name that study and why it qualifies. A
  cost-plus figure or an existing price tier does not qualify; those are internal constraints, not
  WTP evidence.

Only continue once all three checks pass without exiting.

### Step 2 — Method routing by what the answer must support

This is the skill's core decision, and it is decided by arithmetic, not taste.

- **Does the decision require a revenue/profit/volume number** (e.g. "what price maximizes
  revenue," "what's the demand curve")? → PSM **cannot** answer it: it collects no quantity, no
  purchase intent, no cost. Route to a choice-based method (CBC lineage) or an explicit volume
  study — **but apply the same arithmetic to that method too** (see the gate below); switching
  methods does not conjure inputs.
- **Does the decision need only an acceptable-price range / sanity band** as one input among
  several? → PSM's four questions and crossings are a fixed, cheap procedure — usable, provided its
  outputs are labeled as perception thresholds, never as an economic optimum.

**The arithmetic applies to every method, including the one you route to.** CBC collects *choice*:
it yields preference **shares**, not units and not cost. So a revenue number additionally requires a
market-size figure, and a profit number additionally requires cost data from company accounting.
Neither comes out of the study.

**Gate**: name explicitly which of quantity / purchase intent / cost the decision needs, and
confirm the chosen method actually collects it — a method that doesn't collect an input cannot
produce an output that depends on it. This gate is not PSM-specific: if the answer needs revenue or
profit and the chosen method is CBC, the external sources for market size and cost must be named
explicitly, or the gate fails for CBC exactly as it does for PSM. If a PSM-only study is chosen and
any revenue/profit/volume number gets requested downstream, that request fails this gate and must be
redirected to a choice-based method plus its named external inputs.

### Step 3 — Name the family (conjoint-family methods only)

If a conjoint-family method is chosen, state explicitly which family — CBC/discrete-choice, or
rating-based conjoint — and do not import the other's evidence.

**Gate**: the family is named in writing, with the taxonomy dispute noted (Louviere, Flynn &
Carson 2010 reject the "CBC is a kind of conjoint" framing). A report that says only "we're doing
conjoint" without naming the family fails this gate.

### Step 4 — Design gates (CVA-style rating designs, labeled as such)

Enumerate attributes and levels with counts; compute parameters = total levels − number of
attributes + 1; state the task count and its ratio to parameters.

**Gate — scoped, and the scope is load-bearing**:
- **For CVA-style rating designs**: ratio ≥ 1× is mandatory (below 1× the design is blocked — the
  software itself refuses); ratio < 1.5× is a recorded warning; 3× is named as an unenforced ideal,
  not a requirement. Total questions > ~30 triggers a data-quality warning.
- **For CBC**: record the ratio as a **reference figure only**, and state that no CBC-general gate
  was established by this research. Never report a CBC design as "blocked" or "warned" on the basis
  of CVA's bands — CVA is a legacy minority method (~2% of projects, ≤6 attributes) and its
  software thresholds carry no authority over CBC.

In both cases: attributes must vary independently; if a perfectly balanced orthogonal design isn't
achievable, say so in writing and state that efficiency — not orthogonality per se — is the property
being traded (Kuhfeld).

### Step 5 — Incentive alignment decision

Decide **before** fielding whether responses are incentive-aligned (consequential) or hypothetical,
and record the choice with its cost (~$7.81/participant, ≈$2,343 at n=300).

**Gate**: if the meta-analytic benefit is cited to justify the cost, all three qualifications from
the evidence-grade section must be cited alongside it — the 12% is chance-corrected and relative
(raw hit rates run the opposite direction: 48.26% vs. 50.25%), publication bias was detected and
corrected for, and the authors qualify the hit-rate metric itself. A report citing "12% better"
alone, without the qualifications, fails this gate.

### Step 6 — Report

Compile these six numbered elements:
1. The method chosen.
2. Its family (for conjoint-family methods: CBC vs. rating-based).
3. What it collects.
4. What it therefore cannot answer — and, if the answer needs revenue or profit, the named external
   sources supplying market size and cost.
5. The numbers, each with its correct label.
6. The residual list.

**Gate**: each of the six numbered elements is present, and each names the actual method/number/
source rather than a category. Every PSM number carries the label "price-perception threshold, not a
revenue optimum"; OPP is never reported as "the optimal price." The residual list names at least the
questions the chosen method structurally cannot answer (for PSM: any revenue/volume/profit question;
for CBC: unit volume and profit without external market-size and cost inputs).

## Output shape

Applying this skill produces a six-element report per pricing study: the
scope-gate result, the input the decision needed and the method chosen
for it, the conjoint family named where relevant, the design parameters
and their gate band, the incentive-alignment decision and its cost, and
the final numbers with correctly scoped labels plus the residual list of
what the method cannot answer. See `## Report format` below for the full
per-step layout and the high-stakes/directional weighting rule.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- S1 — First: does this even need the procedure? → references/rules.md
- S2 — Evidence grade — read before citing this to anyone → references/rules.md
- S3 — Report format → references/rules.md
- S4 — Related skills → references/rules.md
