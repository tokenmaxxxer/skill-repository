---
name: test-authoring-isolation-and-fixture-strategy
description: >-
  Use when deciding how to build or scope a test's fixture, whether tests can safely share
  state, or which test-double kind (real/fake/stub/mock) a dependency should get — factory vs.
  in-line setup, pytest fixture scope, polluter/victim run-order dependencies, and database
  cleanup/rollback strategy. Trigger on requests like "fixture scope 어떻게 잡을까", "these tests fail
  when run in a different order", "mock or fake for the database", "테스트 격리 좀 봐줘". Do NOT use for
  pulling new test cases out of acceptance criteria (use test-derivation).
---

# Operational playbook — isolation & fixture strategy

Condition → choice → source rules for this role's decides: 테스트 코드 자체가
격리성·fixture 전략 면에서 좋은 설계인가. Numbered, one rule per line item.
REMOVAL-category rules are marked `[REMOVAL]`.

## Trigger

Apply this skill when authoring or reviewing test code and the decision
at hand is one of: how to construct a test's fixture — factory/Creation
Method vs. in-line setup, and per-test vs. shared build (rules 1-6);
what scope to give a pytest/xUnit fixture — function vs. module/session,
including a fixture reused by groups needing different scopes (rules
7-10); whether tests are safely independent of each other and of run
order, and how to fix a polluter/victim or shared-state dependency
(rules 11-14); how a database-backed test should isolate and clean up
its data, including when transaction-rollback teardown does not apply
(rules 15-17); or which test-double kind — real, fake, stub, or mock —
a SUT's dependency should get (rules 18-21). Distinct from generic test
coverage or naming-convention concerns, which this skill does not cover.

## Procedure

1. Locate the specific fixture/isolation/double decision facing the test
   under authoring or review — construction, scope, independence,
   database cleanup, or double selection — and route to the matching
   section (A-E) below.
2. For fixture construction (rules 1-6): check for duplicated setup
   across tests or a SUT needing many collaborators (rules 1-2) and
   whether the fixture is expensive-and-read-only vs. cheap-and-mutable
   (rules 3-4); flag Implicit Setup for removal (rule 5); pair any
   persistent fixture with Automated Teardown (rule 6).
3. For pytest/xUnit fixture scope (rules 7-10): default to function
   scope for fast or mutable fixtures (rule 7); widen to module/session
   scope only for expensive, read-only fixtures (rule 8); remove a wide
   scope whose object gets mutated (rule 9); split into separately named
   fixtures rather than force one fixture across mismatched scope needs
   (rule 10).
4. For test isolation/independence (rules 11-14): if pass/fail depends
   on run order, identify the polluter/victim pair and remove the
   pollution rather than pin order (rule 11); remove reliance on a
   state-setter test having already run (rule 12); convert shared
   globals/singletons/paths into per-test fixtures (rule 13); give
   parallel workers their own DB schema/tmp directory rather than a
   shared store (rule 14).
5. For database-backed fixtures (rules 15-17): wrap same-transaction
   tests in rollback-based Automated Teardown (rule 15); remove that
   assumption when the SUT commits via a separate HTTP client/thread
   (rule 16); use explicit cleanup, not DB rollback, for out-of-process
   side effects (rule 17).
6. For test double selection (rules 18-21): prefer the real dependency
   when it is fast and side-effect-free (rule 18); use a Fake over a
   Mock when only end-state matters (rule 19); replace over-specified
   Mocks with Stubs plus state assertions (rule 20); keep a Mock only
   when the interaction/protocol itself is under test (rule 21).
7. Record the chosen fixture/isolation/double approach against the
   condition that triggered it, and check it against `## Conflicts
   noted` if the decision touches both fixture construction and
   test-double selection.

## Output shape

A fixture/isolation/test-double decision keyed to the specific condition
that triggered it (e.g. "expensive read-only dependency → session-scoped
Fake"), citable back to its rule number(s) and source.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — Fixture setup logic duplicated across >=3 test methods in a suite → extract a Creation Method (parameterized factory function), not In-line Setup copy-paste. Source: Mes…
- 1.2 — SUT construction needs >=4 collaborators and most tests only care about 1-2 of them → use a Creation Method with sensible defaults for the rest, not repeated full-argume…
- 1.3 — Fixture is expensive to build (network call, heavy compute) and read-only across the whole suite → Suite Fixture Setup (build once per suite), never per-test rebuild. So…
- 1.4 — Fixture is cheap to build and any test in the suite might mutate it → Fresh Fixture per test, not Suite/Shared Fixture — Meszaros: "in most circumstances a transient fre…
- 1.5 — [REMOVAL] Fixture setup is hidden inside a base TestCase class's `setUp`/constructor with no per-test visibility of what's built (Implicit Setup) and different tests in…
- 1.6 — Persistent Fresh Fixture is unavoidable (DB-backed test) → pair it with Automated Teardown registered at setup time, not manual In-line Teardown at the end of each test…
- 2.7 — Fixture setup is fast (<10ms) and any test might mutate returned state → function scope (pytest default). Source: pytest docs, "How to use fixtures" (https://docs.pytest…
- 2.8 — Fixture setup is expensive (spins a process, loads a large file) AND every consumer only reads it, never mutates it → session or module scope, sized to the widest group…
- 2.9 — [REMOVAL] A session/module-scoped fixture's returned object is mutated by any consuming test → drop the wide scope back to function scope, or split into a session-scoped…
- 2.10 — A fixture is reused with genuinely different scopes needed by different test groups (e.g. one fast unit group wants function scope, one slow integration group wants sess…
- 3.11 — Any test's pass/fail outcome changes depending on which other tests ran before it (run in isolation vs. full suite order) → the suite has an order dependency; identify t…
- 3.12 — [REMOVAL] A test only passes when a specific earlier test (a "state setter") has already run and populated shared state → this is a brittle in the polluter/victim/state-…
- 3.13 — Tests share a global variable, singleton, shared filesystem path, or unscoped module-level cache → isolated tests do not depend on other tests or share mutable state bet…
- 3.14 — Suite is or will be run with parallel workers and multiple tests read/write the same database rows or files → database-related failures are the most common category of p…
- 4.15 — Test touches a relational DB and does not need the data to outlive the test (no async job, no separate HTTP round trip processing the write) → wrap the test in a transac…
- 4.16 — [REMOVAL] `@Transactional`-style rollback is applied to a test that exercises the SUT through a separate HTTP client / another thread or process (e.g. WebTestClient hitt…
- 4.17 — Test verifies an out-of-process side effect (sent email, uploaded file, third-party API call) → do not rely on DB transaction rollback for cleanup of that side effect; u…
- 5.18 — SUT's dependency has no meaningful side effects and a working real implementation is available and fast → prefer the real dependency over any test double. Source: Google…
- 5.19 — Real dependency is slow/flaky/hard to construct but a lightweight working implementation exists or is easy to write (in-memory DB, in-memory queue) → use a Fake, not a M…
- 5.20 — [REMOVAL] A test asserts that a dependency method was called with specific arguments (behavior verification via Mock) where a Stub plus state/return-value assertion woul…
- 5.21 — The test's actual goal is to verify an interaction/protocol contract itself (e.g. "on failure, retry exactly 3 times calling this API") → a Mock with call-count/argument…
- S1 — Conflicts noted → references/rules.md
