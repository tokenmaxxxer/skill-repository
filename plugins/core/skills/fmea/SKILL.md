---
name: fmea
description: >-
  A design-stage risk analysis procedure (Failure Mode and Effects Analysis): decompose a
  design/system/process into elements, enumerate how each element could fail, rate each failure
  mode on anchored Severity/Occurrence/Detection scales, and prioritize by severity first so a
  low-probability high-severity risk can never be buried under a low RPN. Use this when the user
  wants to find what could go wrong in a design or process before it ships — e.g. "이 설계에서
  뭐가 잘못될 수 있는지 분석해줘", "고장 모드 분석", "FMEA 해줘", "위험 분석해줘 설계 단계에서", "failure mode analysis",
  "what could go wrong with this design", "run an FMEA on this", "risk analysis before we build
  this". Do NOT use it after a failure has already happened in the field (that's root-cause /
  incident analysis, not this — point to `diagnose-first`), when there is no concrete
  design/system/process with enumerable components or steps to decompose, when the user only
  wants the official AIAG-VDA Action Priority decision tables reproduced verbatim (this skill
  does not have those verified — say so and point to the handbook), or for a single trivial,
  low-stakes change where a five-minute gut check is proportionate and a full worksheet is not.
---

# FMEA (Failure Mode and Effects Analysis)

## First: does this even need the procedure?

Check these before running the full worksheet, because forcing it where it doesn't fit wastes the user's time:

- **Has the failure already happened?** FMEA is a design-stage, before-the-fact procedure. If something already broke in production or the field, this is a root-cause / incident analysis question, not an FMEA question — point to `diagnose-first` instead.
- **Is there a concrete thing to decompose?** If the user can't point to a design, system, or process with distinguishable components or steps, there is nothing to enumerate failure modes against yet. That's a design/discovery gap, not an FMEA gap — say so rather than inventing structure to analyze.
- **Does the user just want the AIAG-VDA Action Priority tables?** This skill does not carry verified AP decision-table mechanics (see Evidence grade). If that's specifically what's being asked for, say plainly that the official handbook needs to be consulted and don't fabricate the table.
- **Is the change trivial, cheap, and reversible?** A one-line config default, a copy change. A full multi-element worksheet is overkill; a quick "what's the worst thing this could do" gut check is proportionate, if anything is needed at all.

Everything below applies when there's a real design or process on the table with enumerable parts and real consequences if something fails.

## Evidence grade — read before citing this to anyone

- **The scales and the procedure shape are industry-standard and codified** — this is why the exercise passes an objective-gate bar at all. Severity, Occurrence, and Detection are each 1–10 ordinal scales with standard anchor definitions (Severity 1 = no effect, 10 = hazard without warning; Detection 1 = almost certain detection, 10 = cannot detect), codified in the AIAG 4th-edition lineage. RPN = S × O × D, range 1–1000.
- **RPN ranking has confirmed, peer-reviewed methodological criticism** (academic origin: Bowles 2003):
  - Ordinal scales cannot be meaningfully multiplied — qualitatively different risks can land on the identical RPN (S=9,O=3,D=5 and S=5,O=9,D=3 both equal 135, and they are not the same risk).
  - Numeric action thresholds (e.g. "act if RPN > 100") are arbitrary. AIAG's own manual calls fixed RPN cutoffs a discouraged practice — there is nothing principled about 100 vs. 99.
  - **Detection masking**: low Occurrence and low Detection multiply a high-Severity failure down to a small number (S=9, O=2, D=2 → RPN 36), hiding a safety-critical risk below any reasonable cutoff. Teams end up chasing the biggest number instead of the highest-severity risk.
- **The AIAG-VDA FMEA Handbook (1st edition, 2019) replaced RPN ranking with Action Priority (AP).** That replacement is confirmed. The specific mechanics of the AP categorization were **not** confirmed in verification and must not be reproduced here. If the team needs the official AP tables, point them to the handbook directly; do not improvise the table.
- **Origin note (unverified, mention only with this caveat):** FMEA is commonly said to trace to US military standard MIL-P-1629 (1949) / MIL-STD-1629A. That lineage was not confirmed in our verification research — treat it as commonly-stated folklore, not established history, if it comes up at all.
- **Effectiveness evidence is observational, not experimental.** A healthcare systematic review (22 studies) found most studies report FMEA as useful for risk reduction — but there is no RCT and no meta-analytic effect size behind that. Only 14 of the 22 studies even computed an RPN. State plainly, if asked whether FMEA works: there is no randomized-controlled-trial evidence that FMEA reduces field defects, only case-study-level observational reporting.
- **What this skill actually delivers**: the decomposition + anchored-rating + severity-first-prioritization structure. That structure is checkable step by step regardless of whether RPN is computed at all. Lead with that, not with RPN as a score to optimize.

## Procedure

### Step 1 — Scope gate

Is there a concrete design, system, or process with components or steps that can be enumerated?

**Gate:** if there is no enumerable structure, stop and exit — go back to design or discovery work first, don't force a worksheet onto an undefined target.

### Step 2 — Decompose

List every component (for a design/system) or step (for a process) that makes up the target.

**Gate:** a numbered list exists, with the count stated (e.g., "7 components identified"). An unnumbered or open-ended list does not pass.

### Step 3 — Enumerate failure modes per element

For every element from Step 2, list at least one way it could fail to perform its intended function ("how could this fail to do its job").

**Gate:** every element has either (a) at least one failure mode listed, or (b) an explicit note "no credible failure mode identified" with a one-line reason. No element may be left blank.

### Step 4 — Effect and cause per failure mode

For each failure mode, fill in:
- **Effect** — what the user or downstream system actually experiences.
- **Cause** — why the failure mode would occur.

**Gate:** both cells are filled for every failure mode. A failure mode with an empty effect or cause is incomplete, not "obvious enough to skip."

### Step 5 — Rate S, O, D against anchors

Rate every failure mode on Severity, Occurrence, and Detection using the 1–10 scales below. Ratings must be made against the written anchor bands, not gut feel.

| Band | Severity (effect) | Occurrence (likelihood) | Detection (ability to catch before impact) |
|---|---|---|---|
| 1 | No discernible effect | Failure essentially eliminated / near-zero history | Almost certain detection before reaching the user |
| 2–3 | Minor annoyance, no function lost | Low — isolated occurrences in similar designs/processes | High — controls very likely to catch it |
| 4–6 | Moderate — function degraded, user notices, no safety/regulatory impact | Moderate — occasional failures in similar designs/processes | Moderate — controls may or may not catch it |
| 7–8 | High — major function lost, high dissatisfaction, no safety/regulatory impact | High — repeated failures in similar designs/processes | Low — controls unlikely to catch it |
| 9 | Very high — safety or regulatory issue, but with warning | Very high — failure recurs in most units/runs of similar designs | Very low — controls almost never catch it |
| 10 | Hazardous — safety or regulatory failure with **no warning** | Certain — failure occurs in nearly every unit/run | Cannot detect — no known control |

**Gate:** every S/O/D rating cites which band it matched (e.g., "S=9 — band: safety issue with warning"), for all three scales, for every failure mode. A bare number with no band citation does not pass.

### Step 6 — Prioritize (the critical design decision)

Do not rank by RPN alone. Instead:

1. **Sort by Severity first.** Every failure mode with **S ≥ 9** gets mandatory review, regardless of what Occurrence or Detection say. This is the direct countermeasure to detection masking: a rare, hard-to-detect, hazardous failure must not be allowed to hide behind a low O×D.
2. **Within each severity band**, order by Occurrence descending, breaking ties by Detection descending (harder-to-detect first). This is a fixed, reproducible rule — not a judgment call and not an O×D product.
3. Compute RPN if the team wants a single number to track, but **forbid numeric RPN action cutoffs** (no "act only if RPN > 100"). State the 99-vs-100 arbitrariness explicitly if someone proposes a cutoff, and note AIAG's own manual discourages the practice.

**Gate:** every S ≥ 9 mode has a disposition — either a mitigation action or a documented risk acceptance with a named acceptor (a person, not "the team"). No failure mode may be dismissed solely because its RPN fell below a chosen number.

### Step 7 — Actions

For every mitigation decided in Step 6, record:
- **Owner** — a named person or role.
- **Expected re-rating** — the S/O/D the team expects *after* the action is done.

**Gate:** every action row has an owner and a post-action S/O/D estimate filled in. An action with no owner or no re-rating is not a completed action, it's an idea.
