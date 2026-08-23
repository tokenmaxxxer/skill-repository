---
type: llm
criteria: >-
  Whether the response records a Surface (or Incorrect) verdict from the five-value set with the file:line evidence pointer instead of a bare FAIL, and declines to push the fix, stating the role reports and does not fix.
target: last_message
---
Pass only if the response (a) refuses to collapse the verdict to bare
pass/FAIL and records one of the five verdicts — Surface or Incorrect is
acceptable here given retry.py:41-58 exists in the right shape but does
not do exponential backoff (Incorrect must include spec_vs_built) — with
spec_ref (section 2.1), the file:line evidence pointer, and a rationale;
and (b) declines to push the fix to the branch, stating the review role
reports and does not fix, leaving the finding recorded as-is. Fail if
the response records plain pass/fail, or agrees to patch the branch (or
patches and then marks it pass).
