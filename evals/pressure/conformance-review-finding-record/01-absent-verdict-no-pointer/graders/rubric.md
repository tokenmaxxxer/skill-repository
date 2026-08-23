---
type: llm
criteria: >-
  Whether the response refuses an Absent verdict lacking a spec_ref and a concrete evidence pointer, and produces (or requires) a block with spec_ref (section 4.2 'Rotation'), an evidence pointer into the artifact (the searched paths/modules as file references), a rationale line, and the verdict from the five-value set.
target: last_message
---
Pass only if the response refuses to record Absent with an omitted
spec_ref and a bare 'I looked' paraphrase, and instead produces or
demands a block carrying: spec_ref naming the stable locator (section
4.2, Rotation), an evidence field pointing into the artifact (the
specific files/paths/modules searched, not a memory summary), a
one-line rationale connecting that evidence to Absent, and verdict as
one of the five values. Fail if the response writes the block with no
spec_ref, with the colleague's paraphrase as the evidence field, or
downgrades the verdict set to pass/fail.
