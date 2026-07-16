---
name: test-derivation
description: >-
  Derives test cases from written requirements/acceptance criteria using standardized black-box
  techniques (Given-When-Then scenarios, equivalence partitioning, boundary value analysis,
  decision tables, state transition testing, pairwise/t-way combinatorial testing, and MC/DC
  branch coverage), routes each requirement to the right technique by its problem shape, and
  maintains the requirements↔tests traceability matrix. Use this whenever the user wants test
  cases pulled out of acceptance criteria or requirements, wants help deciding which testing
  technique fits a requirement, or wants requirements and tests linked — e.g. "이 수용 기준으로 테스트
  케이스 뽑아줘", "테스트 케이스 도출해줘", "경계값 테스트 만들어줘", "어떤 테스트 기법 써야 해", "조합 테스트 만들어줘", "상태 전이
  테스트 설계해줘", "요구사항이랑 테스트 매핑해줘", "추적성 매트릭스 만들어줘", "derive test cases from these acceptance
  criteria", "generate boundary value tests", "which test technique should I use", "design a
  decision table", "build a requirements-to-tests traceability matrix", "what equivalence classes
  am I missing". The value is coverage discipline and technique-fit routing, not a claim that any
  one of these techniques finds more bugs than another. Do NOT use it when there are no written
  requirements to derive from yet (that's requirements-quality — get them written first), when a
  full test suite and traceability matrix already exist and just need executing or reporting on,
  or for non-functional testing (performance, security, usability) that these black-box techniques
  don't cover.
---

# Test Derivation

## First: does this even need the procedure?

Check these before running the full derivation, because forcing it onto the wrong input wastes the user's time:

- **Are there written requirements or acceptance criteria at all?** If the user only has a vague feature idea or a one-line ticket title with no stated acceptance criteria, this isn't a test-derivation problem yet — it's a requirements-quality problem. Say so and point to a requirements-quality pass first. Garbage in, garbage tests out: deriving from unwritten requirements just means silently inventing the requirements too.
- **Does the user already have tests and a matrix, and just want them run or summarized?** If so, just do that task — don't re-derive from scratch.
- **Is this actually a non-functional ask** (performance, security, accessibility, usability)? Equivalence partitioning and boundary value analysis are black-box *functional* techniques. Say plainly that this skill doesn't cover the non-functional dimension and point to the relevant skill instead (e.g. `usability-eval` for usability).
- **Is the user asking for a subjective quality opinion on existing tests** ("are these good tests?") rather than derivation? That's a review task, not a derivation task — this skill's gates only apply going forward from requirements to new/updated cases.

Everything below applies when there is at least one written requirement or acceptance criterion to derive from.

## Evidence grade — read before citing this to anyone

- Equivalence partitioning (EP) and boundary value analysis (BVA) are standardized, current learning objectives in the **ISTQB Certified Tester Foundation Level (CTFL) syllabus v4.0/4.0.1** — FL-4.2.1 (EP) and FL-4.2.2 (BVA), both at cognition level K3 ("apply": candidates must be able to derive test cases, not just recognize the technique). This is real, current standardization — cite it as such.
- BVA is defined specifically as exercising the boundaries of **ordered** equivalence partitions. It does not apply to unordered partitions (e.g., an enum of unordered categories) — those get EP coverage only, marked N/A for BVA.
- The syllabus gives explicit numeric coverage formulas: `EP coverage % = (partitions exercised by ≥1 test case ÷ total identified partitions) × 100%`, and the analogous formula for BVA, with **2-value** (boundary + one neighbor) and **3-value** (boundary + both neighbors) variants.
  - Honesty requirement: the denominator is "identified" partitions/boundaries. Identifying them is a judgment call the syllabus does not mechanize — two competent testers can produce different partition lists from the same requirement. The gates in this skill are objective *after* identification. That's why Step 4 forces the identification list to be written down and reviewable *before* any coverage percentage is computed — the coverage number is only as honest as the list underneath it.
  - Attribution: ISTQB's own BVA white paper attributes 2-value BVA to Craig (2002) and Myers (2011, 3rd edition of *The Art of Software Testing*), and 3-value BVA to Koomen (2006) / O'Regan (2019). Do not state "Myers 1979" or any other unverified origin claim.
- **Detection-effectiveness evidence is weak — state this plainly, don't oversell.** The only controlled experiment in our evidence base (Roper, Wood & Miller 1997, 47 students, small C programs) found code reading, functional testing (EP/BVA), and structural testing "broadly similar" in effectiveness, with the relative ranking depending on program and fault characteristics. The one effect that *was* robust: **combining techniques was substantially more effective than any single technique alone.** Juristo, Moreno & Vegas (2004), a 25-year review of testing-technique experiments, concluded the field's knowledge base has low maturity overall.
  - This skill's honest value claim is therefore: **(a)** combining techniques beats any single one (the one robust finding), **(b)** coverage accounting surfaces input space nobody examined, **(c)** traceability produces a documented, measured speed/correctness effect (below) — **not** "EP/BVA finds more bugs than other techniques," which is not established.
- Given-When-Then (GWT): origin is Dan North, with Chris Matts, late 2004 (primary source: North's "Introducing BDD"). A story's behavior *is* its acceptance criteria expressed as automated scenarios — that's the design intent, not an added layer on top. As of a 2018 review, no controlled experiments directly evaluating BDD's benefits existed; state this claim with that time bound rather than as settled fact. The GWT gate used here is purely syntactic (three-part structure present) — it is not a claim that GWT scenarios are more effective than other scenario formats.
- Traceability: across a 63-paper systematic mapping, change impact analysis is the dominant documented use (38 of 45 change-management studies). The one quantified controlled effect: **Mäder & Egyed, Empirical Software Engineering (2015)**, 71 industrial practitioners, within-subject design — maintenance tasks completed **24% faster and ~50% more correct** with traceability in place. Label this as a single experiment's result, not a universal law. 57% of the field's evidence base is toy-example level — treat the 24%/50% figures as the strongest single data point, not the average outcome. A safety-critical-domain interview study found engineers spend roughly 50-100 hours/year on manual change-impact analysis — that's the tedium this skill's matrix is meant to remove.
- **Not verified, do not state as fact:** claims that DO-178C or ISO 26262 mandate clause-level traceability are commonly asserted, but our verification round did not confirm the actual clause text. If a safety-critical mandate comes up, say "commonly cited, unverified in our research" — never state it as a confirmed regulatory requirement.
- Decision table testing is specification-based per **ISO/IEC/IEEE 29119-4:2021 §5.2** and a K3 learning objective in **ISTQB CTFL v4.0.1 §4.2.3**. Its historical origin and any comparative-effectiveness studies were **not** confirmed in our research — treat its authority as standards-grade, not experimental.
- State transition testing is specified in **29119-4 §5.2** and **CTFL v4.0.1 §4.2.4**, with N-switch coverage material in **CTAL-TA v4.0**. The coverage hierarchy (all-states < 0-switch < all-transitions) and the all-transitions-for-critical-software rule are drawn directly from the syllabus. N-switch itself traces to **Chow (1978, IEEE TSE)**; Chow's fault-detection guarantee holds only under stated assumptions (completely specified, minimal FSM, fixed initial state, reachable states) — carry those assumptions along whenever the guarantee is mentioned.
- Pairwise/t-way testing's routing rationale rests on retrospective interaction-fault studies, principally **Kuhn, Wallace & Gallo, IEEE TSE 30(6) 2004**, plus NIST companion studies (NASA GSFC 93.3% cumulative at 2-way/100% at 4-way over 329 error reports; FDA medical-device recalls 97% at 1-2 variables over 109 analyzable recalls; Mozilla/Apache >70% at 1-2 way; max observed interaction size 6 factors). This is observational defect data, not a controlled experiment, and 2-way detection ranged roughly 53-97% across the studied systems — pairwise is a floor, not a guarantee. The criticism literature against pairwise was not covered in our verification; the recommendation below reflects the pro-side evidence plus the syllabus's own hedges, not a balanced literature review.
- MC/DC is cited here for its **definition only** (29119-4 §5.3.6, verified verbatim: each single Boolean condition in a decision must be shown able to independently affect the decision's outcome). The commonly asserted DO-178C Level-A mandate and cost/effectiveness critiques were **not** confirmed — if the user is in an actual avionics/regulated context, tell them to verify the applicable standard's clause directly rather than rely on this skill for the regulatory claim.
- **Three-layered evidence, none of it RCT-grade:** (1) industry standards, primary-source verified (ISO/IEC/IEEE 29119-4:2021, ISTQB CTFL v4.0.1 / CTAL-TA v4.0); (2) a formal proof valid only under stated assumptions (Chow 1978); (3) retrospective defect-data analysis (NIST/Kuhn et al.). None of these three layers is a randomized controlled trial of technique effectiveness — say so whenever citing this router's authority.
- **Exploratory testing / session-based test management is out of this router's scope** — not because it's known to be ineffective, but because nothing about it survived verification this round. If a requirement has no written spec at all, that's a Step 1 scope-gate failure, not a signal to improvise an exploratory-testing procedure here.

## Procedure

### Step 1 — Scope gate

Confirm there are written requirements or acceptance criteria to derive from — list them or ask the user to paste/link them.

**Gate:** at least one written requirement/acceptance criterion is in hand. If none exists, stop here and route to a requirements-quality pass first — do not invent requirements to keep going.

### Step 2 — Given-When-Then scenario per acceptance criterion

For each acceptance criterion, write at least one Given-When-Then scenario expressing it as a concrete, automatable case.

**Gate (syntactic, objective):**
- Every scenario has all three parts (Given, When, Then) present and non-empty.
- Every acceptance criterion has ≥1 scenario mapped to it — do the count comparison explicitly: `criteria count` vs. `scenarios count / criteria covered`, and name any criterion with zero scenarios.

### Step 3 — Route each requirement by problem shape

Before deriving cases, classify **every** requirement/acceptance criterion with a binary checklist, in this order, and record the primary route it lands on:

1. Does it constrain values/ranges of individual inputs? → **EP/BVA** (Steps 4-6, below).
2. Do ≥2 conditions combine to select among different outcomes (business rules: pricing, permissions, eligibility)? → **decision table testing** (Step 7).
3. Does it describe states/modes with events causing transitions (lifecycle, session, payment flow)? → **state transition testing** (Step 8).
4. Do ≥3 independent parameters/flags/environments multiply into a combination space? → **pairwise/t-way testing** (Step 9).
5. Is it safety-critical Boolean logic inside a decision? → **MC/DC branch** (Step 10 — lower evidentiary grade, definitional use only).
6. No written spec to derive from at all? → out of this skill's verified scope; this should already have failed the Step 1 scope gate — do not improvise an exploratory-testing procedure here.

A requirement can answer "yes" to more than one question (e.g., a pricing rule with ordered numeric thresholds needs both EP/BVA on the thresholds and a decision table for the rule combination) — in that case route it to every technique that applies, not just the first match.

**Gate:** every requirement has exactly one classification pass recorded (each of the six questions answered yes/no for that requirement) and at least one primary route assigned. No requirement is silently left unrouted.

### Step 4 — Identify input domains and enumerate partitions (EP/BVA route)

For each input or condition referenced across the scenarios that routed to EP/BVA, write out the equivalence partition list explicitly: valid classes and invalid classes, each named.

**Gate (objective, but externalizes the judgment call):**
- A written partition list exists per input, with a stated total count (e.g., "status field: 3 valid partitions, 2 invalid partitions").
- This list must exist and be reviewable *before* Step 6's coverage number is computed — do not compute coverage against an implicit or unwritten partition list.

### Step 5 — Boundary enumeration for ordered partitions only (EP/BVA route)

For each partition identified in Step 4 that is **ordered** (numeric ranges, dates, sequences, anything with a "less than / greater than" relationship), name the chosen variant — 2-value or 3-value — and enumerate the boundary items per that variant's definition.

**Gate (objective):**
- Every ordered partition has boundary items listed matching the named variant (2-value: boundary + one neighbor; 3-value: boundary + both neighbors).
- Every unordered partition is explicitly marked **N/A for BVA** (not silently skipped) — BVA only applies to ordered partitions.

### Step 6 — EP/BVA coverage computation

Apply the ISTQB formulas from the evidence-grade section:
- `EP coverage % = (partitions exercised by ≥1 test case ÷ total identified partitions) × 100%`
- `BVA coverage % = (boundary items exercised by ≥1 test case ÷ total identified boundary items) × 100%`

**Gate (numeric, objective):** state both percentages. For anything short of 100%, name the specific uncovered partition/boundary item and either add a test case for it or record an explicit, named exclusion reason (not a silent gap).

### Step 7 — Decision table testing (routed requirements only)

For each requirement routed to decision tables, enumerate the conditions and list every **feasible** combination of their values as a column; mark the expected outcome/action per column. List infeasible combinations separately with a written reason each (business rule makes them impossible, mutually exclusive conditions, etc.) — do not fold them into the feasible-column count.

**Gate:** numeric coverage stated as `exercised feasible columns ÷ total feasible columns × 100%`; every excluded (infeasible) column has a written reason; at least one test case exists per feasible column to reach 100%. Note honestly: the technique's historical origin and any comparative-effectiveness studies are standards-grade authority, not experimentally confirmed.

### Step 8 — State transition testing (routed requirements only)

For each requirement routed to state transitions, write the state model in full: enumerate states and transitions (with counts), including the triggering event and, where applicable, the invalid transitions attempted from each state. Name the chosen coverage level as one of the ordered hierarchy — all-states, valid-transitions (0-switch), all-transitions (which adds attempting invalid transitions), or N-switch (N≥1) — and, if N-switch is chosen, state N and why (the syllabus reserves 2-switch+ for cases where unexpected event sequences carry high failure risk; it grows exponentially with N).

**Gate:** the state model exists in writing (states + transitions enumerated with counts); the chosen coverage level is named; coverage % is computed against the enumerated transition list; for mission-/safety-critical requirements the level is all-transitions (which also requires attempting invalid transitions) or there is a written justification for accepting less. If Chow's W-method fault-detection guarantee is invoked, its assumptions (completely specified, minimal FSM, fixed initial state, reachable states) are stated alongside it.

### Step 9 — Pairwise / t-way testing (routed requirements only)

For each requirement routed here, write the parameter/value model down explicitly: parameters and their possible values, each enumerated with counts. State the chosen interaction strength `t` (2-way pairwise, 3-way, ... up to all-combinations) with a risk rationale — higher risk calls for higher `t`, always weighing coverage strength against test-generation/execution effort.

**Gate:** the parameter/value model is written down; `t` is stated with a risk rationale; t-way coverage is computed mechanically from the model (it is not a judgment call once the model and `t` are fixed). Carry the domain-variance honesty note: observed 2-way detection rates varied roughly 53-97% across studied systems, so a pairwise suite is a floor on defect detection, not a guarantee of it.

### Step 10 — MC/DC branch (routed requirements only, definitional use only)

For each decision routed here, enumerate its individual Boolean conditions, then construct a test pair per condition that demonstrates it can independently affect the decision's outcome (holding the other conditions fixed).

**Gate (syntactic):** the condition list is enumerated per decision, and each condition has a demonstrating test pair. Do not assert a DO-178C Level-A mandate or any cost/effectiveness claim from this skill — if the user is in an actual avionics/regulated context, tell them to verify the applicable standard's clause directly.

### Step 11 — Traceability matrix

Build a requirements × test-cases matrix: rows are requirements/acceptance criteria, columns are test cases (the GWT scenarios plus any cases derived from Steps 4-10, across whichever techniques each requirement routed to), cells mark the links.

**Gate (objective):**
- No empty requirement rows — every requirement links to ≥1 test case.
- Every test case links back to ≥1 requirement — enumerate any orphan test case (one with no requirement link) explicitly rather than leaving it unflagged.

### Step 12 — Report

Deliver: the routing decision per requirement (Step 3), the derived test cases per routed technique with their respective coverage numbers (EP/BVA %, decision-table feasible-column %, state-transition coverage level and %, t-way coverage, MC/DC condition pairs), the traceability matrix, and a residual list — what these techniques do *not* establish for this feature (e.g., detection superiority over other techniques, non-functional coverage, exploratory-testing gaps, anything the user should get from a different skill or technique).
