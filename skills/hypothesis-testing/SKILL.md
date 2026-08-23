---
name: hypothesis-testing
description: >-
  Use whenever someone wants to test whether an idea, feature, or direction actually works
  before sinking more into it — whenever a go/kill/pivot/persist decision is still open and
  the metric or threshold has not yet been written down. The scientific approach to
  entrepreneurial and product decisions: treat an idea as a theory, derive falsifiable
  hypotheses, PRE-REGISTER the metric, threshold, and decision rule before any data is
  collected, then let that registered rule — not post-hoc judgment — make the
  kill/pivot/persist call. Trigger on "이 아이디어 될지 검증해보자", "피벗해야 하나", "가설 세워서 테스트하자", "how do
  we know if this is working", "should we kill this or keep going". Do NOT use once a test
  is already running with thresholds fixed, for a decision already committed with no option
  to stop, for pure preference calls with no observable outcome (use decision-brief), or for
  the discovery-role in-repo variant (use product-discovery-hypothesis-testing).
---

# Hypothesis Testing

## First: does this even need the procedure?

Run this gate before drafting a theory statement or a registration form — most of the value of this skill comes from applying it only where a real, still-open decision exists, and forcing it elsewhere just produces theater around a call that was already made.

- **Is there a genuine go/kill/pivot/persist decision still ahead?** The option to NOT proceed must still be realistically open. If the team is already committed — funded, shipped, contractually locked — and is just executing, this is an execution problem, not a testing problem: route back to planning/execution, not here.
- **Is this actually about an idea, feature, or direction, with an observable outcome that could settle it?** If the question is pure preference or creative taste — which of two taglines "feels right," which color the team likes — no test result could ever falsify a preference. That is decision-brief territory if it needs to be escalated at all, not this skill.
- **Has a test already been registered and started?** If thresholds are already fixed and data collection is underway, don't re-open the registration — go straight to Step 5 (run to the registered rule) and Step 6 (verdict). Rewriting the threshold now is the exact failure mode this skill exists to prevent.
- **Is there really a theory here, or just a task?** "Build the login page" has no theory to falsify. If nobody can say what would have to be true for the idea to be wrong, there is no hypothesis to extract yet — that's a scoping problem, handle it before invoking Step 2.

Everything below applies only once a real, still-open, falsifiable go/kill/pivot/persist decision is on the table.

## Evidence grade

Pre-registered thresholds plus a mechanical verdict rule caused better termination and pivot behavior in four RCTs (759 firms, instructor-led). This self-serve procedure is an inference from that method, not itself RCT-validated. Full evidence base in `references/evidence.md`.

## Procedure

### Step 1 — Scope gate

Confirm: is there a genuine go/kill/pivot/persist decision still ahead, on an idea, feature, or direction, with the option to not proceed still genuinely open?

**Gate**: if the decision is already committed and only execution remains, exit and route to execution — do not build a theory around a call that's already made. If the question is pure preference or creative taste where no observable outcome could settle it, exit and route to decision-brief if it needs escalating at all. Only continue if both checks pass.

### Step 2 — Theory articulation

Write the causal sentence: **"We believe X will produce Y for Z because MECHANISM."**

**Gate**: the sentence names an actor/segment (Z), an outcome (Y), an intervention (X), and — critically — the **"because" clause**. A sentence missing the mechanism fails this gate: an idea without a stated mechanism cannot generate diagnostic hypotheses, because there's nothing to falsify except the outcome itself.

### Step 3 — Hypothesis extraction

Derive 1-3 falsifiable hypotheses from the theory.

**Falsifiability gate, per hypothesis** — it must name all three:
1. An observable metric.
2. A direction or threshold.
3. Who/where it is measured.

"Users will love it" fails all three. "≥25% of pilot users who try the feature use it again within 7 days" passes. Ask of every hypothesis: **is there a conceivable result that would count against it?** If no result could ever fail it, it is not a hypothesis — rewrite it before moving on.

### Step 4 — PRE-REGISTRATION (the active ingredient)

Before any data is collected, fill out the registration form in writing, in full:

| Field | Content |
|---|---|
| (a) Hypothesis | The falsifiable statement from Step 3 |
| (b) Test design | The cheapest test that can falsify it — landing page, concierge MVP, prototype interviews, A/B test |
| (c) Metric and measurement window | Exactly what is measured, over what period |
| (d) Threshold values with decision rule | e.g. "≥T → persist; <T but ≥T' with learning L → pivot candidate; <T' → kill" |
| (e) Sample size / duration | Decided in advance, not adjusted once data starts arriving |
| (f) Date stamp | When the registration was written |

**Gate**: all six fields are filled **before the test starts**. A registration written or edited after data collection has begun is a **procedure violation** and must be recorded as such, not quietly absorbed — the whole value of pre-registration is that it precedes the data. Post-hoc thresholds are the exact failure mode this skill exists to kill; treat "I'll set the threshold once I see the numbers" as a hard stop, not a shortcut.

### Step 5 — Run the registered test

Execute the test exactly as registered.

**Gate**: a deviations log exists (it may be empty). Any deviation — metric changed, window extended, sample redefined — is logged with a reason, in real time, not reconstructed afterward. An undocumented deviation discovered later invalidates the run's verdict; there is no partial credit here.

### Step 6 — Verdict by the registered rule

Compare the measured result to the pre-registered thresholds. The decision — kill, pivot, or persist — follows the registered rule mechanically, not from a fresh judgment call made after seeing the number.

**Gate**: the verdict sentence cites the registered threshold and the measured number side by side (e.g., "registered threshold ≥25% at 7 days; measured 18% → below T, above T' → pivot candidate"). **Override rule**: the user may override the registered decision, but the override must be written down explicitly as an override, with its reason. This is auditable, not silent — it preserves the human's final authority while killing quiet post-hoc rationalization dressed up as "the data was ambiguous."

### Step 7 — Pivot discipline

If the verdict is "pivot," it spawns a **new** theory (return to Step 2) and a **new** registration (Step 4) — it does not recycle the old thresholds onto a different idea.

**Gate**: pivot count is tracked across cycles, and the log distinguishes kill / pivot / persist outcomes at each cycle. State the evidence pattern plainly when relevant: trained founders in the RCTs converged on **1-2 focused pivots**, not zero (never revisiting a bad theory) and not many (thrashing). The escalation trigger is itself pre-committed: **≥3 pivots in one idea lineage with no kill and no persist verdict → stop cycling and escalate the direction call via decision-brief.** (The threshold mirrors the RCT pattern of 1-2 focused pivots; crossing it means the theory keeps failing to generate a decidable test.)

## Verdict

Classify the stakes before reporting depth. Write the classification in the verdict so it's auditable.

**High-stakes** (expensive pivot, hard-to-reverse commitment, or decision that will block other work): full 7-element report per cycle — scope gate result, theory sentence, each hypothesis with falsifiability check, full six-field registration with date stamp and gate-violation flag, deviations log (or its explicit emptiness), verdict sentence citing registered threshold vs. measured number plus any override with reason, and cumulative pivot count with kill/pivot/persist history.

**Directional / early-stage**: decision + metric + threshold only (3 elements) — state the kill/pivot/persist call, cite the metric and the measured vs. registered threshold, and record the cycle's outcome in the pivot log. Full traceability is preserved in the registration form itself; the directional report does not reprint it.

If stakes are unclear, default to full 7-element reporting.
