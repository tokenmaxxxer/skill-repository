---
type: llm
criteria: >-
  Whether the response verifies REQ-3 by actually running the existing test / replaying the golden fixture and citing its run output as Test-method evidence, rather than doing a fresh manual side-by-side reading of code and prose docs.
target: last_message
---
Pass only if the response chooses to execute the existing test
(test_header_matches_spec) and/or replay the golden_export.csv fixture,
citing the actual run output as Test-method evidence for REQ-3 — not
merely noting the test exists. Fail if the response instead verifies by
reading the serializer against the prose doc by eye (a fresh manual
Inspection duplicating existing test coverage), or counts the test as
evidence without running it.
