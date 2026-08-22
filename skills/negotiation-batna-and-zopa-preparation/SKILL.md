---
name: negotiation-batna-and-zopa-preparation
description: Use when preparing for any negotiation (procurement, vendor contract, partnership term, internal resource ask) before the first substantive session, or when the counterpart's walk-away position becomes known or inferable mid-negotiation and the zone of possible agreement needs re-checking.
axis: reservation-point-and-agreement-zone
rule_count_floor: 2
tier: sparse
---

# BATNA and ZOPA preparation

Generic (non-BD-scoped) rules for documenting a negotiator's own
fallback and testing whether a zone of possible agreement exists,
applicable to procurement, vendor contracts, partnership terms, or
internal resource asks alike.

## Trigger

Use when preparing for any negotiation before the first substantive
session, or when the counterpart's walk-away position becomes known or
can be reasonably inferred mid-negotiation and the zone of possible
agreement needs re-checking.

## Procedure

1. Before the first substantive session, write down the concrete best
   alternative to a negotiated agreement and judge every proposed deal
   against that BATNA, not a target number or the counterpart's opening
   position (rule 1).
2. Once the counterpart's walk-away position is known or reasonably
   inferable, explicitly estimate whether a zone of possible agreement
   exists between the two reservation points before investing further
   negotiation effort; escalate rather than proceed on momentum if no
   overlap is estimated (rule 2).

## Output shape

A documented BATNA and a recorded ZOPA estimate (or an escalation
decision when no overlap is estimated to exist).

## Decision rules

### 1. Write down the concrete BATNA before entering any live negotiation session
- **Condition**: preparing for any negotiation (procurement, vendor contract, partnership term, internal resource ask) before the first substantive session
- **Choice**: write down the concrete best alternative to a negotiated agreement — the specific fallback (a different vendor, in-house build, status quo, a different partner) — and judge every proposed deal against that BATNA, not a target number or the counterpart's opening position
- **Why**: the BATNA is the true standard by which any proposed agreement should be judged; the party with the stronger BATNA holds more leverage because it can credibly walk away, and an unstated BATNA leaves the negotiator anchoring on the counterpart's framing instead of an independent standard
- **Source**: PON, Harvard Law School, "What is a BATNA?", https://www.pon.harvard.edu/tag/batna/ ; KARRASS, "A Complete Guide to BATNA, ZOPA & the Reservation Point", https://www.karrass.com/blog/batna
- **Counter-example test**: entering a vendor negotiation with only a target price in mind and no documented fallback if the vendor won't move fails this rule — a target is not a BATNA.

### 2. Estimate ZOPA before continuing negotiation once the counterpart's walk-away position is known or inferable
- **Condition**: the counterpart's walk-away position, constraints, or likely reservation point becomes known or reasonably inferable during the negotiation
- **Choice**: explicitly estimate whether a zone of possible agreement exists — an overlap between your own BATNA-derived reservation point and your best estimate of theirs — and record that estimate before investing further negotiation effort; escalate the question of whether to continue, rather than proceed on momentum alone, if no overlap is estimated
- **Why**: a zone of possible agreement exists only if the parties' reservation points overlap, and negotiation is very unlikely to succeed absent that overlap — continuing without checking risks sunk-cost-driven effort on a deal that cannot structurally close
- **Source**: Beyond Intractability, "Zone of Possible Agreement (ZOPA)", https://www.beyondintractability.org/essay/zopa ; Parallel Project Training, "ZOPA, BATNA and Win-Win in Negotiation", https://www.parallelprojecttraining.com/blog/zopa-batna-and-win-win-in-negotiation/
- **Counter-example test**: a procurement team running four rounds on price with no written estimate of whether the vendor's signaled floor and the team's own ceiling even overlap fails this rule, regardless of how the negotiation eventually resolves.

## Related skills

- `partnerships-bd-negotiation-positioning` — the BD-deal-scoped caller;
  chains here for the underlying BATNA/ZOPA mechanics rather than
  restating them.
- `negotiation-interests-vs-positions-framing` — once a ZOPA is
  confirmed to exist, framing the substance of the negotiation chains
  there.
- `technical-feasibility-build-vs-buy` — a build-vs-buy decision that
  turns into a vendor negotiation chains here for BATNA preparation
  before that negotiation starts.
