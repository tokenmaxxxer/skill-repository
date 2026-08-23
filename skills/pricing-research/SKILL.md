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

## First: does this even need the procedure?

Run this gate before touching any method — the whole point of this skill is matching the method
to what the pricing decision needs, and skipping straight to a favorite technique (usually
conjoint, because it sounds rigorous, or PSM, because it's cheap) is exactly the failure mode this
skill exists to block.

- **Is the question actually about willingness to pay / price setting** — as opposed to "what do
  competitors charge for something similar"? The latter is competitor/market research. Route it to
  `market-recon` instead; this skill does not re-derive competitor pricing.
- **Is there a defined product or feature bundle whose attributes can be enumerated?** If nothing
  about the offer is fixed enough to list attributes and levels (or, for PSM, to describe the
  single concept respondents will price), it is too early for pricing research. Say so and stop —
  route back to product definition first.
- **Does the decision actually need primary research at all?** An existing number is adequate — and
  new fieldwork is not warranted — only if there is a prior study **on the same offer, covering the
  same price range, whose method passes Steps 2-5 of this skill**. Cost-plus figures and existing
  tiers are not WTP evidence and do not clear this check; they are internal constraints. If an
  adequate prior study exists, exit and say which study and why it qualifies.

Everything below applies only once a genuine WTP/pricing question is on the table, the offer is
enumerable, and no adequate number already exists.

## Evidence grade — read before citing this to anyone

This skill's spine is an asymmetry between two method families. State it precisely; do not
overstate it.

**The asymmetry, stated correctly**: conjoint's advantage is NOT "conjoint is validated and PSM is
not." It is that conjoint has a predictive-validity literature including a 2025 meta-analysis,
plus machine-checkable design gates (in CVA's case), while PSM has a fixed, cheap procedure whose
*interpretation layer* is not defended on theory even in the documentation of a vendor that sells
PSM tooling. For PSM, the honest
statement is: no validity study was found in this research, and the criticisms circulating in
vendor blogs failed independent verification — that is a coverage gap plus weak sourcing, not a
demonstrated absence of validity. None of what follows is RCT evidence that using either method
improves actual pricing outcomes.

**Conjoint lineage — CONFIRMED, three-part (NOT single-origin)**:
- Luce & Tukey (1964, *Journal of Mathematical Psychology* 1(1):1-27) — axiomatic conjoint
  measurement; the theory.
- Green & Rao (1971, *JMR* 8(3):355-363) — the marketing operationalization. Their own abstract
  calls conjoint measurement "a new development in mathematical psychology" and limits their
  contribution to applying "these techniques to illustrative problems in marketing." Their real
  contributions: the two-factor trade-off matrix collection method and non-metric part-worth
  estimation (MONANOVA). "Full-profile" is a later label (formalized in Green & Srinivasan 1978);
  Johnson (1974) is named as a parallel introducer. **REFUTED**: attributing conjoint's origin
  solely to Green & Rao 1971 — do not write that.
- Louviere & Woodworth (1983, *JMR* 20(4):350-367) — integration with discrete choice theory; the
  starting point of choice-based conjoint (CBC). Their own 1983 remark about limited external
  validity evidence is a self-assessment of that origin paper — cite it only as such, never as a
  grade of today's CBC.

**Taxonomy dispute — CONFIRMED, must be named whenever a conjoint-family method is chosen**:
Louviere, Flynn & Carson (2010, *Journal of Choice Modelling* 3(3):57-72, "Discrete Choice
Experiments Are Not Conjoint Analysis") argue that treating discrete choice experiments as a
special case of conjoint analysis is "a mistake" and that the CBC name is "potentially very
misleading" — the theoretical bases differ (random utility theory vs. conjoint measurement
theory); health economics journals dropped the conjoint label in the late 1990s. **Consequence for
this skill**: never grade CBC and rating-based conjoint on one shared "conjoint" evidence scale —
name which one is meant, every time.

**Conjoint predictive-validity evidence — CONFIRMED, with three mandatory qualifications (the most
misquotable finding here)**:
- *Marketing Letters* (2025) 36:533-546 meta-analysis: 134 effect sizes from 34 papers (working
  papers deliberately included as a publication-bias defense — never call it "34 published
  articles"), N=12,980 respondents (4,165 incentive-aligned / 8,815 hypothetical), scope limited to
  work from 2000 onward.
- Result: incentive alignment significantly increases predictive validity (β = 0.11, SE = 0.02,
  p < .001), reported by the authors as a ~12% **relative** increase in hit rate.
- **Qualification 1** (state whenever the 12% is cited): raw hit rates run the other way —
  incentive-aligned 48.26% vs. hypothetical 50.25%. The advantage appears only after controlling
  for chance level (14.60% vs. 22.76%); as improvement-over-chance it is 33.66% vs. 27.49% = 6.16
  percentage points. Citing "12% better" as an observable gap is a misreading.
- **Qualification 2**: the authors detected publication bias themselves (funnel-plot asymmetry
  test) and controlled for it with standard error as a moderator — the estimate is
  bias-corrected, not raw.
- **Qualification 3**: the authors qualify their own metric — hit rate is "sometimes criticized as
  an assessment of predictive validity."
- Cost datum: incentive alignment adds about $7.81 per participant (≈$2,343 at n=300).
- **REFUTED**: "individual-level estimation has significantly higher predictive validity than
  aggregate" — do not write that.

**Design gates — CONFIRMED, with a scoping caveat that must be honored**:
- Sawtooth's CVA software recommends 3× as many choice tasks as parameters (parameters = total
  levels − number of attributes + 1), but the manual itself says this ideal "often is not used in
  practice" and "some experienced conjoint analysts are willing to ask as few as 1.5x." The
  software's actual enforced gates are a **warning below 1.5×** and a **hard block below 1×** — 3×
  is an unenforced ideal, not a gate.
- Practical ceiling: "asking more than about 30 conjoint questions may result in poor quality
  data."
- Orthogonality: "Attributes must vary independently of each other to allow efficient estimation
  of utilities," while the same manual concedes "it might not be possible to create a perfectly
  balanced, orthogonal design"; Kuhfeld argues orthogonality is a pre-computational-era requirement
  and "a design does not have to be orthogonal to be efficient" — efficiency and unbiasedness are
  different properties. **REFUTED**: defining orthogonal design as the two-property combination of
  balance + orthogonality — do not write that.
- **SCOPING CAVEAT (must appear whenever these gates are cited)**: CVA is a legacy minority method
  (~2% of projects, ≤6 attributes) — its manual cannot stand as the standardization basis for
  conjoint in general. Present these as CVA's software gates specifically, and state that the
  general-case (CBC) gate argument would have to rest on CBC documentation, which this research did
  not establish. **REFUTED**: "full-profile is recommended only for ≤6 attributes and typical
  commercial practice violates design requirements" — do not write that.

**Van Westendorp PSM — CONFIRMED**:
- Origin: Peter H. van Westendorp, "NSS Price Sensitivity Meter (PSM)," 29th ESOMAR Congress,
  Venice, September 5-9 1976, pp.139-167. Do not call him an economist — unverified in independent
  primary sources.
- Operationalization (the whole of it): four price questions (too expensive / too cheap / getting
  expensive / bargain) → cumulative curves → four crossing points (PMC, PME, IPP, OPP).
- **The arithmetic fact that drives this skill's hardest gate**: basic PSM does not merely fail to
  optimize revenue or profit — it does not collect the inputs. No quantity, no purchase intent, no
  cost data, so revenue (price × quantity) is arithmetically incomputable from PSM data alone.
  OPP's "optimal" means minimal extreme-rejection, **not** an economic optimum.
- Crossing-point criticism, verified only in this narrow form: Sawtooth — a vendor that sells PSM
  tooling — states in its own documentation that the "line-crossing approach has largely been
  criticized and discredited as lacking good theory" (medium grade). It is one vendor's
  documentation, not an admission by PSM's proprietor; do not upgrade it.
- **REFUTED THIS ROUND — must NOT appear**: "PSM has no theoretical foundation," "no published
  explanation of its theory exists," "PSM has no track record of predictive validity," "PSM
  produces guidance that resists empirical validation," "PSM assumes linear price perception and
  ignores brand/quality/market trends." All of these failed verification; they were vendor-blog
  assertions. The correct statement is: no PSM validity study was **found** in this research, and
  even the vendor does not defend the crossing-point interpretation layer — but absence of found
  evidence is not proof of absence. Never write "PSM has no validity evidence."

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

## Report format

Report, per pricing study:

- Step 1: scope gate result (proceed / routed to `market-recon` / exited as too early / exited —
  adequate number already exists, with the qualifying study named).
- Step 2: which input the decision needs (quantity / purchase intent / cost / none of these), and
  the method chosen because it collects that input.
- Step 3 (conjoint-family only): the named family (CBC vs. rating-based conjoint) and the taxonomy
  dispute noted.
- Step 4: attributes and levels, computed parameters, task count, and the ratio. For CVA-style
  designs, which gate band it falls in (blocked / warned / ideal-not-met / clear). For CBC, the
  ratio as a reference figure only, with the statement that no CBC-general gate was established —
  never a band verdict.
- Step 5: the incentive-alignment decision, its cost, and — if the meta-analytic benefit is
  cited — all three qualifications alongside it.
- Step 6: the numbers with their labels (PSM crossings labeled as perception thresholds; conjoint
  utilities/shares labeled per the model that produced them) and the residual list of what the
  method cannot answer.
- The evidence-grade asymmetry restated briefly: conjoint has a predictive-validity literature
  (2025 meta-analysis) plus machine-checkable design gates (CVA-specific); PSM has a fixed, cheap
  procedure whose interpretation layer even its vendor won't defend on theory, and no validity
  study was found (a coverage gap, not a demonstrated absence). Neither is RCT evidence that the
  method improves actual pricing outcomes.

Match the report's weight to the decision's weight:

- **High-stakes** (revenue-critical launch, multi-year contract, method-family debate materially changes the number): full per-step report format below.
- **Directional / early-stage**: the six numbered elements from Step 6's gate plus the evidence-grade asymmetry note are sufficient — the per-step walkthrough is not required.

In all cases the number must be traceable to a named method and family, a stated set of inputs it actually collected, and gates that were checked before the number was trusted. State explicitly which format you used and why, so the reader knows whether a compressed report reflects low stakes or omitted procedure.

## Related skills

- [pricing-method-family](../pricing-method-family/SKILL.md) — route back to method-family first if the family choice (PSM vs. conjoint) itself is still open.
