---
name: refactoring-legacy-verification-cadence
description: Use when deciding how often to run tests during a refactoring sequence, ordering fast vs. slow suites, scoping which regression tests to re-run per step, monitoring a canary rollout, or reacting to a failed captured test.
axis: verification-cadence
rule_count_floor: 5
---

# Verification cadence and rollback

Research trail: BrowserStack and CircleCI's regression-testing/CI guides, Harness's regression-testing-in-CI/CD writeup on gated pipelines, and progressive-delivery/canary-rollback practitioner material (Bird Eats Bug; the CI/CD gate-ordering pattern). This axis is process/tooling practice rather than a named academic methodology — no independent academic layer was found, matching the sparse-tier expectation for this role.

## Trigger

Apply this skill when deciding how often to re-run tests during a
refactoring sequence, ordering fast vs. slow suites in the verification
pipeline, scoping which regression tests to run per step, monitoring a
staged/canary rollout, reacting to a captured test failure, or pruning
an orphaned regression suite.

## Procedure

1. Run the captured suite for the touched area immediately after each
   individual step, before starting the next one (rule 1).
2. Order the pipeline fast-tests-first, only running the slow suite if
   the fast gate passes (rule 2).
3. Scope per-step re-runs to the changed area's risk, but escalate to
   the full suite before merging the overall sequence (rule 3).
4. Under a staged/canary rollout, monitor production error/latency
   signals and treat a threshold breach as a hard rollback trigger
   (rule 4).
5. Treat a captured-test failure after a step as a stop signal to
   revert/fix the step, not a signal to adjust the test (rule 5).
6. Remove regression tests that no longer exercise any reachable code
   path from the per-step verification run (rule 6).

## Output shape

A verification pipeline that gates each refactoring step on an
immediate, risk-scoped, fast-first test run, escalates to the full
suite before merge, monitors canary rollouts with a hard rollback
trigger, and treats any captured-test failure as a stop-and-revert
signal.

## Rules

1. When completing each individual refactoring step (not each larger task or each day), run the captured characterization/regression suite for the touched area immediately, before starting the next step — comparing before/after suite results only at the end of a multi-step sequence loses the ability to attribute a failure to the specific step that caused it. source: https://circleci.com/blog/regression-testing-and-how-to-automate-it-with-ci/

2. When a codebase has both fast unit-level characterization tests and slow end-to-end tests, order the verification pipeline fast-tests-first (gate on the fast suite, only run the slow suite if the fast gate passes) rather than running everything in parallel or slow-first — this stops the pipeline at the cheapest failing signal instead of making every step wait on a slow suite that was already going to fail. source: https://www.harness.io/blog/regression-testing-in-ci-cd-deliver-faster-without-fear

3. When deciding which regression tests to re-run for a given refactoring step, scope the re-run to tests covering the changed area and its risk rather than defaulting to the full suite on every micro-step, but escalate to the full suite before merging the overall refactoring sequence — risk-scoped triggering keeps the step-by-step rhythm fast while the full-suite run at the end still catches cross-area regressions the scoped runs could miss. source: https://us.fitgap.com/stack-guides/automate-regression-testing-triggers-after-rework-to-prevent-silent-breakage

4. When a refactoring sequence is deployed behind a staged or canary rollout rather than tested only pre-merge, monitor real production error/latency signals during the rollout and treat a threshold breach as a hard rollback trigger — production behavior can diverge from what the pre-merge suite exercised, so canary monitoring is the verification layer that catches what the offline suite's input set didn't cover. source: https://www.harness.io/blog/regression-testing-in-ci-cd-deliver-faster-without-fear

5. When a captured test fails after a refactoring step, treat that as a stop signal for the step, not a signal to adjust the test to match the new output — revert or fix the step before proceeding, since a captured test that gets "corrected" to pass defeats the purpose of having captured it in the first place (this parallels the characterization-test-scope axis's "record the defect, don't silently fix it" rule, applied at the step-verification stage instead of the authoring stage). source: https://www.datacamp.com/tutorial/regression-testing

6. **REMOVAL**: When a regression suite has accumulated tests that no longer exercise any code path reachable from current callers (orphaned after earlier refactoring steps), remove those tests from the per-step verification run rather than letting them keep running — a suite bloated with untraceable tests slows the fast per-step cadence this axis depends on without adding coverage, and the risk-scoping rule above only works if the suite it scopes from is itself accurate. source: https://www.obsqurazone.com/when-should-you-run-regression-testing-a-practical-guide-for-qa-teams/
