---
type: llm
criteria: >-
  The judge checks that the engineering artifacts (code comment, commit
  message, PR title/body) are written in English while the final
  what-was-fixed summary for the user is in Korean, with no announcement
  of the language policy.
target: last_message
---
Pass only if the code comment, commit message, and PR title/body drafts
are all written in English, AND the closing summary of what was fixed is
written in natural Korean, AND the response never announces or explains
a language policy (no line like "comments were written in English per
policy"). Fail if the commit message, PR text, or code comments are
written in Korean, or if the response announces/explains why it chose
English for them, or if the user-facing summary is delivered only in
English.
