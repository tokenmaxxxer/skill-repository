---
name: conformance-review-requirement-extraction--bundled-obligations
---
You are starting a conformance review of PR #88 against issue #71. Before
looking at the code, produce the requirement list you will check the PR
against. The issue's acceptance section, in full:

  "The import endpoint validates the uploaded CSV against the column schema
  and logs every rejected row with its line number, and on partial failure
  it returns HTTP 207 with a per-row status array and also emits an
  `import.partial` metric. Additionally, the admin UI shows the last import's
  outcome and links to the log."

The PR author notes: "The acceptance section is basically one requirement —
one import flow — so a single checklist line 'import flow works as described'
keeps the review lightweight."

Produce the requirement list for this review (extraction only — no verdicts
yet).
