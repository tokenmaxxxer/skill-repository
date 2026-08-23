---
name: decision-records
description: >-
  Use whenever the user wants a decision written down for future reference or wants their
  existing ADR practice checked. A discipline for deciding WHICH decisions must be recorded
  as Architecture Decision Records (ADRs) and for enforcing record completeness once one is
  warranted — a set of binary trigger conditions and a syntactic completeness check, not a
  "write a doc about everything we decide" habit. Trigger on "이 결정 ADR로 남겨줘", "아키텍처 결정
  기록해줘", "왜 이렇게 했는지 문서로 남기자", "document this architecture decision", "is our ADR practice
  actually being followed". Do NOT use for escalating a still-open direction call to the
  user (use decision-brief), for decisions cheap to reverse and scoped to one person/team
  with no lasting cross-team consequence, or for writing general design docs or specs.
---

# Decision Records

## First: does this even need the procedure?

Check these before reaching for the ADR template, because writing one for every decision is how ADR repositories die of noise before they die of neglect:

- **Does the decision clear the trigger test below?** If none of the four trigger conditions in Step 1 holds, say so explicitly and stop — "no record required" is a valid, useful output, not a cop-out.
- **Is this a design doc or spec question instead?** ADRs record a single decision and its rationale, not an ongoing design surface. If what's wanted is "document how this subsystem works," that's different from "document why we chose X over Y" — point that out rather than forcing the Nygard template onto it.
- **Is there already a complete, current ADR for this exact decision?** If one exists and nothing about the decision has changed, don't write a duplicate — point to the existing one. If the decision *has* changed, that's the supersede path in Step 3, not a fresh unrelated record.
- **Is the user asking you to audit an existing ADR practice, not write a new record?** Then skip straight to Step 2 (completeness) and Step 4 (liveness) against what already exists, rather than starting from the trigger test.

Everything below applies once there's an actual decision on the table (or an existing repo to audit) and at least someone is willing to look at real evidence for it.

## Evidence grade — read before citing this to anyone

- **Origin**: Michael Nygard's blog post "Documenting Architecture Decisions" (2011-11-15) defined the lightweight ADR: a template of exactly five sections — Title, Context, Decision, Status, Consequences — with Status drawn from a fixed small vocabulary (proposed / accepted / deprecated / superseded) and Decision written in active voice ("We will ..."). His stated motivation: decision rationale gets lost over a project's life, leaving teams to either blindly follow or blindly reverse decisions nobody remembers the reasoning for.
- **Industry endorsement, not effectiveness proof**: ThoughtWorks Technology Radar placed lightweight ADRs in Trial (Nov 2016) and promoted them to Adopt (Nov 2017, reaffirmed May 2018), explicitly recommending that most projects have no reason not to use them. Cite this as **authoritative industry endorsement** — it is not a measurement of outcomes.
- **The effectiveness evidence is thin.** The best available study is a single 2024 peer-reviewed action-research paper (ECSA), conducted at one company, based on 7 interviews and 3 months of observation. Its own authors note the near-absence of empirical evidence on ADR applicability and usefulness. There is no randomized trial, no cross-org survey, no replication. Say plainly: claims like "ADRs speed up onboarding" or "ADRs reduce rework" are **plausible, not empirically established.**
- **Documented failure mode**: roughly half of ADR repositories in the wild contain fewer than 5 records — teams pilot the practice and then abandon it. This is exactly why Step 4 (liveness gate) exists below; without it, this skill would just be encouraging another repo that stalls at record #3.
- What *is* objective here: template conformance and the trigger test are syntactic and checkable regardless of the thin effectiveness base. Lead with that checkability, not with unproven productivity claims.

## Procedure

### Step 1 — Trigger test: does this decision need an ADR?

Check the candidate decision against these four binary conditions:

| # | Condition | Yes/No |
|---|---|---|
| a | Reversing it later would cost more than a sprint of work (expensive-to-reverse) | |
| b | It constrains or crosses more than one team's work | |
| c | It selects between technologies/vendors/protocols expected to outlive the current quarter | |
| d | Someone already asked "why did we do it this way?" about it and no written answer existed | |

**Gate**: any single "yes" → an ADR is required. All four "no" → explicitly output "no record required" and stop. Do not record decisions that clear none of these — over-recording trivia is precisely how repositories drown and get abandoned (see the liveness evidence above).

### Step 2 — Record completeness check (syntactic, per-section pass/fail)

For a decision that triggered Step 1, check the drafted or existing ADR section by section:

| Section | Pass condition | Fail condition |
|---|---|---|
| Title | Contains both the decision subject and the chosen option (e.g. "Use Postgres for the event store") | Missing, or a bare topic noun with no chosen option ("Database", "Event store") |
| Context | States at least one concrete force, constraint, or alternative that made this a real decision | Names no alternative or constraint — reads as scene-setting with nothing at stake |
| Decision | Single sentence, active voice ("We will ...") | Passive or hedged phrasing ("It was decided that...", "X might be used") |
| Status | Exactly one value from {proposed, accepted, deprecated, superseded} | Any other value, or missing |
| Consequences | Lists at least one negative/accepted cost alongside any benefits | All-upside list — every real decision has a cost; an all-benefit Consequences section fails |

**Gate**: build the five-row table above for every ADR being checked. Any single row marked fail means the ADR is incomplete — name the specific failing row(s), don't average them into a vague "mostly fine."

### Step 3 — Immutability & supersede rule

Once an ADR's Status is `accepted`, its Context and Decision content is never edited to mean something different. A changed decision gets a **new** ADR:

- The new ADR's Status starts at `proposed` or `accepted`, and its Context/Decision references the old ADR by ID/link.
- The old ADR's Status flips to `superseded`, linking forward to the new one.

**Gate** (binary): was any `accepted` ADR's Decision or Context content edited in place to mean something different than when it was accepted? If yes, that's a violation — flag it and require a proper supersede instead of an edit.

### Step 4 — Liveness gate

This is the direct countermeasure to the documented pilot-then-abandon failure mode (roughly half of real ADR repos stall under 5 records). At any review point, check:

1. Has at least one ADR been added within the last quarter, **or** is there an explicit note that no trigger-condition decision (Step 1) occurred in that period?
2. Compare two counts for the period: the number of new ADRs written vs. the number of decisions the user can point to (from meeting notes, PRs, incident retros) that would have cleared the Step 1 trigger test.

**Gate**: if trigger-condition decisions occurred in the period but zero new ADRs were written, the discipline has lapsed — flag it explicitly and name which decisions should have had one, rather than letting the repo's silence pass as "nothing happened."

## Verdict

Report, per decision or per audit:

- Step 1 result: required / not required, with the specific condition(s) that fired.
- Step 2 table, for any ADR drafted or reviewed, with named failing sections if any.
- Step 3: clean, or a named violation (which ADR, what was edited).
- Step 4: liveness holding, or lapsed — with the specific undocumented decisions named.

Never round these into a single "ADR health: good/bad" score — each gate has its own consequence, and a passing template with a lapsed liveness gate is a different problem than a failing template with good cadence.
