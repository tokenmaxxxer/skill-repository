---
name: technical-feasibility-build-vs-buy
description: Use when the feasibility role's `probing` state reaches the prior-art probe and needs a build-vs-buy comparison with per-dependency health scores before that probe can resolve.
---

# Build vs buy

**Belongs to state:** `probing`, prior-art probe.

## Trigger

This probe applies when the feasibility role is in the `probing` state and
has reached the prior-art probe specifically — i.e. the open question is
whether the specification already exists as prior art (product, library, or
patented approach), distinguishing it from sibling probes in `probing` that
ask about other kinds of feasibility risk rather than build-vs-buy choices.

## Procedure

1. Ask the user, one question at a time, whether prior art exists and, only
   if a genuine build-vs-buy choice is live, which alternatives to compare
   (see ## What it asks the user for).
2. Record the results in `feasibility-record.md`'s prior-art probe field,
   pointing to or inlining a project-local artifact such as
   `feasibility/build-vs-buy.md`; note that this write is not itself gated
   (see ## Artifact).
3. Populate the build-vs-buy comparison table (one row per candidate) and
   attach a per-dependency health score for each open-source dependency
   pulled in, flagging that the score reflects process hygiene rather than
   code quality or vulnerability absence (see ## Field list).
4. Classify each option's reversibility using `reversibility-tag`, treating
   buy as typically two-way-door and in-house build on a core dependency as
   typically one-way-door, and scale the evidence bar for resolving the
   probe accordingly (see ## Reversibility note).
5. Confirm the probe only resolves once the comparison table (or an
   explicit "no prior art of note" finding) is recorded, with health scores
   attached wherever dependencies are named (see ## Resolution rule).

## Output shape

Applying this skill produces an updated prior-art probe field in
`feasibility-record.md` pointing to a build-vs-buy comparison table (option,
cost/TCO, lock-in/maintenance risk, differentiator status, reversibility
tag) plus per-dependency health scores, written to the project-local
artifact referenced there (e.g. `feasibility/build-vs-buy.md`).

## What it asks the user for

Ask the user: does this specification already exist as prior art (an
existing product, library, or patented approach), and if a build-or-buy
choice is live, what alternatives should be compared? Ask one question at a
time: first whether prior art exists at all, then — only if a genuine
build-vs-buy choice is on the table — for the candidate alternatives to
compare.

## Artifact

Writes to `feasibility-record.md`'s prior-art probe field (a pointer to, or
inline table within, a project-local file, e.g.
`feasibility/build-vs-buy.md`). This artifact write is not gated — only the
state file's `status` transition is gated.

## Field list

- **Build-vs-buy comparison table**, one row per candidate: option (build /
  buy — named vendor or package), cost/TCO estimate, vendor-lock-in or
  maintenance-burden risk, and whether the capability is a competitive
  differentiator.
- **Per-dependency health score** — for each open-source dependency the
  specification would pull in, an attached health score (OpenSSF Scorecard
  or equivalent aggregated 0-10 score). Note plainly that this score
  measures process hygiene (branch protection, dependency pinning, CI
  checks), not code quality or absence of vulnerabilities.

## Reversibility note

Buying is usually the two-way door (a contract can be cancelled); building
in-house on a core architectural dependency is usually the one-way door
(migrating off it later is expensive). Record this classification per
option in the comparison table using `reversibility-tag`, and scale the
evidence required for the prior-art probe to resolve `pass` accordingly —
a one-way-door build decision needs more than a two-way-door buy decision.

## Resolution rule

The prior-art probe does not resolve until the comparison table (or an
explicit "no prior art of note" finding) and, where dependencies are named,
their health scores are recorded.
