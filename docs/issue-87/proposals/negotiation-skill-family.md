---
status: proposed
files:
  - docs/issue-87/reports/partnerships-bd/survey.md
  - docs/issue-87/proposals/negotiation-skill-family.md
---

# Negotiation/procurement skill family (phase 1: research + proposal)

Note on survey location (scout-skip-adjacent note, no design decision
left open by this path choice): the current-state survey required by
the survey-before-proposal norm lives at
`docs/issue-87/reports/partnerships-bd/survey.md` (role-scoped per
contract v3 s11/s19), not at the generic
`docs/issue-87/reports/implementation/survey.md` path, since this role
writes only its own record area under
`docs/issue-87/reports/partnerships-bd/` and never another role's
`reports/implementation/` tree (board-gate.sh refuses that write). No
design decision remains open beyond what that survey and this proposal
already resolve (the three-skill split below) — there is nothing a
second survey copy at the implementation path would add.

## Request

Issue #87 (professional-discipline gap #5 of 5, final): research-first,
primary-sourced (Fisher & Ury "Getting to Yes" lineage — BATNA,
interests-vs-positions, objective criteria; ZOPA; vendor-evaluation and
RFP scoring practice) survey of the negotiation/procurement discipline,
then propose a `negotiation-*` skill family of >=3 skills
(`negotiation-batna-and-zopa-preparation`,
`negotiation-interests-vs-positions-framing`,
`negotiation-vendor-evaluation-rfp-scoring`), each with a
condition-matched "Use when" trigger, per-rule `source:` citations, and
resolving `Related-skills` links to `partnerships-bd-*` and
`technical-feasibility-build-vs-buy` where they chain. Phase 1 (survey +
proposal) only; authoring the actual `skills/negotiation-*/SKILL.md`
files is phase 2, gated on approval.

## Constraints

- Every rule proposed below must trace to a primary source with a live
  URL, verified in `survey.md` (issue acceptance criterion).
- >=3 skills, axis-split, no content overlap between them or with the
  existing `partnerships-bd-negotiation-positioning` skill.
- Each skill's `description` must carry a distinct "Use when..."
  trigger.
- `Related-skills` cross-references must resolve to real, existing
  skill directory names.
- `scripts/check_skill_conformance.py` must stay green once phase 2
  authors the actual SKILL.md files.
- Sources must appear in the PR body (issue acceptance criterion).

## Rationale

Two structural alternatives were considered, given what the survey
found.

1. **Extend the existing `partnerships-bd-negotiation-positioning`
   skill with more rules (add interests-vs-positions and vendor/RFP
   scoring as new numbered rules on that same skill) instead of
   authoring a new family.** Rejected: the survey's Angle 2 finding is
   that skill's trigger is scoped to partnership *deal* negotiation
   (pricing, exclusivity, revenue split, governance rights) and its
   "Output shape" is deal-term specific — a procurement negotiation with
   a vendor who is not a BD partner, or an internal resource
   negotiation, never fires that trigger. Folding vendor/RFP scoring
   into a BD-partner-scoped skill would force every partnership
   negotiation to also load vendor-scoring-matrix rules it never needs,
   and would hide the generic BATNA/ZOPA and interests-framing rules
   from any non-BD role (e.g. `technical-feasibility-build-vs-buy`'s own
   procurement/vendor decisions) that has no reason to look inside a
   `partnerships-bd-*` skill. Keeping the new family separate, and
   having `partnerships-bd-negotiation-positioning` chain to it via
   `Related-skills` instead of restating the same BATNA/ZOPA rules,
   matches this repo's converged pattern (confirmed against the
   `content-strategy-*`/`content-design-operational-playbook` split in
   issue #82) of routing shared decision axes to one owning skill rather
   than duplicating them per caller.
2. **One combined `negotiation-preparation-and-scoring` skill covering
   BATNA/ZOPA, interests-framing, and vendor/RFP scoring together, since
   all three fire during "preparing to negotiate."** Rejected: the
   survey's three angles are separable decisions with separable failure
   modes and separable timing. BATNA/ZOPA preparation fails by not
   checking whether a zone of possible agreement exists at all (a
   go/no-go gate, checked once per negotiation before investing further
   effort). Interests-vs-positions framing fails mid-negotiation, when a
   stalled positional exchange needs reframing around underlying
   interests — a task that can recur many times within one negotiation,
   independent of whether a ZOPA exists. Vendor-evaluation/RFP scoring
   fails at a different point in the process entirely (comparing
   competing written proposals against weighted criteria, typically with
   no live counterpart negotiating in real time) and has its own
   distinct failure mode (unweighted or unanchored scoring, criteria
   mixed into requirements) that has nothing to do with BATNA math. A
   negotiation can need ZOPA-checking with no vendor-scoring involved
   (e.g. a bilateral partnership term), or vendor-scoring with no live
   negotiation yet (early RFP-response comparison before any counter-
   offer is made). Collapsing them would break this repo's
   axis-triggered dispatch convention, same as the `content-strategy-*`
   precedent's rejected two-skill merge.

## What will be done

`survey.md` (already written, listed in `files:`) documents the
primary-source findings across all three scouted angles, including the
BATNA/ZOPA overlap with the existing `partnerships-bd-negotiation-
positioning` skill. This proposal specifies the three skills to author
in phase 2.

### Proposed family: `negotiation-*` (3 skills)

**1. `negotiation-batna-and-zopa-preparation`**
(axis: `reservation-point-and-agreement-zone`)

- Use when: preparing for any negotiation (procurement, vendor
  contract, partnership term, internal resource ask) before the first
  substantive session, or when the counterpart's walk-away position
  becomes known or inferable mid-negotiation and the zone of possible
  agreement needs re-checking.
- Core rules (source-cited to PON/Harvard Law School):
  - Write down the concrete best alternative to a negotiated agreement
    before entering any live session, and judge every proposed deal
    against that BATNA, not a target number or the counterpart's
    opening position.
  - Once the counterpart's walk-away position is known or reasonably
    inferable, explicitly estimate whether a zone of possible agreement
    exists between the two reservation points before investing further
    negotiation effort; escalate rather than proceed on momentum if no
    overlap is estimated.
- `Related-skills`: `partnerships-bd-negotiation-positioning` (the
  BD-deal-scoped caller — chains here for the underlying BATNA/ZOPA
  mechanics rather than restating them); `negotiation-interests-vs-
  positions-framing` (once a ZOPA is confirmed to exist, framing the
  substance of the negotiation chains there); `technical-feasibility-
  build-vs-buy` (a build-vs-buy decision that turns into a vendor
  negotiation chains here for BATNA prep before that negotiation
  starts).

**2. `negotiation-interests-vs-positions-framing`**
(axis: `positional-vs-interest-based-framing`)

- Use when a negotiation has stalled into repeated positional
  concessions with no underlying interest identified, when drafting an
  opening proposal that states a position without the interest behind
  it, or when a counterpart's stated position seems irreconcilable with
  your own and neither side has yet asked what interest the position
  protects.
- Core rules (source-cited to Fisher, Ury & Patton / Beyond
  Intractability):
  - Before stating a position, identify and write down the underlying
    interest it is meant to protect; when a proposal is drafted around
    a position with no stated interest, treat that as an incomplete
    preparation, not a finished opening offer.
  - When a negotiation stalls on irreconcilable positions, stop
    trading further concessions on the position itself and instead
    surface each side's underlying interests to search for options that
    satisfy both (the Camp David pattern: positions on territory were
    irreconcilable, but the interests behind them — security,
    sovereignty — were not).
- `Related-skills`: `negotiation-batna-and-zopa-preparation` (interest-
  based reframing only has room to work once a ZOPA is confirmed to
  exist — chains back there first if that has not been checked);
  `partnerships-bd-negotiation-positioning` (its rule 3, "drop
  objective-criteria-free positional bargaining," chains here for the
  interests-identification step it currently treats as a single
  sub-clause rather than a first-class procedure).

**3. `negotiation-vendor-evaluation-rfp-scoring`**
(axis: `weighted-criteria-scoring-integrity`)

- Use when designing an RFP's evaluation-criteria section, scoring
  competing vendor proposals against weighted criteria, or reviewing an
  existing vendor-scoring matrix for a criterion that can single-
  handedly decide the award.
- Core rules (source-cited to Responsive/AutoRFP.ai/Inventive.ai
  practitioner guidance):
  - Assign each evaluation criterion a percentage weight summing to
    100%, and cap any single criterion (commonly 40%) so that no one
    factor — including price — can unilaterally decide the award.
  - Write down what each numeric score point means, with a concrete
    example, before scoring any vendor; an unanchored numeric scale
    (a "3" with no stated meaning) is the named failure mode letting
    evaluator bias substitute for the criterion.
  - Keep the evaluation-criteria section separate from the RFP's
    technical-requirements section, and document the reasoning behind
    each score, so the criteria used to judge is never confused with
    what was merely required, and the award is auditable after the
    fact.
- `Related-skills`: `technical-feasibility-build-vs-buy` (once a
  build-vs-buy analysis resolves toward "buy," the vendor short-list
  routes here for scoring); `negotiation-batna-and-zopa-preparation`
  (once a vendor is selected via scoring, price/term negotiation with
  that vendor chains there); `partnerships-bd-deal-structure-selection`
  (when the "vendor" being scored is actually a candidate partner, the
  deal-vehicle decision chains there after scoring narrows the field).

## Out of scope

- Authoring the actual `skills/negotiation-*/SKILL.md` files (phase 2).
- Rewriting or removing any rule inside
  `skills/partnerships-bd-negotiation-positioning/SKILL.md` — that
  skill keeps its existing BD-deal-scoped rules as-is; only its
  `Related-skills` field gains a phase-2 cross-reference to the new
  family (a non-content, additive change).
- Deal-vehicle selection, exclusivity terms, governance cadence, and
  term-sheet clause conventions — already owned by the other
  `partnerships-bd-*` skills.
- The build-vs-buy decision itself (whether to build or purchase at
  all) — already owned by `technical-feasibility-build-vs-buy`; this
  family only supplies the negotiation/scoring layer once "buy" or
  "negotiate" is already the path.

## How you'll know it worked

- `docs/issue-87/reports/partnerships-bd/survey.md` and this proposal
  exist on disk, phase-1 committed, PR opened against `main`
  referencing `#87` (no Closes/Fixes trailer at this phase).
- On approval (phase 2): three `skills/negotiation-*/SKILL.md` files
  exist, each with a distinct "Use when" trigger, per-rule `source:`
  citations matching this survey, and `Related-skills` links (including
  the additive cross-reference from
  `partnerships-bd-negotiation-positioning`) that resolve to real
  directories; `scripts/check_skill_conformance.py` runs green over the
  full repo.
