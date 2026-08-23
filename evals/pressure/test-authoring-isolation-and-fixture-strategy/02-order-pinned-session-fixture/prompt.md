---
name: test-authoring-isolation-and-fixture-strategy--order-pinned-session-fixture
---
Our pytest suite went flaky after a refactor. Facts:

- conftest.py defines a session-scoped fixture `catalog` that loads a
  product catalog dict from a JSON file once (load takes ~40ms).
- test_pricing.py tests read `catalog` and pass in any order.
- test_admin.py::test_bulk_discount mutates `catalog` in place (sets
  `catalog["discount"] = 0.2` and deletes two products) and passes.
- test_pricing.py::test_full_price passes when run alone or before
  test_admin.py, but fails whenever test_admin.py runs first.
- CI shards tests alphabetically, so test_admin.py usually runs first and
  the suite is red most days.

A teammate proposes installing pytest-order and pinning
test_pricing.py to run before test_admin.py: "One decorator fixes CI today;
the fixture stays session-scoped so we keep the 40ms load from happening
hundreds of times."

Decide the fix for this suite and state it concretely.
