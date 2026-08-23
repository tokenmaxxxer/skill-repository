---
name: decision-brief
description: >-
  Use whenever the AI is about to make or ask about a direction call that belongs to the
  user — invoke proactively, before typing a bare "which do you want?" question. A
  discipline for escalating a significant judgment call as a methodologically sound decision
  brief instead of deciding unilaterally or asking a bare open question; the AI supplies the
  decision methodology, the user only has to pick. Trigger on "이거 어떻게 할지 정해줘야 할 것 같은데", "선택지
  정리해줘", "결정 상신", "should I ask the user or decide myself". Do NOT use for reversible
  implementation choices the AI can just make and note (variable names, formatting nits —
  escalating those is the Type-2 failure this skill warns against), or to record a decision
  after the fact (use decision-records).
---

# Decision Brief

## First: does this even need the procedure?

Run the Step 1 trigger test below before drafting anything. Most judgment calls that surface during development are reversible, single-scope, and already implied by context — the AI should just make those and move on, noting the choice in passing rather than interrupting the user with a brief.

- **Does the call clear the trigger test?** If none of the four conditions in Step 1 fires, decide it yourself, say what you decided and why in one line, and do not build a brief around it.
- **Is this actually a bare question the AI was about to ask?** If the AI's instinct was to type "should I do A or B?" with no structure behind it, that instinct is exactly what this skill replaces — stop, run the procedure, and escalate with a brief instead of the bare question.
- **Has the user already decided this, explicitly or by established convention in this codebase/conversation?** If so there is nothing to escalate — follow the existing call, don't relitigate it.
- **Is the ask "record why we already decided X"?** That is decision-records' job, not this skill's — a brief is for a decision still open, not one already made and needing a paper trail.

Everything below applies only once a real, still-open, user-owned judgment call is on the table.

## Evidence grade

For full evidence grading — procedure standards, observational numbers, convention-only labels, and what this skill does and does not claim — see [references/evidence.md](references/evidence.md). In short: the procedures here are expert-consensus scaffolds with observational backing, not RCT-proven interventions; cite them with their evidence labels, never as guarantees of better outcomes.

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

**Gate**: the recommendation row/line appears physically after the completed table, never interleaved with it. For non-high-stakes escalations, this full weighted table may be omitted per the Verdict depth rule below.

### Step 6 — Recommendation + falsifier

State: the recommended alternative, a numeric confidence (e.g. 0–100), and at least one concrete disconfirming condition — what specific evidence or measurement would flip this recommendation.

**Gate**: all three elements present, and the falsifier is checkable — an observable number, event, or measurement ("if X exceeds Y" / "if the vendor's SLA drops below Z"), not a vague hedge like "if circumstances change."

### Step 7 — Closed handoff

End with a closed question the user can answer by picking one of the Step 5 alternatives (AskUserQuestion-shaped), with the Step 6 recommendation marked as such among the options. After the user decides, check whether the decision clears the decision-records trigger test (a separate skill) — if it does, route to decision-records to get it written down; if not, the pick alone is sufficient and no further artifact is needed.

**Gate**: the closed question lists exactly the same alternatives that appear in the Step 5 table — no option is smuggled in at the last moment that wasn't scored, and no scored alternative is silently dropped from the question.

## Verdict — stakes-based depth

The output format is determined by the stakes, not a one-size-fits-all mandate:

- **High-stakes** (expensive to reverse, sets binding direction, or the user explicitly requests full rigor): produce the full 7-step brief — frame sentence, alternative table with "wins on" cells, musts filter, full weighted trade-off table with evidence-graded cells, recommendation with numeric confidence and checkable falsifier, and closed handoff question.
- **Directional / medium-stakes**: produce a summary brief containing only: (1) decision what+excluded frame, (2) rationale — the key trade-off and why the recommendation wins on it, (3) the top risk or disconfirming signal, (4) the recommendation and closed question. Skip the full musts filter and weighted table.
- **Low-stakes**: produce a one-paragraph decision note — the recommendation, one-sentence rationale, and what would flip it. No tables, no formal frame.

The "do not escalate" path from Step 1 (all four conditions no) is distinct from low-stakes escalation: "do not escalate" means the AI decides and notes it in one line; low-stakes escalation means the AI still escalates but in abbreviated form.
