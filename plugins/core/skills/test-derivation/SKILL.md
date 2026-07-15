---
name: test-derivation
description: >-
  Derives test cases from written requirements/acceptance criteria using standardized black-box
  techniques (Given-When-Then scenarios, equivalence partitioning, boundary value analysis) and
  maintains the requirements↔tests traceability matrix. Use this whenever the user wants test
  cases pulled out of acceptance criteria or requirements, or wants requirements and tests linked
  — e.g. "이 수용 기준으로 테스트 케이스 뽑아줘", "테스트 케이스 도출해줘", "경계값 테스트 만들어줘", "요구사항이랑 테스트
  매핑해줘", "추적성 매트릭스 만들어줘", "derive test cases from these acceptance criteria", "generate
  boundary value tests", "build a requirements-to-tests traceability matrix", "what equivalence
  classes am I missing". The value is coverage discipline and removal of tedious manual
  cross-referencing — not a claim that these techniques find more bugs than other techniques. Do
  NOT use it when there are no written requirements or acceptance criteria to derive from yet
  (that's a requirements-quality problem — get the requirements written first), when the user
  already has a full test suite and traceability matrix and just wants them executed or reported
  on, or when the ask is about non-functional testing (performance, security, usability) that
  these black-box techniques don't cover.
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
  - Honesty requirement: the denominator is "identified" partitions/boundaries. Identifying them is a judgment call the syllabus does not mechanize — two competent testers can produce different partition lists from the same requirement. The gates in this skill are objective *after* identification. That's why Step 3 forces the identification list to be written down and reviewable *before* any coverage percentage is computed — the coverage number is only as honest as the list underneath it.
  - Attribution: ISTQB's own BVA white paper attributes 2-value BVA to Craig (2002) and Myers (2011, 3rd edition of *The Art of Software Testing*), and 3-value BVA to Koomen (2006) / O'Regan (2019). Do not state "Myers 1979" or any other unverified origin claim.
- **Detection-effectiveness evidence is weak — state this plainly, don't oversell.** The only controlled experiment in our evidence base (Roper, Wood & Miller 1997, 47 students, small C programs) found code reading, functional testing (EP/BVA), and structural testing "broadly similar" in effectiveness, with the relative ranking depending on program and fault characteristics. The one effect that *was* robust: **combining techniques was substantially more effective than any single technique alone.** Juristo, Moreno & Vegas (2004), a 25-year review of testing-technique experiments, concluded the field's knowledge base has low maturity overall.
  - This skill's honest value claim is therefore: **(a)** combining techniques beats any single one (the one robust finding), **(b)** coverage accounting surfaces input space nobody examined, **(c)** traceability produces a documented, measured speed/correctness effect (below) — **not** "EP/BVA finds more bugs than other techniques," which is not established.
- Given-When-Then (GWT): origin is Dan North, with Chris Matts, late 2004 (primary source: North's "Introducing BDD"). A story's behavior *is* its acceptance criteria expressed as automated scenarios — that's the design intent, not an added layer on top. As of a 2018 review, no controlled experiments directly evaluating BDD's benefits existed; state this claim with that time bound rather than as settled fact. The GWT gate used here is purely syntactic (three-part structure present) — it is not a claim that GWT scenarios are more effective than other scenario formats.
- Traceability: across a 63-paper systematic mapping, change impact analysis is the dominant documented use (38 of 45 change-management studies). The one quantified controlled effect: **Mäder & Egyed, Empirical Software Engineering (2015)**, 71 industrial practitioners, within-subject design — maintenance tasks completed **24% faster and ~50% more correct** with traceability in place. Label this as a single experiment's result, not a universal law. 57% of the field's evidence base is toy-example level — treat the 24%/50% figures as the strongest single data point, not the average outcome. A safety-critical-domain interview study found engineers spend roughly 50-100 hours/year on manual change-impact analysis — that's the tedium this skill's matrix is meant to remove.
- **Not verified, do not state as fact:** claims that DO-178C or ISO 26262 mandate clause-level traceability are commonly asserted, but our verification round did not confirm the actual clause text. If a safety-critical mandate comes up, say "commonly cited, unverified in our research" — never state it as a confirmed regulatory requirement.

## Procedure

### Step 1 — Scope gate

Confirm there are written requirements or acceptance criteria to derive from — list them or ask the user to paste/link them.

**Gate:** at least one written requirement/acceptance criterion is in hand. If none exists, stop here and route to a requirements-quality pass first — do not invent requirements to keep going.

### Step 2 — Given-When-Then scenario per acceptance criterion

For each acceptance criterion, write at least one Given-When-Then scenario expressing it as a concrete, automatable case.

**Gate (syntactic, objective):**
- Every scenario has all three parts (Given, When, Then) present and non-empty.
- Every acceptance criterion has ≥1 scenario mapped to it — do the count comparison explicitly: `criteria count` vs. `scenarios count / criteria covered`, and name any criterion with zero scenarios.

### Step 3 — Identify input domains and enumerate partitions

For each input or condition referenced across the scenarios, write out the equivalence partition list explicitly: valid classes and invalid classes, each named.

**Gate (objective, but externalizes the judgment call):**
- A written partition list exists per input, with a stated total count (e.g., "status field: 3 valid partitions, 2 invalid partitions").
- This list must exist and be reviewable *before* Step 5's coverage number is computed — do not compute coverage against an implicit or unwritten partition list.

### Step 4 — Boundary enumeration for ordered partitions only

For each partition identified in Step 3 that is **ordered** (numeric ranges, dates, sequences, anything with a "less than / greater than" relationship), name the chosen variant — 2-value or 3-value — and enumerate the boundary items per that variant's definition.

**Gate (objective):**
- Every ordered partition has boundary items listed matching the named variant (2-value: boundary + one neighbor; 3-value: boundary + both neighbors).
- Every unordered partition is explicitly marked **N/A for BVA** (not silently skipped) — BVA only applies to ordered partitions.

### Step 5 — Coverage computation

Apply the ISTQB formulas from the evidence-grade section:
- `EP coverage % = (partitions exercised by ≥1 test case ÷ total identified partitions) × 100%`
- `BVA coverage % = (boundary items exercised by ≥1 test case ÷ total identified boundary items) × 100%`

**Gate (numeric, objective):** state both percentages. For anything short of 100%, name the specific uncovered partition/boundary item and either add a test case for it or record an explicit, named exclusion reason (not a silent gap).

### Step 6 — Traceability matrix

Build a requirements × test-cases matrix: rows are requirements/acceptance criteria, columns are test cases (the GWT scenarios plus any EP/BVA-derived cases), cells mark the links.

**Gate (objective):**
- No empty requirement rows — every requirement links to ≥1 test case.
- Every test case links back to ≥1 requirement — enumerate any orphan test case (one with no requirement link) explicitly rather than leaving it unflagged.

### Step 7 — Report

Deliver: the derived test cases, the EP and BVA coverage percentages with any named exclusions, the traceability matrix, and a residual list — what these techniques do *not* establish for this feature (e.g., detection superiority over other techniques, non-functional coverage, anything the user should get from a different skill or technique).
