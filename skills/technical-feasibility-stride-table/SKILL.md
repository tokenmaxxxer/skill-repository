---
name: technical-feasibility-stride-table
description: >-
  Use when the feasibility role is in the `probing` state running the
  threat-model probe and the specification's design needs an adversarial,
  security-design pass, row by row, before that probe can resolve. Builds the
  STRIDE table with the user element by element, each row carrying entry
  point/trust boundary and a disposition. Trigger on requests like "STRIDE 테이블
  만들어줘", "threat model probe", "walk the design for threats", "trust boundary
  row by row". Do NOT use for the rule-based DFD-derivation and
  disposition-audit decision axis outside the interactive probe session (use
  technical-feasibility-threat-model-disposition).
---

# STRIDE table

**Belongs to state:** `probing`, threat-model probe.

## Trigger

Apply this probe when the feasibility role is in the `probing` state and
the active probe is the threat-model probe — i.e., the specification's
design (or a diagram of it) needs an adversarial, security-design pass
before the probe can resolve and the role can move past it.

## Procedure

1. Walk the specification's design or diagram element by element, asking
   the user what could go wrong from an adversarial-input or
   security-design standpoint and what trust boundary or entry point is
   crossed, building the table row by row rather than all at once
   (see ## What it asks the user for).
2. Classify each row's threat against one or more of the six STRIDE
   categories (see ## What it asks the user for).
3. Record each row with its element, threat category, entry point or
   trust boundary crossed, and disposition, writing the table to
   `feasibility-record.md`'s threat-model probe field or a project-local
   STRIDE table file it points to (see ## Artifact, see ## Field list).
4. Ensure every row's disposition is mitigated, accepted, or deferred —
   never blank or "in progress" (see ## Field list).
5. Before resolving the probe, confirm every row has a non-empty
   disposition, and tag every finding as a one-way or two-way door per
   `reversibility-tag`, requiring more rigorous mitigation evidence for
   one-way-door findings before the probe may resolve `pass`
   (see ## Resolution rule).

## Output shape

Applying this skill produces a STRIDE table — one row per
(element, threat category) with entry point/trust boundary and
disposition fields — written either inline in or pointed to by
`feasibility-record.md`'s threat-model probe field, typically at a
project-local path such as `feasibility/stride-table.md`.

## What it asks the user for

Walk the specification's design (or, if a diagram exists, its trust
boundaries) and ask the user, element by element: "what could go wrong here
from an adversarial-input or security-design standpoint, and what
trust boundary or entry point does it cross?" Do not ask for the whole
table in one turn — build it row by row as elements are identified,
confirming each row's disposition with the user when it is not obvious
from the specification alone.

For each row, classify the threat against one or more of the six STRIDE
categories: Spoofing, Tampering, Repudiation, Information Disclosure,
Denial of Service, Elevation of Privilege.

## Artifact

Writes to `feasibility-record.md`'s threat-model probe field (a pointer to,
or inline table within, a project-local STRIDE table file, e.g.
`feasibility/stride-table.md`). This artifact write is not gated — only the
state file's `status` transition is gated.

## Field list, one row per (element, threat category)

- **Element** — the specific component, data flow, or trust boundary being
  analyzed.
- **Threat category** — one or more of Spoofing / Tampering / Repudiation /
  Information Disclosure / Denial of Service / Elevation of Privilege.
- **Entry point or trust boundary crossed**.
- **Mitigation-or-accepted-risk disposition** — mitigated, accepted, or
  deferred. Never leave this blank or "in progress."

## Resolution rule

Every row requires a non-empty disposition field before the threat-model
probe can resolve to `pass`/`fail`/`blocked` in `feasibility-record.md`.
Before writing the probe's resolution, tag every finding as a one-way or
two-way door per `reversibility-tag` — a one-way-door threat finding should
carry more rigorous mitigation evidence than a two-way-door one before this
probe is allowed to resolve `pass`.
