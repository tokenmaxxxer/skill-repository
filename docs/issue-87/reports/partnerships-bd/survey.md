# Survey: negotiation/procurement skill family (issue #87)

Scout mode used: parallel WebSearch fan-out, 1 sweep stage (3 concurrent
angles), stopped at judge point 1 — the three angles converged on
distinct, non-overlapping literatures (principled-negotiation theory,
BATNA/ZOPA preparation practice, RFP/vendor-scoring practice) with no
disagreement to reconcile, so a deepening round would not change any
build decision. Wall-clock well under the 3min budget.

## Angle 1 — interests vs. positions (Fisher & Ury, "Getting to Yes")

- Four principles of principled negotiation: separate people from the
  problem; focus on interests, not positions; invent options for mutual
  gain; insist on objective criteria. Developed at the Harvard
  Negotiation Project (Fisher, Ury & Patton), first published 1981.
- Positional bargaining is inefficient, neglects parties' actual
  interests, and encourages stubbornness that harms the relationship —
  the canonical failure mode is negotiators repeating positional
  concessions instead of asking what underlying interest a position is
  protecting.
- Camp David example: Egypt's and Israel's stated positions on Sinai
  territory were irreconcilable on the map; looking to underlying
  interests (Egyptian sovereignty vs. Israeli security) produced a deal
  no map of positions could.

Sources:
- [Getting to Yes — Wikipedia](https://en.wikipedia.org/wiki/Getting_to_Yes)
- [Summary of "Getting to Yes: Negotiating Agreement Without Giving In" — Beyond Intractability](https://www.beyondintractability.org/bksum/fisher-getting)
- [Summary of "Principled Negotiation at Camp David as described in Getting to Yes" — Beyond Intractability](https://www.beyondintractability.org/artsum/fisher-principled)

## Angle 2 — BATNA/ZOPA preparation practice (PON, Harvard Law School)

- BATNA (best alternative to a negotiated agreement) is the standard by
  which any proposed deal should be judged, not a target number or the
  counterpart's opening offer.
- ZOPA (zone of possible agreement) exists only where the two parties'
  reservation points overlap; a documented preparation checklist checks
  for that overlap explicitly rather than assuming it.
- PON's own negotiation-preparation checklist treats BATNA analysis and
  ZOPA estimation as sequenced steps done *before* a live session, not
  discovered live — biggest preparation failure named: negotiators who
  skip this analysis leave value on the table or get taken advantage of.
- Existing skill overlap: `skills/partnerships-bd-negotiation-positioning`
  already encodes BATNA-statement, ZOPA-estimation, and
  drop-positional-bargaining as three numbered rules, sourced to the
  same PON/Beyond Intractability/KARRASS material — but its own trigger
  is scoped to partnership *deal* negotiation (pricing, exclusivity,
  revenue split, governance rights) and its "Output shape" is deal-term
  specific. It does not cover interests-vs-positions framing as its own
  decision axis (interests appear only inside rule 3's "drop positional
  bargaining" as a consequence, not as a first-class preparation step),
  and it has no vendor/RFP scoring content at all.

Sources:
- [What is a BATNA? — PON, Harvard Law School](https://www.pon.harvard.edu/tag/batna/)
- [What is the Zone of Possible Agreement? — PON, Harvard Law School](https://www.pon.harvard.edu/tag/zone-of-possible-agreement/)
- [How to Find the ZOPA in Business Negotiations — PON, Harvard Law School](https://dev.pon.harvard.edu/daily/business-negotiations/how-to-find-the-zopa-in-business-negotiations/)

## Angle 3 — vendor evaluation / RFP scoring practice

- A weighted scoring matrix is the converged practitioner tool: each
  evaluation criterion (technical approach, cost, experience,
  compliance) gets a percentage weight, weights sum to 100%, and no
  single criterion is allowed to dominate (common cap: 40% max on any
  one criterion) so price alone cannot silently decide the award.
- Score definitions must be written down *before* evaluating vendors
  (what a "3" vs. a "5" means on each criterion) — vague numeric scales
  without anchoring examples are the named failure mode, because they
  let evaluator bias substitute for the criterion.
- Evaluation criteria belong in a section separated from the RFP's
  technical requirements themselves; mixing the two confuses vendors
  about what is being scored vs. what is merely required.
- Cross-functional scoring (multiple stakeholders, not one buyer)
  and documenting the reasoning behind each score are both named as
  reducing single-evaluator bias and supporting later audit.

Sources:
- [RFP evaluation criteria: How to score and select the right vendor — Responsive](https://www.responsive.io/blog/rfp-evaluation-criteria)
- [RFP Scoring Matrix — AutoRFP.ai](https://autorfp.ai/glossary/rfp-scoring-matrix)
- [RFP Evaluation Criteria: Guide with Examples and Scoring Best Practices — Inventive.ai](https://www.inventive.ai/blog-posts/rfp-evaluation-criteria-examples)

## Gap line

The repo already has BATNA/ZOPA and drop-positional-bargaining rules,
but only inside `partnerships-bd-negotiation-positioning`, gated behind
a BD-deal-specific trigger. Missing entirely: (1) a BATNA/ZOPA skill
usable by *any* negotiation context (procurement, vendor contracts,
internal resource asks), not just BD partner deals; (2)
interests-vs-positions framing as its own first-class decision axis,
distinct from the BATNA/ZOPA reservation-point math; (3) any vendor-
evaluation/RFP-scoring skill at all — nothing in the repo currently
covers weighted-criteria vendor scoring, and `technical-feasibility-
build-vs-buy` covers *whether* to buy but not *how to score competing
vendor proposals* once buying is chosen.

## Write-surface implication for the proposal

Given the overlap found in Angle 2, the proposal below must decide how
the new family relates to the existing
`partnerships-bd-negotiation-positioning` skill rather than silently
duplicating its BATNA/ZOPA rules — see the Rationale section of
`docs/issue-87/proposals/negotiation-skill-family.md`.
