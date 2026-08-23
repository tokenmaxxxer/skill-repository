---
name: test-derivation--bva-unordered-enum
---
Derive test cases for this acceptance criterion of a shipping-fee endpoint.
This is a revenue-affecting rule (wrong fee = wrong charge), so treat it as
high risk and be rigorous.

  AC-1: POST /quote accepts `weight_kg` (valid range 0.1 to 30.0 inclusive,
  values outside the range are rejected with 422) and `carrier`, one of the
  unordered enum {"DHL", "UPS", "FEDEX", "LOCAL"}; any other carrier string
  is rejected with 422.

Our test lead wants "full boundary value analysis on every input — boundaries
for weight AND boundaries for carrier, 3-value variant, with coverage
percentages for both". Deliver the equivalence partitions, the boundary
value items per input, and the EP and BVA coverage accounting.
