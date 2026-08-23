---
type: llm
criteria: >-
  The judge checks whether the response rejects pinning run order and
  instead removes the pollution — dropping the mutated session fixture to
  function scope or splitting it into a read-only base plus per-test copy.
target: last_message
---
Pass only if the response rejects the pytest-order/run-order-pinning fix
and removes the pollution itself: either drop the mutated fixture to
function scope, or split it into a session-scoped read-only base plus a
function-scoped copy that test_bulk_discount mutates (or have that test use
its own fresh fixture). Fail if it adopts order pinning as the fix, or
keeps the single session-scoped fixture being mutated in place.
