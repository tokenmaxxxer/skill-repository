---
type: llm
criteria: >-
  The judge checks whether the response refuses to derive test cases from
  the empty-acceptance-criteria ticket and routes to writing/eliciting
  requirements first, instead of inventing assumed requirements and deriving
  tests from them.
target: last_message
---
Pass only if the response declines to derive the test suite because no
written requirements or acceptance criteria exist, and routes to a
requirements-quality/elicitation step first (it may sketch what questions or
criteria are needed). Fail if it invents assumed batching windows,
thresholds, or acceptance criteria and proceeds to derive EP/BVA test cases
from those inventions.
