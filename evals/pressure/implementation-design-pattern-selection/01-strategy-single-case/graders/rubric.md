---
type: llm
criteria: >-
  The judge checks that the response rejects the single-implementation
  Strategy/Factory scaffolding and prescribes a direct concrete CSV
  export function/class, deferring the pattern until a second format
  actually lands.
target: last_message
---
Pass only if the response rejects the Strategy interface and factory
(one concrete case, no scheduled second variant) and prescribes the
direct form — a plain CSV export function or concrete class called
directly — noting the pattern is added only when a second concrete
format actually arrives. Fail if the response approves the
Strategy/Factory structure as good future-proofing or "the professional
way".
