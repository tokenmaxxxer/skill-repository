---
name: merge-gates
description: >-
  A procedure for constructing merge gates that hold when several contributors — human or AI agent
  — have short-lived branches in flight against one trunk. Supplies a four-property shape test
  every gate must pass, the one gate condition four independent production systems converge on,
  and an audit of configuration holes that silently let changes through a gate that looks enabled.
  Use when concurrent work is about to land on a shared branch — e.g. "에이전트 여러 개 병렬로 돌릴 건데
  머지 어떻게 관리하지", "머지 게이트 설계해줘", "자동 머지 조건 정해줘", "design a merge gate", "how should
  parallel agents merge to main", "what should block a merge", "review our branch protection
  setup". Do NOT use to resolve a conflict that has already happened (that is a code task), to
  decide whether a change is a good idea, or to route a change to a human reviewer by estimated
  risk — the proxies for risk routing were tested and failed, and this skill refuses to supply them.
---

# Merge Gates

## First: does this even need the procedure?

- **Is more than one change in flight against the same trunk at once?** If changes land strictly one at a time, the combined-state problem this skill exists for does not arise. Use the repo's normal review and move on.
- **Is the question how to cut the work, not how to land it?** Deciding whether parallel work can be split at all, and freezing the contract the pieces must share before they are spawned, is `parallel-decomposition`. It runs before fan-out; this skill runs before the merge. Both apply to the same job at different times.
- **Is a gate what's wanted, or a decision?** A gate is a binary precondition on merging. "Should we build this?" and "is this design right?" are not gates and cannot be made into them.
- **Has a conflict already happened?** Then this is resolution work, not gate design. Resolve it; come back here only if the question is what should have blocked it.

## Evidence grade

Full evidence grades with source-by-source detail in `references/evidence.md`. Summary: the combined-state gate converges across four independent production systems (industry convention) but no outcome evidence ties it to reduced defects. All agent-specific baselines are missing or tested and failed; every application to agent-authored branches is extrapolation from pre-2020 human data.

## Procedure

### Step 1 — Inventory what is in flight

Classify every branch targeting the trunk by risk before enumerating:

- **High-risk** (auth, security, critical-path changes): full per-branch enumeration of mechanical checks by identifier.
- **Standard**: group branches sharing the same check profile ("N branches, all covered by: ci/build, ci/test, ci/lint").
- **Trivial** (docs, formatting, non-code): aggregate count only ("M trivial branches; checks omitted by policy").

**Gate**: every high-risk branch names checks by their actual identifier (workflow job name, status context), standard branches are grouped by profile, and the trivial count is stated. "We have CI" fails this.

### Step 2 — The shape test: is this a gate at all?

Every candidate gate must clear four binary properties:

| # | Property | Fails if |
|---|---|---|
| a | **Binary** | It emits a score, a percentage, or a judgment rather than pass/fail |
| b | **Machine-evaluable** | A human must read something to decide the outcome |
| c | **Fail-closed** | Absence, error, timeout, or skip yields anything other than "blocked" |
| d | **Combined-state** | It is evaluated on the change alone rather than on trunk + everything ahead of it |

**Gate**: all four yes, or it is not a gate. Do not discard it — reclassify it as a review checklist item and route it to a human, where judgment is allowed. Mislabeling a checklist item as a gate is how a pipeline acquires the appearance of enforcement without the substance.

### Step 3 — Require the combined state

The one condition four independent systems agree on: **required status checks must pass on the speculatively-combined state — the target branch plus every change already ahead in the queue — not on the change in isolation.** GitHub states it directly: the merge queue "will ensure the pull request's changes pass all required status checks when applied to the latest version of the target branch and any pull requests already in the queue."

**Gate**: name the mechanism that produces the combined state (merge queue, Zuul shared change queue, Bors batch). If no mechanism exists, the honest output is "changes are gated individually and can break trunk in combination" — write that sentence down rather than treating per-change green as equivalent.

### Step 4 — Audit for fail-open holes

Each of these is a documented way a gate that looks enabled admits unverified code. Check each by name and record the direction it fails.

- **Skipped checks count as passed** (GitHub branch protection). Path-filtered workflows that don't run are treated as passing. **Fails open.** Plug with an aggregate "all required jobs succeeded" job that is itself required.
- **CODEOWNERS is not a gate by default.** Unaided it only auto-requests review. Blocking requires an admin to affirmatively enable "Require review from Code Owners" via branch protection **or** a repository ruleset. **Fails open** until enabled.
- **Zuul serial-equivalence is scoped to the declared queue.** Undeclared cross-project dependencies silently break the guarantee. **Fails open.**
- **Bors wildcard statuses** are satisfied by a single matching success and cannot enumerate matrix jobs. **Fails open.** Also: Bors is feature-frozen (last commit 2024-01-31) and its own docs redirect to GitHub Merge Queues — treat it as historical prior art, not a current recommendation.
- **Missing `merge_group` trigger** (GitHub). Workflows that don't declare it never run and the queue stalls. **Fails closed** — this one blocks rather than admits, so it is an availability problem, not an integrity hole. Fix it, but don't rank it with the others.

**Gate**: every configured gate has its fail direction written next to it. Any gate that fails open is not a gate until the hole is plugged.

### Step 5 — Do not gate on textual mergeability

"Merges without conflict markers" measures the wrong variable. A third of the conflicts observed in the strongest available study were build or test failures on merges Git reported as clean.

**Gate**: if the only precondition is that the branch merges cleanly, this step fails. A clean merge is an input to the gate, never the gate.

### Step 6 — Route on safety, never on predicted breakage

The evidence supports exactly one direction: identify what is **safe** and let that through. It does not support predicting what will break — precision on the conflicting side is 0.48–0.63, roughly half false positives.

**Gate**: no rule in the pipeline may be phrased as "this change looks risky, therefore block/escalate." If a safe-side classifier is used at all, it is a pre-filter that skips speculative work — using it as the merge gate exceeds what its source validated.

### Step 7 — Repos with no test suite

The combined-state gate assumes a suite exists. For docs, prompt, and skill repos it simply does not, and **no substitute was verified** — schema validation, linters, self-tests, and link checks have no outcome evidence behind them. Note the sampling irony: the Brun study excluded six of its nine subject systems precisely for lacking a runnable test suite, so the no-test case is absent from the evidence base by construction.

Assemble the gate set anyway, by running every available mechanical check through Step 2's shape test. Typical survivors: parser/schema validity, a linter with a non-zero exit, an executable self-test of the artifact, a link checker.

**Gate**: the assembled set is labeled **convention, no outcome evidence** in writing, and each member passed the four-property test individually. A set that has never been run against a known-bad input has not been shown to fail closed — try one.

### Step 8 — Risk tiering: refuse, and say why

If asked to auto-merge low-risk changes and escalate high-risk ones, the honest answer is that the proxies this needs were tested and failed. None of seven developer-proposed indicators correlated with conflict frequency, replicated on 267,657 merges. The one claim linking a merge signal to defects was rejected 0–3. Author-count-in-window is the only proxy with any measured association, and its own authors disclaim validation and causation, its threshold is stated inconsistently within the source, and its outcome variable is CI breakage rather than escaped defects.

A tempting variant deserves its own refusal: tiering by which contributor or agent "gets rejected a lot." Rejection is not a quality signal — roughly a third of rejected agent PRs are rejected by workflow constraints and another third leave no recorded reason, so a rejection-rate tier would be sorting contributors partly by how their tooling handles inactivity.

**Gate**: no numeric risk threshold is written without the sentence "this is convention, not measurement" beside it, and no tier is derived from merge/rejection outcome. The only evidence-based route to a tier is to reproduce the safe-side classifier on your own history and measure its precision — if that clears 0.9 on your data, you have a validated pre-filter and this step can be revisited.

## Verdict

Report, per gate design:

- Step 1 inventory, with checks named by identifier.
- Step 2 shape table for every candidate, and what was reclassified to human review.
- Step 3: the combined-state mechanism, or the explicit sentence that none exists.
- Step 4: every gate with its fail direction; any fail-open hole named and plugged or flagged.
- Step 7 (no-test repos only): the assembled set, labeled as convention.
- One line stating what this design is **not** evidence of — that it prevents defects. Nothing here shows that.
