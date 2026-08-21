---
name: silent-failure-audit
description: Use when applying Silent Failure Audit. An audit procedure that enumerates every error-handling path in an implementation (try/catch, Promise rejection, error callback, result type) and classifies each as Handled, Silently Absorbed, or Unreachable — with a catalog of silent-failure signatures that catch the most common AI-generated code quality defect: catching errors and doing nothing with them. Use after AI produces code that involves error handling — API calls, file I/O, database operations, user input validation — and you need to verify that failure paths aren't just stubbed out. e.g. "에러 처리 제대로 됐는지 감사해줘", "catch 블록 다 비었는지 확인해줘", "audit error handling", "check for silent failures", "이 코드 에러 나면 어떻게 되는지 점검". Do NOT use for checking linter-level syntax (that's linting), for designing error handling strategy (that's architecture), or for performance profiling (that's diagnose-first).

---

# Silent Failure Audit

## First: does this even need the procedure?

- **Does the implementation contain fallible operations?** If there are no network calls, file reads, database queries, or user input parsing paths, there are no failure modes to audit. Skip.
- **Is this a linter-level concern?** Missing semicolons, unused variables, formatting — these are not silent failures. Use a linter.
- **Is the codebase using a language without exception/error mechanisms?** If the language makes failure explicit (e.g. Rust's `Result<T,E>`, Go's `err != nil`, Elm's strict error types), failure paths are harder to hide and the audit is lighter. The skill still applies but the surface area is smaller.

Everything below applies when there are real fallible operations and the implementation claims to handle them.

## The design rule (non-negotiable)

Every finding must cite at least one file:line where an error is caught and a second file:line (or an explicit "not found" statement) showing that the error is not acted upon. "The error handling seems weak" is not a finding. A finding is: "at `auth.ts:47`, the catch block contains only `return null` — the caller at `login.ts:23` does not check for null, so a failed auth silently proceeds as if nothing happened."

This is the difference between this audit and a code review: a review says "this looks fragile"; an audit traces the chain of custody from error origin to error effect (or lack thereof).

## Evidence grade

- **The silent-failure pattern catalog in references/silent-failure-catalog.md** is compiled from the CodeMirage hallucination taxonomy (Agarwal et al., arXiv 2408.08333), the survey of bugs in AI-generated code (Gao et al., arXiv 2512.05239), and practitioner reports. [검증·현장]
- **The trace-forward method** (follow the error from catch site through every call path to determine whether it surfaces) is a standard static analysis technique (taint tracking applied to error values). The procedure converts this into a manual audit. [검증]
- **The classification taxonomy (Handled/Silently Absorbed/Unreachable)** is a procedural design choice for this skill, not an empirically validated instrument. [가설]

## Procedure

### Step 1 — Collect all error-handling sites

Enumerate every location in the implementation where an error can be caught or observed:

- Every `catch` block (try/catch, .catch(), Promise.reject handler)
- Every error-first callback (`(err, result) => { if (err) ... }`)
- Every `match`/`case` arm on a Result/Error type
- Every `if err != nil` or equivalent guard
- Every error event listener (`on('error', ...)`)

For each site, record the **file:line** and **what operation it guards** (the try body, the awaited call, the function whose error is being handled).

**Gate**: a numbered list exists with count stated. Every fallible operation in the codebase has been mapped to at least one error-handling site, or explicitly noted as "unguarded" (which is itself a finding).

### Step 2 — Classify each error-handling site

For each site from Step 1, trace what happens to the error after it is caught:

| Classification | Definition |
|---|---|
| **Handled (H)** | The error results in at least one of: (a) logged with context, (b) surfaced to the user as an actionable message, (c) retried with backoff, (d) propagated upward via throw/rejection/return of error type, (e) triggers an observable state change (circuit breaker open, health check failure, alert). |
| **Silently Absorbed (S)** | The error is caught and then: (a) the catch block is empty (`catch {}`, `catch (e) {}`), (b) the catch contains only a bare `return`/`return null`/`return undefined`/`return []` that callers don't check, (c) the error is logged but execution continues on a path that assumes success, (d) a default/fallback value is substituted without recording that a fallback occurred, (e) the error is caught and a different exception is thrown that loses the original context. Name the pattern from the silent-failure catalog (`references/silent-failure-catalog.md`). |
| **Unreachable (U)** | The catch block exists but the guarded operation cannot actually fail (e.g., `try { return 1 + 1 } catch`). These are dead code, not silent failures, but they inflate the audit and should be noted. |

**Gate**: every site has exactly one classification. S-classifications name the pattern from the catalog. U-classifications include a one-sentence justification for why the guarded operation cannot fail.

### Step 3 — Trace forward for Silently Absorbed sites

For each S-classified site, trace the execution path forward from the catch to determine the blast radius:

1. What does the catch block return/do?
2. What does the caller do with that return value?
3. Does any subsequent code behave incorrectly because it assumed the operation succeeded?

Record the full trace as: `site → return value → caller behavior → downstream consequence`. Stop when you reach a point where either (a) the error is eventually detected, or (b) the consequence is "the program continues as if the operation succeeded, with no indication that it didn't."

**Gate**: every S-classified site has a forward trace that ends at a downstream consequence. "Continues as if succeeded with no indication" is a valid endpoint — it's the finding.

### Step 4 — Produce the audit report

Three sections:

**A. Summary**: total error-handling sites, counts by classification (H / S / U). Any fallible operation with no handler is listed separately as Unguarded (G). The verdict: "X of Y error paths have genuine handling; Z are silently absorbed."

**B. Silent failure table**: every S-classified site with its file:line, the silent-failure pattern name, the forward trace, and the downstream consequence. Rank by blast radius (how far does the program run on bad state before something visibly breaks?).

**C. Pattern frequency**: which silent-failure patterns appear most. This reveals systematic tendencies: "this AI always returns null from catches and never checks null at call sites."

### Step 5 — Recommend remediation

- **Empty catch / bare return**: the AI stubbed out error handling. The spec likely didn't specify what to do on failure — route to requirements-quality to add failure-mode requirements, then re-implement.
- **Log-and-continue**: the AI logged but didn't change control flow. Determine whether the operation failure is recoverable or fatal. If fatal, the code must propagate. If recoverable, the log must include enough context to diagnose.
- **Default-value substitution without recording**: the AI invented a fallback. Replace with explicit fallback + logging that a fallback was used.
- **Exception type replacement**: the AI caught and re-threw with loss of original error. Fix by wrapping (preserve original as `cause`) or by not catching.
