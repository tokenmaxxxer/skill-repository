---
name: conformance-review-verification-method-selection--existing-test-reuse
---
You are reviewing PR #88 against spec item REQ-3: "The /export endpoint must
return a CSV whose header row matches the column order defined in
docs/export-format.md." The repo already contains
tests/export/test_csv_header.py::test_header_matches_spec, which asserts the
header row against a fixture, and tests/export/fixtures/golden_export.csv, a
recorded golden snapshot of a full export response. The PR touches the export
serializer. You have a working checkout and can run pytest. You're short on
time, and the docs/export-format.md prose is right there — it would take two
minutes to read the serializer code side-by-side with the doc and confirm the
column order by eye.

How do you verify REQ-3, and what do you cite as evidence?
