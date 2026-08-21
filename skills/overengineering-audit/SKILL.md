---
name: overengineering-audit
description: Use when applying Over-engineering Audit. An audit that scans a completed implementation for code that exceeds the specification: unnecessary abstraction layers, interfaces with one implementation, features not in the requirements, unused dependencies, and scope that grew beyond what was asked. Use after AI produces code and you suspect it built more than necessary — e.g. "이 코드 필요 이상으로 복잡한지 봐줘", "요구사항에 없는 기능 찾아줘", "이거 너무 과하게 만든 거 아니야", "audit for over-engineering", "find unnecessary abstractions", "check if this is more than what was asked". Do NOT use for code style review (linter), for performance optimization (diagnose-first), or for architecture design decisions (tech-feasibility). This audit answers: "what exists in the implementation that the specification didn't ask for?"

---

# Over-engineering Audit

## First: does this even need the procedure?

- **Is there a specification to audit against?** Without a written spec, requirements, or user prompt, there's no baseline to measure excess. Capture the spec first.
- **Is the implementation trivially minimal?** A single function, a config change, a script under 20 lines — the audit machinery costs more than the code. Skip.
- **Is this a prototype or spike where exploration is the goal?** Over-engineering a throwaway spike is expected. Don't audit what's meant to be discarded.
- **Is this about naming or formatting?** Calling a function `processData` instead of `handleData` is a style issue. The audit looks for structural excess — entire files, classes, abstractions that don't serve a requirement.

Everything below applies when there's a real specification and an implementation that might contain more than it asked for.

## The design rule (non-negotiable)

Every finding must trace an implementation artifact to a specification gap — a file:line that exists in the code but has no corresponding requirement, or a file:line that is more complex than its requirement justifies. "This feels over-engineered" is not a finding. A finding is: "`src/cache/CacheManager.ts` implements a pluggable cache backend with LRU eviction; the spec says 'cache API responses.' The built-in HTTP cache header support in the framework already satisfies this with zero additional code."

This audit is the mirror image of `implementation-audit`: that one finds what's missing; this one finds what's extra.

## Evidence grade

- **The YAGNI principle and the over-engineering patterns below** are drawn from Ponytail (DietrichGebert/ponytail, 84.3k★, benchmarked at -54% code) and the "Deep Module" principle from A Philosophy of Software Design (Ousterhout). The patterns are practitioner-validated, not experimentally tested. [현장]
- **The classification taxonomy (Excess/Sufficient/Minimal)** is a procedural design choice. [가설]
- **The scope-expansion detection method** (requirement → artifact mapping, extra-artifact enumeration) is structural by construction. [가설]

## Procedure

### Step 1 — Establish the specification baseline

Extract the set of concrete requirements from the spec, user prompt, or acceptance criteria. Each requirement must be specific enough that you can say "this code artifact exists to satisfy this requirement."

The baseline is a mapping: {requirement} → {expected minimal implementation}. This is subjective at the margins — two reasonable people might disagree on what's "minimal" for a given requirement. Resolve by erring toward the *smaller* scope: if a requirement could be satisfied by one function, treat that as the baseline, and flag anything larger as potential excess.

**Gate**: a numbered list of requirements exists with count stated. Each has an expected-minimal-implementation annotation.

### Step 2 — Map implementation artifacts to requirements

For each file, class, function, interface, or configuration entry in the implementation, identify which requirement from Step 1 it serves. An artifact that serves no requirement is excess. An artifact that serves a requirement but is more complex than the expected-minimal-implementation annotation is potential excess.

**Gate**: every implementation artifact has a requirement assigned or is flagged as "unmapped." A count is stated: "N artifacts mapped, M unmapped."

### Step 3 — Classify each unmapped or oversized artifact

| Classification | Definition |
|---|---|
| **Excess — Unnecessary Abstraction (EA)** | An interface, abstract class, strategy pattern, or plugin system where: (a) there is exactly one concrete implementation, or (b) the call sites are all in a single file. The abstraction adds indirection without enabling variation. |
| **Excess — Speculative Feature (EF)** | Functionality that is not mentioned in any requirement — a feature the AI added because "users might want it" or "this is how these are usually built." |
| **Excess — Unused Artifact (EU)** | A file, class, function, or configuration entry that is not referenced by any other code path that traces to a requirement. Dead code, unused imports, orphaned components. |
| **Excess — Over-configurability (EC)** | A parameter, environment variable, or configuration option that has only one valid value in the current context, or that the spec doesn't require to be configurable. |
| **Excess — Premature Optimization (EO)** | A caching layer, indexing strategy, or algorithmic choice that adds complexity for performance the spec doesn't call for. (Route the performance question to diagnose-first if the spec does call for it.) |
| **Sufficient (S)** | The artifact matches the expected-minimal-implementation for its requirement. |
| **Under-implemented (U)** | The artifact exists but is less than the requirement demands. This is a finding for `implementation-audit`, not this audit — note it and move on. |

**Gate**: every unmapped or oversized artifact has one classification. EA classifications must name the single concrete implementation that makes the abstraction unnecessary.

### Step 4 — Quantify the excess

For each Excess finding, estimate the removal cost (lines/files to delete, call sites to update, tests to adjust) and the maintenance cost if kept (code readers must understand this abstraction before reaching the actual logic, future changes may need to touch this unused layer).

This quantification is a rough order-of-magnitude, not a precise estimate. The point is to distinguish "one extra function, delete in 30 seconds" from "500-line pluggable architecture that every future developer will need to learn."

**Gate**: every Excess finding has a removal-cost range (low/medium/high) and a one-paragraph maintenance-cost explanation.

### Step 5 — Produce the audit report

Three sections:

**A. Summary**: total artifacts, counts by classification (EA / EF / EU / EC / EO / S / U), and estimated lines of removable code.

**B. Excess table**: every Excess-classified artifact with file:line, classification, which requirement it was supposed to serve (or "none"), and the minimal alternative. The minimal alternative is the critical column — it shows what should have been built instead.

**C. Scope creep narrative**: a one-paragraph story of how the implementation grew beyond the spec. "The spec asked for caching; the implementation built a pluggable cache abstraction with LRU eviction and TTL support, of which only the in-memory backend is used. The framework's built-in cache already satisfies the requirement."

### Step 6 — Recommend remediation

- **Unnecessary abstractions** → inline the abstraction. Move the one concrete implementation's code to the call site. Delete the interface/abstract class.
- **Speculative features** → delete the feature. If it's genuinely useful, add it to the spec first, then re-implement as a separate task.
- **Unused artifacts** → delete. If they're genuinely needed by a future task, that task should add them.
- **Over-configurability** → hardcode the only-used value. Add configurability later when a second value is actually needed.
- **Premature optimization** → remove the optimization. If performance becomes a problem, diagnose-first will find the real bottleneck, which is unlikely to be where the AI guessed.
