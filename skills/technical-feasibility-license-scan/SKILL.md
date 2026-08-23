---
name: technical-feasibility-license-scan
description: >-
  Use when the feasibility role is in its `probing` state and needs to run the
  legal-regulatory probe — i.e. dependencies (packages, SaaS, third-party
  services) are being pulled into the specification and their licenses and
  applicable regulatory regimes have not yet been recorded. Trigger on requests
  like "라이선스 스캔해줘", "license scan the dependencies", "per-dependency license
  verdict", "regulatory applicability note". Do NOT use for judging DPIA
  necessity or GDPR high-risk thresholds by decision rule outside the probe
  workflow (use technical-feasibility-license-and-regulatory-risk).
---

# License scan

**Belongs to state:** `probing`, legal-regulatory probe.

## Trigger

This applies whenever the feasibility role is in its `probing` state and the
legal-regulatory probe for the current specification has not yet resolved —
concretely, when the specification names or implies dependencies (packages,
SaaS, third-party services) whose licenses have not been verdicted, or when
it touches a data category, customer base, or region whose regulatory
applicability has not yet been noted.

## Procedure

1. Identify the dependencies (packages, SaaS, third-party services) the
   specification would pull in, asking the user if they are not already
   listed (see ## What it asks the user for).
2. Ask the user what regulatory regime, if any, they believe applies (data
   category, customer/region), so the applicability note is grounded rather
   than guessed, and be plain that this is research and not a legal opinion
   (see ## What it asks the user for).
3. Record findings by writing to `feasibility-record.md`'s legal-regulatory
   probe field, pointing to or inlining a project-local file such as
   `feasibility/license-scan.md`; note that this artifact write is not
   itself gated, only the state file's `status` transition is (see ##
   Artifact).
4. For each dependency, produce a per-dependency license verdict — package
   name, declared license, compatibility verdict, and any custom or
   dual-licensing edge case — and write the regulatory-applicability note,
   stating plainly where it is research rather than legal advice (see ##
   Field list).
5. Before treating the probe as resolved, confirm every named dependency
   has a license verdict and that the regulatory-applicability note has
   been written explicitly, even if it states "none identified" (see ##
   Resolution rule).

## Output shape

Applying this skill produces (or updates) a per-dependency license-verdict
table and a regulatory-applicability note, written into a project-local
file such as `feasibility/license-scan.md` and pointed to from (or inlined
in) `feasibility-record.md`'s legal-regulatory probe field.

## What it asks the user for

Ask the user what dependencies (packages, SaaS, third-party services) the
specification would pull in, if not already listed. Then ask what
regulatory regime, if any, the user believes applies (data category,
customer/region), so the note below is grounded rather than guessed. This
is research, not a legal opinion — say so plainly if a real legal
determination is needed and none is available.

## Artifact

Writes to `feasibility-record.md`'s legal-regulatory probe field (a pointer
to, or inline table within, a project-local file, e.g.
`feasibility/license-scan.md`). This artifact write is not gated — only the
state file's `status` transition is gated.

## Field list

- **Per-dependency license verdict** — one verdict per dependency (FOSSA /
  ScanCode-or-equivalent shape): package name, declared license,
  compatibility verdict, and any custom or dual-licensing edge case flagged.
- **Regulatory-applicability note** — which regulatory regimes (if any)
  apply to this specification, mirroring the DPIA-before-processing pattern
  for data-handling designs. State plainly where this is research rather
  than legal advice.

## Resolution rule

The legal-regulatory probe does not resolve until every named dependency
has a license verdict and the regulatory-applicability note is written
(even if that note is "none identified" — it must be an explicit finding,
not a silent omission).
