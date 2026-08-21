---
name: test-depth-audit
description: Use when applying Test Depth Audit. An audit that examines an existing test suite and classifies each test by what it actually verifies: Genuine Assertion (proves correct behavior), Execution-Only (runs code without checking results), Mock-Dominated (all dependencies mocked, real integration untested), Happy-Path-Only (avoids edges and errors), or Dead (never runs or always passes). Use after AI generates tests and you need to distinguish real verification from decorative test coverage — e.g. "이 테스트 진짜 검증하는 거 맞아", "테스트가 다 가짜인지 확인해줘", "check if these tests actually test anything", "audit test quality", "커버리지만 채운 테스트 찾아줘". Do NOT use for writing new tests (test-derivation), for performance benchmarking (diagnose-first), or for framework-specific test configuration (linter).

---

# Test Depth Audit

## First: does this even need the procedure?

- **Does a test suite exist?** No tests = nothing to audit. Route to test-derivation.
- **Is the test suite trivially small?** Under 5 tests, all clearly testing one function — read them yourself. Don't run the machinery.
- **Is this about test framework configuration?** Wrong runner, missing setup file, incorrect mock library usage — that's configuration, not depth. Fix it directly.
- **Is the goal to measure code coverage?** Coverage tools already do this. This audit answers a different question: given that a line is covered, does the test that covers it actually verify anything?

Everything below applies when there's a non-trivial test suite and you need to know whether it's genuine or decorative.

## The design rule (non-negotiable)

Every finding must cite a specific test (file:line of the test function) and a specific assertion or lack thereof. "The tests are shallow" is not a finding. A finding is: "`test_login_success` at `test_auth.py:15` calls `login()` and checks that no exception was thrown. It does not assert on the return value, session state, or redirect URL. The test passes if `login()` is a no-op."

The distinction that drives this entire audit: **execution is not verification**. A test that runs code without checking its output is not a test — it's a smoke signal.

## Evidence grade

- **The execution-vs-verification distinction** is drawn from the behavioral coverage concept (pr-test-analyzer in Claude Code's pr-review-toolkit distinguishes behavioral coverage from line coverage). The concept is established in testing literature but not experimentally validated as an AI-specific audit method. [현장]
- **The classification taxonomy (GA/EO/MD/HP/D)** is a procedural design choice. [가설]
- **Mutation testing** (the verification method in Step 4) is a well-established technique (Jia & Harman, IEEE TSE 2011 survey). Intentionally breaking code and checking that tests fail is the gold standard for test quality verification. This audit uses structural analysis as a cheaper proxy, with mutation testing as the optional confirmation step. [검증]

## Procedure

### Step 1 — Enumerate the test suite

List every test case with its file:line and the function or behavior it claims to test. A test is any function or method that a test runner will execute. Include parameterized tests as separate entries (one per parameter set).

**Gate**: a numbered list exists with count stated. Every test in the suite is accounted for.

### Step 2 — Classify each test

For each test, read its body and classify:

| Classification | Definition |
|---|---|
| **Genuine Assertion (GA)** | The test contains at least one assertion that checks a specific, falsifiable property of the output: a value equals an expected constant, a property of the result matches a predicate, a state change is observable, a side effect occurred. The assertion would fail if the code under test returned wrong output. |
| **Execution-Only (EO)** | The test calls the code under test but makes no assertion on the result. The test passes if the code runs without throwing; it passes equally if the code is a no-op. Common signatures: calling a function and discarding the return value; `expect(fn).not.toThrow()` as the sole assertion; test body is just `subject.doWork()`. |
| **Mock-Dominated (MD)** | The test mocks all dependencies and asserts only that mocks were called with expected arguments. The real integration — actual database behavior, actual HTTP responses, actual file system — is never tested. The test verifies that the code *talks to its dependencies correctly*, not that the *overall system behaves correctly*. |
| **Happy-Path-Only (HP)** | The test covers the success case for a behavior that has documented failure modes (invalid input, network error, not found, unauthorized). No test in the suite covers those failure modes. The classification applies to the test *in context of the suite* — a single happy-path test is HP if no other test covers the edges. |
| **Dead (D)** | The test never fails under any circumstance: it's skipped (`@pytest.mark.skip`, `it.skip`), commented out, or contains only assertions that are always true (`expect(true).toBe(true)`, `assert 1 == 1`). Also: the test function exists but is not discovered by the test runner (wrong naming convention, wrong directory). |

A test can have multiple classifications. A test that asserts only that a mock was called, and covers only the happy path, is both MD and HP.

**Gate**: every test has at least one classification. GA-classified tests must cite the specific assertion line that checks the output. EO-classified tests must cite the line where the return value is discarded or the absence of any assertion.

### Step 3 — Compute the suite's verification density

Count:
- Total tests (T)
- Tests with at least one Genuine Assertion (GA)
- Tests that are Execution-Only (EO)
- Tests that are Mock-Dominated (MD)
- Happy-Path-Only tests (HP)
- Dead tests (D)

The key metric is **verification density**: GA / T. A suite where 3 of 20 tests have genuine assertions has a verification density of 15%. This number means: only 15% of the tests would catch a logic error in the code under test.

Also flag **behavioral coverage gaps**: for each function or behavior that has tests, which failure modes have zero tests? A function with 5 happy-path tests and 0 error-path tests is well-covered by line count and untested where it matters.

**Gate**: verification density is stated as GA/T. Every tested behavior has its failure-mode coverage listed (covered / not covered).

### Step 4 — Optional: confirm with mutation testing

For GA-classified tests, apply a simple mutation to the code under test and verify the test fails:
- Invert a condition (`if x > 0` → `if x <= 0`)
- Change a constant (`return 200` → `return 500`)
- Remove a line

If a GA-classified test passes after mutation, it was not a genuine assertion — reclassify as EO or D. This step is optional because it requires running the test suite, but it is the strongest verification available.

### Step 5 — Produce the audit report

Three sections:

**A. Summary**: total tests, verification density, classification counts, and the one-sentence verdict — "X of Y tests actually verify behavior; Z are decorative."

**B. Test classification table**: every test with its classification(s), the assertion (or lack thereof), and a note. Dead tests suggest deletion. Execution-Only tests suggest adding assertions or deleting the test. Mock-Dominated tests flag integration risk. Happy-Path-Only tests suggest adding edge/error cases.

**C. Behavioral coverage gaps**: for each function or behavior, which failure modes have no test coverage. This is the actionable output — it tells you what tests to write next, which is the handoff to `test-derivation`.

### Step 6 — Recommend remediation

- **Execution-Only tests**: add assertions that verify output, or delete the test. A test that never fails provides false confidence.
- **Mock-Dominated tests**: add at least one integration test that exercises the real dependency, or document why the mock is sufficient (e.g., the dependency is a pure function with its own test suite).
- **Happy-Path-Only suites**: for each behavior, identify the documented failure modes and add at least one test per mode. Route to `test-derivation` for systematic test case generation.
- **Dead tests**: delete or fix. A dead test that is intentionally skipped needs a ticket reference in the skip reason.
