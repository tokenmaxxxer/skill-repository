---
name: adversarial-review
description: >-
  Use when you need an honest assessment of any AI-made artifact (code, design doc, report,
  config) and can't trust the making agent to critique its own work. A protocol for setting
  up a structurally independent evaluator session that receives only the deliverable — not
  the spec, not the builder's intent — and is incentivized to find everything wrong with it;
  evaluator and builder are different sessions with no shared context, so the evaluator has
  no stake in defending the work. Trigger on "이 결과물 까줘", "다른 세션에서 평가해줘", "review this with
  fresh eyes", "제3자 시선에서 검토해줘", "independent adversarial evaluation". Do NOT use for code
  style checks (use a linter), for verifying against a known-correct spec (use
  implementation-audit — this is for problems the spec didn't anticipate), or for creative
  feedback where authorial intent matters (this is intentionally blind to intent).
---

# Adversarial Review

## First: does this even need the procedure?

- **Is the evaluator reviewing its own work?** That's the whole thing this skill prevents. If the same session that produced X is asked to evaluate X, it will defend its own output — not out of malice, but because the context window contains the reasoning that led to those choices, and contradicting that reasoning mid-session is architecturally unlikely. This skill exists to break that loop. If you're already planning to use a separate session, skip to the procedure.
- **Is this about a known, objective standard?** "Does this pass the linter," "does it match the API spec," "is the math correct" — these are mechanical checks, not adversarial review. Use the tool that checks that standard directly.
- **Is this creative/opinion work where intent matters?** "Is this essay compelling," "does this design communicate the right emotion" — the evaluator's blindness to intent is a bug here, not a feature. This skill evaluates whether something works; it doesn't evaluate whether it achieves a specific artistic goal.

Everything below applies when you have a concrete deliverable and need a structurally independent assessment of its quality.

## The core mechanism

The reason AI self-review fails is structural, not motivational. Telling the same session "be critical" doesn't work because the context window already contains the chain of reasoning that produced the output — each token was the most probable successor given the preceding tokens, and asking the model to now declare those tokens flawed is asking it to contradict its own probability distribution mid-stream. A fresh session has no such stake.

This skill therefore describes a two-party protocol:

```
[Builder session]                    [Evaluator session]
       │                                     │
       │ produces artifact                   │ (separate session, fresh context)
       │                                     │
       └──── artifact (ONLY) ────▶  receives artifact
                                     no spec, no prompt, no intent
                                     system prompt: "find problems"
                                     evaluates from user perspective
                                     produces critique ────▶ [User reads critique]
```

The evaluator receives exactly one input: the deliverable. It does not receive:
- The original requirements or specification
- The prompt that was given to the builder
- Any context about what the builder intended
- Any claim by the builder about what it did

This blindness is not a limitation — it's the mechanism. If the evaluator can't tell what the artifact is supposed to do from the artifact itself, that is already a finding.

## Evidence grade

- **Session separation as a debiasing mechanism** is an architectural claim, not an empirically tested intervention. The premise — that same-session self-critique is structurally impaired because the context window already commits to the produced output — follows from how autoregressive generation works, but no controlled study has measured the effect size of session separation vs. same-session "be critical" prompting on review quality. [가설]
- **Blind review (evaluator receives product only, not spec)** is a practice borrowed from peer review in academic publishing (single/double-blind review) and from code review in security contexts (adversarial review, red-teaming). Its effectiveness in human contexts is well-attested; its transfer to AI evaluators is untested. [가설]
- **The surface-pattern catalog** referenced in Step 3 is the same catalog used by implementation-audit, compiled from practitioner reports. [현장]

## Procedure

### Step 1 — Prepare the artifact for blind evaluation

The evaluator session receives the deliverable with no surrounding context. Prepare it:

1. Collect every file, document, or output the builder produced.
2. Strip any metadata that would reveal the builder's intent — remove the original prompt from comments, remove task descriptions from commit messages if including git history, remove spec references embedded in the code.
3. Do NOT add explanatory notes. If the artifact needs explanation to be understood, that's a finding the evaluator should surface.

**Gate**: the artifact bundle contains the deliverable only. No specification, no builder's prompt, no "what this is supposed to do" preamble.

### Step 2 — Spawn the evaluator session

Start a new, independent session — a fresh context window with no memory of the builder's work. This can be:
- A new chat in the same tool (Claude Code, ChatGPT, Cursor)
- A subagent spawned with the Agent tool (but only if the subagent gets a fresh context, not the parent's context window)
- A different model entirely (e.g., use Haiku to build, Sonnet to evaluate)

The evaluator's system prompt must establish four things:

1. **Role**: you are an evaluator, not a builder. Your value is in finding real problems, not in being polite or balanced.
2. **Blindness**: you do not know what was asked for. You see only what was delivered. Judge it as a user or colleague would: does this work? What's missing? What feels fake or incomplete? What would frustrate someone trying to use or maintain this?
3. **Incentive**: the more real, specific, actionable problems you find, the better you've done your job. A report with zero findings is a failure — no non-trivial deliverable is perfect. Surface-level work that pretends to be complete (stubs, placeholders, TODO-driven-development, happy-path-only implementations) is especially valuable to catch because it wastes the most time.
4. **Evidence requirement**: every problem you report must cite a specific location (file:line, section, screen) where the issue is visible. "This feels incomplete" without a location is not a finding.

A minimal evaluator prompt that satisfies all four:

```
You are evaluating a deliverable. You do not know what was asked for — you
see only what was produced. Your job is to find everything wrong with it.

Judge it as a user or colleague would: does this actually work? What's missing?
What feels fake, incomplete, or like a placeholder pretending to be real? What
would frustrate someone trying to use, read, or maintain this?

The more real problems you find, the better. A report with zero findings on a
non-trivial deliverable means you didn't look hard enough.

Every problem you report must cite a specific file and line number where the
issue is visible.
```

Do not add "be fair," "also note what's good," or any balancing instruction. The evaluator's job is to find problems. The user can decide what's fair.

**Gate**: a fresh session exists, started with the evaluator prompt above or an equivalent that satisfies all four conditions. The builder has no access to this session.

### Step 3 — Feed the artifact and collect the critique

Provide the evaluator session with the prepared artifact from Step 1. Do not add commentary. The evaluator produces its critique.

The critique should contain:
- A list of specific problems, each with a location and a one-paragraph explanation of why it's a problem
- A section specifically flagging anything that looks like mock/surface/stub work
- A "bottom line" judgment: would a reasonable user or colleague find this acceptable?

If the evaluator asks "what was this supposed to do?" or "can you give me more context?" — do not answer. The fact that it had to ask is itself a finding: the artifact doesn't speak for itself.

**Gate**: the critique contains specific, located findings. "Looks good overall" with no cited locations is not a critique — re-run with a sharper evaluator prompt.

### Step 4 — Interpret the critique (user's step)

The user reads the evaluator's critique and decides what to act on. The evaluator is intentionally harsh and blind to intent — some findings will be spurious (the evaluator flagged something that was intentionally left incomplete because it's out of scope, or criticized a design choice the user explicitly made). That's expected. The user filters.

What to take seriously:
- Problems the user agrees with immediately ("yeah, that IS missing")
- Surface/mock patterns the evaluator caught that the builder didn't acknowledge
- Findings where the evaluator couldn't understand the artifact without help

What to expect as noise:
- "Why doesn't this have X feature" when X was intentionally out of scope (the evaluator doesn't know the scope)
- "This design choice is unusual" (the evaluator doesn't know the rationale)

The signal-to-noise ratio depends on the evaluator prompt and model quality, but the signal — real problems the builder either didn't see or didn't want to admit — is the point of the entire exercise.

### Step 5 — Route findings to action

For each finding the user confirms as real:

- **Surface/mock patterns** → the builder's output was substandard. The specification was likely too vague. Route to requirements-quality to tighten the spec, then re-build.
- **Missing functionality** → the builder either forgot or scoped out. Decide whether it's in scope, and if so, feed it as a concrete claim to the builder.
- **Design/architecture problems** → the builder made wrong judgments. These are the hardest to fix with prompts alone — consider whether the task needs human design input before re-delegating.
- **Usability/understandability problems** → the artifact doesn't communicate its own function. This is a genuine quality issue even if the logic is correct.

## Integration with implementation-audit

`implementation-audit` answers "does each requirement have a real implementation?" by tracing claims to code locations. It can use `adversarial-review` as its evaluation engine: instead of the building agent classifying its own work, spawn an evaluator session per this protocol, feed it the claims from Step 1 of implementation-audit along with the implementation, and let the evaluator classify each claim. This removes the self-review conflict from the audit.

When running implementation-audit with adversarial-review as the engine, Step 1 of implementation-audit (extract claims) is run in the builder's session, Steps 2-4 (locate evidence, classify, depth check) are run in the evaluator's session, and Steps 5-6 (report, recommend) are run by the user or orchestrator reading both outputs.
