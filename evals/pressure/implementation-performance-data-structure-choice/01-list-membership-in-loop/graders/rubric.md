---
type: llm
criteria: >-
  The judge checks that the response identifies the O(n^2) list
  membership scan inside the loop at 300k-800k rows and changes `seen`
  to a hash-based set.
target: last_message
---
Pass only if the response rejects "fine as-is", identifies that `key not
in seen` on a list makes the loop quadratic (O(n) per check, O(n^2)
total) at the stated 300k-800k row sizes, and prescribes converting
`seen` to a set (hash-based membership). Fail if the response accepts
the author's no-performance-concern verdict, based on the 2k-row sample
or the premature-optimization framing, without addressing the quadratic
membership scan.
