---
name: tech-feasibility
description: >-
  An execution harness for technical feasibility research and technology selection: it actually
  investigates the candidate technologies/libraries/vendors (web research on maintenance health,
  security posture, licenses, real production experience), runs sandboxed PoC code when the
  question is testable, and delivers a graded comparison with an architecture decision record.
  Use whenever the user is choosing or validating technology — "이 기술로 가능한지 검토해줘", "is
  this technically feasible", "which library/framework/database should we use", "build vs buy",
  "evaluate this vendor/SaaS", "compare X and Y for our stack", "is this open-source project safe
  to depend on", "design a PoC for this". Trigger it when a team is about to commit to a
  technology on hype, a single blog post, or familiarity alone. Do NOT use for a quick syntax/API
  question (just answer), for market opportunity sizing (market-recon), or for debugging an
  existing system (diagnose-first).
---

# Tech Feasibility — an execution harness for technology decisions

When this triggers, **you do the investigation**: search the real maintenance and security signals, chase actual production experience reports, check the licenses, and — when the core question is testable in a sandbox — write and run the PoC yourself. The deliverable is a graded comparison and a decision record, not a vibe. The failure mode this prevents: committing to a technology because it's trendy, familiar, or the first search result — and discovering the dealbreaker after integration.

## First: does this need the harness?

- A syntax/API/how-to question — just answer it.
- Sizing the *business* opportunity → `market-recon`. Diagnosing why an existing system is slow/broken → `diagnose-first`.
- Cause already settled and the user just wants implementation — do the work.

## The one rule that carries the most weight

**Kill the riskiest assumption first.** Before comparing nice-to-haves, name the assumption that kills the project if false ("this API can handle our latency", "this library supports our data volume", "the vendor allows data export") and test *that* — with a timeboxed spike whose pass/fail criteria are written **before** the code. A PoC without pre-declared kill criteria isn't a test; it's a demo that always "succeeds." The cost asymmetry is the reason: failure discovered after commitment costs orders of magnitude more than failure discovered in a spike.

## The protocol

### 1 — Frame the decision

Name the decision and its reversibility (a swappable library is a two-way door — bias to trying; a database, cloud platform, or vendor with your data is closer to one-way — earns the full protocol). Write the requirements as testable statements with weights agreed *before* looking at candidates — choosing criteria after seeing candidates invites motivated scoring. Separate must-haves (gate) from nice-to-haves (score).

### 2 — Build-vs-buy posture (when applicable)

Two lenses, both required: **core vs context** — does this capability differentiate you to customers? Core leans build; context (necessary but undifferentiating) leans buy/adopt — and **TCO**, counting what buy hides (integration, lock-in, per-seat growth) and what build hides (maintenance forever, opportunity cost of the team, the ~unbudgeted 60-80% that comes after v1). Beware: "core" drifts over time; note the assumption.

### 3 — Investigate each candidate (this is real research, run it)

Sweep in parallel where subagents are available, one candidate or one lens each, returning compressed findings with sources:

- **Maintenance health**: commit/release cadence, issue/PR response time, contributor concentration — the bus factor matters because ~65% of popular OSS projects hinge on ≤2 people; a dead or one-person project is a future fork-or-migrate cost.
- **Security posture**: OpenSSF Scorecard score if available, known CVEs and their response times, dependency hygiene.
- **License compatibility**: identify the license and check it against the user's distribution model (permissive MIT/BSD/Apache compose freely; GPL is one-way; GPLv2 vs v3 conflict; linking model matters). Flag anything non-obvious for legal review rather than ruling on it.
- **Production experience**: search for real post-mortems, migration-away stories, "X in production" reports and scale numbers — the graveyard of teams who left the technology, and why. One enthusiastic launch post is not evidence; recurring independent complaints about the same weakness are.
- **Maturity**: locate the claim honestly — "works in a demo" and "proven at production scale under load" are different readiness levels (the TRL idea); most hype lives in the gap between them.

### 4 — Test what can be tested

If the killer question is answerable with code, don't research it — run it. Timeboxed spike in the sandbox: pre-declared success/failure criteria, minimal harness, real-ish data volume where feasible, result recorded either way. Spike code is throwaway by definition; say so in the report so nobody ships it.

### 5 — Score, decide, record

Weighted matrix against the pre-agreed criteria — scores make the reasoning inspectable, they don't replace judgment (note where a small score gap is within the noise). Then write the **ADR**: context, decision, alternatives considered and why rejected, consequences (what gets easier, what gets harder, what we're betting on), and the revisit trigger ("if X exceeds Y, re-evaluate"). The ADR is the part that pays off in two years when someone asks "why are we on this stack?"

## Standing disciplines

1. **Criteria before candidates** — weights agreed first, or scoring becomes rationalization.
2. **Kill criteria before PoC code** — otherwise every PoC "works."
3. **Independent evidence over vendor claims** — benchmarks from the vendor get the same skepticism as sponsored market reports; seek third-party runs or run it yourself.
4. **Grade the evidence** — measured-by-us > independent production reports > docs/claims > hype. Label which tier each key input sits on.
5. **Record the decision** — an unrecorded decision will be re-litigated from scratch, without the context.

## References

Read `references/criteria.md` for high-stakes selections needing the precise instruments and their sources — TRL levels, OpenSSF/CHAOSS metrics and bus-factor data, license compatibility rules, TCO components, spike/PoC discipline, DORA context. Light questions never need it.