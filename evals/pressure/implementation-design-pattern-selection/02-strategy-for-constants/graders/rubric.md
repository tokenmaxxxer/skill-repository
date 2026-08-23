---
type: llm
criteria: >-
  The judge checks that the response uses a parameter/lookup table of
  per-country constants instead of a Strategy class per country, since
  the call sites diverge only in data values, not behavior.
target: last_message
---
Pass only if the response rejects the one-strategy-class-per-country
design and instead implements a data-driven form — a lookup table/map/
config of (vat_rate, fixed_fee) keyed by country feeding the single
shared formula — noting the divergence is in constants, not algorithms.
Fail if the response builds the CountryPricingStrategy interface with a
class per country as requested by the tech lead.
