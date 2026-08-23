---
name: test-derivation
description: >-
  Use whenever the user wants test cases pulled from written requirements/acceptance criteria,
  wants help deciding which black-box technique fits a requirement, or wants requirements and
  tests linked in a traceability matrix — routing each requirement by problem shape to
  equivalence partitioning, boundary value analysis, decision tables, state transition testing,
  pairwise/t-way combinatorial testing, MC/DC, or Given-When-Then scenarios. Trigger on requests
  like "이 수용 기준으로 테스트 케이스 뽑아줘", "어떤 테스트 기법 써야 해", "derive test cases from these acceptance
  criteria", "build a traceability matrix". Do NOT use when there are no written requirements
  yet (requirements-quality), when the ask is judging whether existing tests actually verify
  anything (use test-depth-audit), or for non-functional testing (performance, security,
  usability) these techniques don't cover.
---

# Test Derivation

## First: does this even need the procedure?

Check these before running the full derivation, because forcing it onto the wrong input wastes the user's time:

- **Are there written requirements or acceptance criteria at all?** If the user only has a vague feature idea or a one-line ticket title with no stated acceptance criteria, this isn't a test-derivation problem yet — it's a requirements-quality problem. Say so and point to a requirements-quality pass first. Garbage in, garbage tests out: deriving from unwritten requirements just means silently inventing the requirements too.
- **Does the user already have tests and a matrix, and just want them run or summarized?** If so, just do that task — don't re-derive from scratch.
- **Is this actually a non-functional ask** (performance, security, accessibility, usability)? Equivalence partitioning and boundary value analysis are black-box *functional* techniques. Say plainly that this skill doesn't cover the non-functional dimension and point to the relevant skill instead (e.g. `usability-eval` for usability).
- **Is the user asking for a subjective quality opinion on existing tests** ("are these good tests?") rather than derivation? That's a review task, not a derivation task — this skill's gates only apply going forward from requirements to new/updated cases.

Everything below applies when there is at least one written requirement or acceptance criterion to derive from.

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

### Step 3a — Classify requirements by risk and decide derivation depth

Before deriving detailed test cases, classify each requirement so the procedure invests full enumeration only where the risk justifies it. Not every requirement needs the same depth — deriving boundary values for an "OK" button label wastes tokens without improving safety.

Score each requirement on two axes:

- **A: Impact of failure** — could a bug in this requirement cause safety/regulatory harm, data loss, revenue loss, or unrecoverable user impact?
- **B: Complexity** — does it route to 2+ techniques, or have 3+ conditions/states/parameters?

| Level | Rule | Derivation depth |
|---|---|---|
| **High** | A or B is yes | Full derivation at all routed techniques. Explicit partition lists, boundary enumeration, decision columns, state model, parameter model — all written out. Coverage percentages with itemized gap lists. Full GWT scenarios. |
| **Medium** | Neither A nor B, but user-facing functional behavior | Derive test cases per routed technique, but in summary format: partition names and counts without itemized lists; boundary variant named with coverage % but not per-item enumeration; decision table as condition count × feasible column count. GWT scenarios present but one-line. |
| **Low** | Neither A nor B, cosmetic/informational/trivial | One GWT happy-path scenario. Coverage noted as "N requirements, basic scenario only — no boundary/combination analysis needed." No per-technique derivation. |

**Gate:** every requirement has a written High/Medium/Low classification with one-phrase rationale. Record as a compact table before proceeding. This classification is the audit record for why depth varied — a reviewer can see that Low requirements were explicitly judged low-risk, not silently skipped.

The depth rule above applies to all of Steps 4–10: execute each step at the depth dictated by the requirement's classification. Low requirements contribute only their GWT scenario and a classification note; they do not generate partition lists, boundary items, decision tables, state models, parameter models, or MC/DC pairs.

### Step 4 — Identify input domains and enumerate partitions (EP/BVA route)

For each High or Medium requirement that routed to EP/BVA, write out the equivalence partition list. High: explicit, named partitions with counts. Medium: partition names and total count, no itemized list.

**Gate (objective, but externalizes the judgment call):**
- For High requirements: a written partition list exists per input, with a stated total count (e.g., "status field: 3 valid partitions, 2 invalid partitions"). This list must exist and be reviewable *before* Step 6's coverage number is computed — do not compute coverage against an implicit or unwritten partition list.
- For Medium requirements: partition names and total count stated, itemized list optional.
- Low requirements: the Step 3a classification note suffices; no partition list required.

### Step 5 — Boundary enumeration for ordered partitions only (EP/BVA route)

For each High requirement with ordered partitions: name the chosen variant — 2-value or 3-value — and enumerate the boundary items per that variant's definition. For Medium requirements: state the variant and coverage %, skip per-item enumeration.

**Gate (objective):**
- For High: every ordered partition has boundary items listed matching the named variant. Every unordered partition is explicitly marked **N/A for BVA** (not silently skipped).
- For Medium: variant named, coverage % stated, per-item list not required.

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

Build a requirements × test-cases matrix: rows are requirements/acceptance criteria, columns are test cases (the GWT scenarios plus any cases derived from Steps 4-10, across whichever techniques each requirement routed to), cells mark the links. Apply depth by classification: High requirements have individually named test cases; Medium and Low requirements may be grouped by technique-type counts.

**Gate (objective):**
- No empty requirement rows — every requirement links to ≥1 test case.
- Every test case links back to ≥1 requirement — enumerate any orphan test case (one with no requirement link) explicitly rather than leaving it unflagged.

### Step 12 — Report

Deliver:

1. **Classification table** from Step 3a (requirement × risk level × rationale — the audit record for depth decisions).
2. **Routing decisions** per requirement (Step 3).
3. **Derived test cases** per technique, at the depth dictated by classification:
   - High: full coverage with itemized gap lists, EP/BVA %, decision-table feasible-column %, state-transition coverage level and %, t-way coverage, MC/DC condition pairs.
   - Medium: coverage percentages and summary counts, without per-item gap enumeration.
   - Low: GWT scenario + classification note.
4. **Traceability matrix**, with High requirements individually linked and Medium/Low grouped.
5. **Residual list** — what these techniques do *not* establish for this feature (e.g., detection superiority over other techniques, non-functional coverage, exploratory-testing gaps, anything the user should get from a different skill or technique).

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- S1 — Evidence grade — read before citing this to anyone → references/rules.md
