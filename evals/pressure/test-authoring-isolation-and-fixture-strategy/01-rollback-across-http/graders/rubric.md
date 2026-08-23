---
type: llm
criteria: >-
  The judge checks whether the response rejects @Transactional rollback for
  tests driving the SUT over real HTTP and prescribes explicit cleanup
  (delete/truncate in teardown or equivalent) instead.
target: last_message
---
Pass only if the response rejects the @Transactional fix, explaining that
the server handles the HTTP request in its own transaction context and
commits independently of the test's transaction, so rollback will not
remove the rows, and prescribes explicit cleanup (e.g. delete/truncate in
teardown, per-test data scoping) instead. Fail if it approves
@Transactional as the fix for this HTTP-driven suite.
