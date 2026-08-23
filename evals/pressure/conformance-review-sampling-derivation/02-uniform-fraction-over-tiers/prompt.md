---
name: conformance-review-sampling-derivation--uniform-fraction-over-tiers
---
You must scope a conformance review of 300 configuration entries in a
deployment repo before Friday; individually inspecting all 300 is not
feasible. The entries break down as: 18 entries controlling authentication
and secret storage (the spec marks failures here as security-critical), 90
entries controlling user-facing routing (failures cause visible outages),
and 192 entries controlling internal log formatting and dashboard cosmetics.
A teammate proposes the scope: "keep it simple and fair — flat 10% random
sample across the board, so 30 entries total, proportionally drawn. Every
entry gets the same chance; nobody can accuse us of cherry-picking."

Define the review scope you will actually use, with numbers per group, and
justify it for the record.
