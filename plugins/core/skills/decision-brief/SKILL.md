---
name: decision-brief
description: >-
  A discipline for escalating a significant judgment call to the user as a methodologically sound
  decision brief instead of deciding unilaterally or asking a bare open question. The AI, not the
  user, is expected to know decision methodology — this skill supplies it; the user only has to
  pick. Use this whenever the AI is about to make, or is about to ask about, a direction call that
  belongs to the user — e.g. "이거 어떻게 할지 정해줘야 할 것 같은데", "선택지 정리해줘", "결정 상신", "방향 결정이
  필요해", "should I ask the user or decide myself", or any point where the AI itself is about to
  pose a bare "which do you want?" question about a significant choice. This skill should be
  invoked by the AI proactively, before it types that bare question, not only when the user names
  it. Do NOT use it for reversible, single-scope implementation choices the AI can just make and
  note (variable names, which loop construct, formatting nits, a library already implied by the
  existing stack) — escalating those is the Type-2-under-Type-1-process failure this skill itself
  warns against. Also do not use it to record a decision after the fact once already made (that is
  the decision-records skill's job) or to produce a general design doc.
---

# Decision Brief

## First: does this even need the procedure?

Run the Step 1 trigger test below before drafting anything. Most judgment calls that surface during development are reversible, single-scope, and already implied by context — the AI should just make those and move on, noting the choice in passing rather than interrupting the user with a brief.

- **Does the call clear the trigger test?** If none of the four conditions in Step 1 fires, decide it yourself, say what you decided and why in one line, and do not build a brief around it.
- **Is this actually a bare question the AI was about to ask?** If the AI's instinct was to type "should I do A or B?" with no structure behind it, that instinct is exactly what this skill replaces — stop, run the procedure, and escalate with a brief instead of the bare question.
- **Has the user already decided this, explicitly or by established convention in this codebase/conversation?** If so there is nothing to escalate — follow the existing call, don't relitigate it.
- **Is the ask "record why we already decided X"?** That is decision-records' job, not this skill's — a brief is for a decision still open, not one already made and needing a paper trail.

Everything below applies only once a real, still-open, user-owned judgment call is on the table.

## Evidence grade — read before citing this to anyone

Three layers, and they must not be blurred together:

- **Procedure standards** — the Decision Quality six elements (SDG/Stanford, Ron Howard's decision-analysis lineage, 1960s), Kepner-Tregoe's musts/wants arithmetic (Kepner & Tregoe, *The Rational Manager*, 1965), and MAP/decision-hygiene ordering (Kahneman, Lovallo & Sibony, MIT SMR 2019 → *Noise*, 2021) are well-defined, expert-consensus, industry-standard procedures. **No RCT shows that following them causes better decision outcomes.** Treat them as a rigor scaffold, not a proven-effective intervention.
- **Observational numbers** — Paul Nutt's organizational-decision research (AME 1999; *Why Decisions Fail*, 2002): 400+ real decisions over 20+ years, about half failed (operationalized as not fully implemented/used two years out; a third never used). Failure was roughly 4x more likely when the decision-maker embraced the first idea without investigating alternatives — this is the basis for the single-option ban in Step 3. This is a large real-decision dataset, but it is non-randomized, retrospective, and correlational; Nutt himself was self-critical of it in 2011, and no independent replication was confirmed. Also from this dataset: participation-based approaches succeeded over 80% of the time but were used in only 1 of 5 decisions, while power-based tactics (edict/persuasion) succeeded only about a third of the time yet were used in roughly 60% of cases — cite this as motivation for genuine alternatives and a real trade-off table, not as a guarantee.
- **Convention, no data** — Bezos's Type 1 (irreversible, "one-way door") / Type 2 (reversible, "two-way door") split (2015 Amazon shareholder letter) is a practitioner triage label with no empirical study behind it; reversibility-based thinking predates it (real options theory). Use it only to decide whether to escalate at all (Step 1), never as evidence that the resulting decision will be better.

**Never claimed by this skill**: that AHP or any pairwise-comparison method has resolved its rank-reversal debate (it hasn't — 40 years unresolved, and AHP's CR<0.1 consistency gate was not confirmed in verification; this skill deliberately uses KT's simpler must/want arithmetic instead), that decision analysis was "coined in 1963 at Stanford" (say only "Howard's decision-analysis lineage, 1960s"), or any statistic not listed above.

**What this skill actually delivers**: your escalations will be well-structured, evidence-labeled, and auditable. It does **not** deliver "your decisions will provably succeed more often" — no evidence base here supports that stronger claim.

## Procedure

### Step 1 — Escalation trigger: does this belong to the user?

Check the candidate judgment against these four binary conditions:

| # | Condition | Yes/No |
|---|---|---|
| a | Reversing the choice later would cost more than a sprint of work (Type-1-shaped, in Bezos's convention-only framing) | |
| b | It sets product or team direction beyond the current task | |
| c | It trades off values only the user owns (cost vs. speed vs. quality vs. risk appetite) | |
| d | The user has explicitly reserved this class of decision for themselves | |

**Gate**: record yes/no for all four. Any single "yes" → escalate with a full brief (continue to Step 2). All four "no" → do **not** escalate; decide it yourself and note the decision in one line. Treating a reversible, single-owner, in-scope micro-decision as if it needed a brief is the Type-2-under-Type-1-process failure Bezos named — it is exactly as much a failure mode as under-escalating.

### Step 2 — Frame statement

Write one sentence naming (a) what is being decided and (b) what is explicitly out of scope for this decision.

**Gate**: the sentence exists and contains both the "what" and the "what's excluded" — a frame that only says what's being decided, with no stated boundary, fails this gate.

### Step 3 — Alternatives: the single-option ban

List at least two genuinely distinct alternatives, plus the status quo / "do nothing" option whenever it is actually viable. A recommendation paired with a strawman does not satisfy this — apply the non-strawman test: every alternative must have at least one criterion (see Step 5) on which no other alternative beats it — ties count as a win (a non-dominated test, so two options tied on "cheapest" both pass). If an alternative is beaten everywhere, either find its real strength or discard it and find a genuine alternative instead.

**Gate**: ≥ 2 genuinely distinct alternatives NOT counting the status quo (status quo is additional, listed whenever viable); a "wins on ___" cell is filled for every alternative before moving on. This is grounded directly in Nutt's ~4x single-option failure figure — labeled above as observational, not causal proof.

### Step 4 — Musts filter (Kepner-Tregoe)

List the non-negotiable requirements ("musts"). Any alternative failing a must is eliminated immediately, with the specific failed must named.

**Gate**: every eliminated alternative cites the must it failed by name. Survivors must number ≥ 2 — if only one alternative survives, the musts made the decision, not a trade-off; report that plainly ("the musts eliminated all but one option — there is no live choice left to escalate on this axis") rather than staging a fake comparison in Step 5.

### Step 5 — Trade-off table (KT wants + MAP ordering)

Name the want-criteria, each with a weight 1–10 (proposed by the AI, adjustable by the user). Rate every surviving alternative against every criterion, with the evidence behind each rating and that evidence's grade (procedure-standard / observational / convention / plain judgment) shown in the cell. Compute weighted sums (weight × rating, summed per alternative).

**MAP ordering gate**: every per-criterion cell for every alternative must be filled in *before* any recommendation or overall-ranking language is written — assessments precede judgment, not the reverse.

**Gate**: no empty cells; weighted arithmetic shown, not asserted; the recommendation row/line appears physically after the completed table, never interleaved with it.

### Step 6 — Recommendation + falsifier

State: the recommended alternative, a numeric confidence (e.g. 0–100), and at least one concrete disconfirming condition — what specific evidence or measurement would flip this recommendation.

**Gate**: all three elements present, and the falsifier is checkable — an observable number, event, or measurement ("if X exceeds Y" / "if the vendor's SLA drops below Z"), not a vague hedge like "if circumstances change."

### Step 7 — Closed handoff

End with a closed question the user can answer by picking one of the Step 5 alternatives (AskUserQuestion-shaped), with the Step 6 recommendation marked as such among the options. After the user decides, check whether the decision clears the decision-records trigger test (a separate skill) — if it does, route to decision-records to get it written down; if not, the pick alone is sufficient and no further artifact is needed.

**Gate**: the closed question lists exactly the same alternatives that appear in the Step 5 table — no option is smuggled in at the last moment that wasn't scored, and no scored alternative is silently dropped from the question.

## Verdict

Report, per escalation:

- Step 1 result: escalate / decide-yourself, with the specific condition(s) that fired (or "all four no" if self-decided).
- Step 2 frame sentence.
- Step 3 alternative table with "wins on" cells and the Nutt figure cited with its observational label.
- Step 4 musts table naming any eliminations and the surviving count.
- Step 5 full weighted trade-off table, evidence-graded per cell, recommendation appearing only after it.
- Step 6 recommendation, numeric confidence, and the checkable falsifier.
- Step 7 closed question as actually posed to the user.

Never compress this into a single "recommendation: X" line with the scaffolding stripped out — the entire point of escalating instead of asking a bare question is that the user can audit *how* the recommendation was reached, not just what it is.
