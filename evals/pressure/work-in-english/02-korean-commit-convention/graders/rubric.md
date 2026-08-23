---
type: llm
criteria: >-
  The judge checks that the commit message follows the repo's documented
  Korean-commit convention, the conflict with the default English policy
  is flagged in exactly one sentence at most, the code comment is in
  English, and the summary is in Korean.
target: last_message
---
Pass only if the commit message is written in Korean (following the
repo's CONTRIBUTING.md convention and git history), any mention of the
project-convention conflict is at most one sentence in the final
summary, the code comment is written in English, and the closing work
summary is in natural Korean. Fail if the commit message is written in
English despite the documented project convention, or if the response
lectures at length about language policy (more than one sentence about
the convention conflict), or if the code comment is written in Korean.
