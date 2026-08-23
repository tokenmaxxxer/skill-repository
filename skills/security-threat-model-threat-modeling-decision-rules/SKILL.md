---
name: security-threat-model-threat-modeling-decision-rules
description: >-
  Use when drawing or scoping a DFD's trust boundaries, classifying an asset's sensitivity,
  running a STRIDE pass on a DFD element, CVSS-rating a threat, choosing a mitigation disposition
  (mitigate/avoid/transfer/accept), or signing off residual risk — practitioner-depth decision
  rules, distinct from generic STRIDE/FMEA walkthroughs or a feasibility-scoped threat disposition
  call. Trigger on requests like "신뢰 경계 어디에 그어야 해", "CVSS 점수 매겨줘", "rate this threat's attack
  vector and scope", "mitigate or accept this rated threat", "sign off the residual risk". Do NOT
  use for a full design-stage per-element STRIDE walkthrough from scratch (use stride) or for a
  feasibility spike's threat disposition (technical-feasibility-threat-model-disposition).
metadata:
  rule_count_floor: 12
  tier: moderate
  axes:
    - trust-boundary-scoping
    - asset-sensitivity-classification
    - stride-enumeration-by-element
    - cvss-risk-rating
    - mitigation-disposition
    - residual-risk-signoff
---

# Operational playbook: trust-boundary threat modeling decision rules (issue-1174)

Numbered condition → choice → source rules for the `security-threat-model`
role. Practitioner-depth decision rules, not methodology-name pointers.
Each rule cites the fetched source it is derived from; rules marked
`[REMOVAL]` are subtractive (drop/simplify/de-scope), per amendment 4 —
at least one removal rule is recorded per axis below.

## Trigger

Apply this skill — rather than `stride`, `fmea`, a generic
`risk-management-*` skill, or
`technical-feasibility-threat-model-disposition` — when the work is one
of: drawing or scoping a DFD and deciding where its trust boundaries sit
(rules 1.1–1.4); classifying a data store or field's sensitivity for
threat-modeling purposes, not just for storage/compliance labeling
(rules 2.1–2.3); running a STRIDE enumeration pass keyed to a specific
DFD element type and logging its findings with an owner and disposition
(rules 3.1–3.5, 5.6); CVSS-rating a specific threat's Attack Vector,
Attack Complexity, Privileges Required, or Scope (rules 4.1–4.5);
choosing among mitigate/avoid/transfer/accept for a rated threat (rules
5.1–5.5); or rating and signing off a threat's residual risk after
mitigation (rules 6.1–6.3).

## Procedure

1. Trust boundary scoping (rules 1.1–1.4): mark a trust boundary at
   every privilege/trust change, not only network edges; scope the DFD
   to one side per model; collapse same-technology same-boundary
   elements into one node (`[REMOVAL]`, rule 1.3); still record threats
   for flows that stay inside one boundary.
2. Asset/data sensitivity classification (rules 2.1–2.3): model the
   system before scoring any threat; drop asset nodes with no
   reader/writer (`[REMOVAL]`, rule 2.2); classify an asset by its most
   sensitive plausible field content, not its nominal label.
3. STRIDE enumeration by DFD element type (rules 3.1–3.5, 5.6): apply
   only the STRIDE categories an element type is exposed to; run the
   full checklist at every trust-boundary crossing; do not chase
   downstream consequences mid-enumeration (`[REMOVAL]`, rule 3.3); log
   every finding with an owner and a fix/accept/backlog decision; triage
   an ambiguous candidate against the fixed accept/dismiss/investigate
   question set; cite where an existing mitigating control actually
   lives before crediting a `mitigate` disposition (rule 5.6).
4. CVSS-style risk rating (rules 4.1–4.5): rate Attack Vector by what
   the exploit chain requires; score Local when malicious data crosses
   components before the vulnerability triggers; rate Attack Complexity
   against the standard undisabled configuration; rate Privileges
   Required by the delta gained; only mark Scope Changed across a
   security-authority boundary, not within one (`[REMOVAL]`, rule 4.5).
5. Mitigation disposition selection (rules 5.1–5.5): rank mitigation
   attention by likelihood × impact; prefer eliminating a non-load-bearing
   feature over compensating controls (`[REMOVAL]`, rule 5.2); disable
   unused services/ports/accounts directly (`[REMOVAL]`, rule 5.3);
   transfer only risks a named contract/insurance instrument actually
   covers; accept only against a stated tolerance threshold.
6. Residual risk sign-off (rules 6.1–6.3): record the post-mitigation
   rating, not the pre-mitigation one restated; escalate to the named
   approver when residual severity still exceeds tolerance; drop an
   already-accepted, unchanged item from the active findings list
   (`[REMOVAL]`, rule 6.3).

## Output shape

A per-threat condition → choice → source decision at whichever axis
triggered the skill, and — when the session spans a full pass — a
dispositioned STRIDE table (finding, owner, fix/accept/backlog) plus
residual-risk-notes carrying the post-mitigation rating and, where
above tolerance, the named approver's sign-off decision.

## Rule index

Full rule text, citations, and counter-examples:
`references/rules.md` in this skill's directory — read it when a
matched rule's detail is needed.

- 1.1 — a data flow crosses from one privilege/trust zone to another (internet → DMZ, user tier → admin tier, or a change in "who can be trusted" assumptions on the same host) → mark a trust boundary there even if the transition is
- 1.2 — a system has both client-side and server-side components under analysis → build the primary DFD for the side under this review's control,
- 1.3 — [REMOVAL] two or more processes/data stores are implemented in the same technology and sit inside the same trust boundary → merge them into a single modeled element rather than
- 1.4 — a data flow, data store, or process sits entirely within a single trust boundary (e.g. server-internal only) → still record tampering/information-disclosure/DoS threats for
- 2.1 — a threat-model session is opened for a spec that has not yet had its data flows, data stores, processes, and external entities enumerated → complete asset/system modeling (DFD) first; do not begin
- 2.2 — [REMOVAL] a data store in the draft DFD has data flowing in but no process ever reads it back out (a "data sink"), or data appears with no process producing it (a "magic… → either add the missing reader/writer process to the model
- 2.3 — a data store holds fields that could carry PII, payment data, or sector-specific regulated data (e.g. health data under HIPAA), even if the spec labels the store generic… → rate the asset at the sensitivity of its most sensitive
- 3.1 — a DFD element is being checked against the six STRIDE categories → apply Tampering, Information Disclosure, and Denial of Service
- 3.2 — a data flow crosses a marked trust boundary → run the full STRIDE checklist against that flow rather than
- 3.3 — [REMOVAL] while enumerating one STRIDE threat (e.g. spoofing a process), the analyst notices it could cascade into others (e.g. spoofing → DoS → elevation of privilege) → record the originating threat and move on; do not expand the
- 3.4 — a STRIDE pass over a trust boundary produces one or more findings → attach an owner and one of fix/accept/backlog to each finding
- 3.5 — a candidate threat surfaces during enumeration whose applicability is genuinely unclear (not simply "feels unlikely," which Rule 3.2 already forbids skipping) — e.g. a d… → run a short fixed set of triage questions (is the precondition
- 5.6 — a mitigation-list entry's disposition is `mitigate` and the entry claims the mitigating control already exists (as opposed to being newly proposed) → cite the specific file:line, config key, or infrastructure
- 4.1 — exploitation requires the attacker to reach the vulnerable component over a network at some point in the chain, even if the final trigger executes locally (e.g. a local… → score Attack Vector as Network (N), not Local — AV reflects
- 4.2 — malicious data is received over a network by one component, then handed to a separate vulnerable component (e.g. downloading a malicious document, then opening it in vul… → rate Attack Vector Local, not Network, for the second
- 4.3 — rating Attack Complexity (AC) for a threat → score against the reasonable, undisabled, non-custom
- 4.4 — an attacker already holds some level of access before exploiting the flaw → compare privileges held before exploitation against privileges
- 4.5 — [REMOVAL] a vulnerability's impact reaches beyond the component that contains the flaw (e.g. a container escape, a sandboxed script affecting the host) → only set Scope to Changed when the affected resource is
- 5.1 — multiple STRIDE findings exist for one trust boundary and mitigation effort must be sequenced → compute a likelihood × impact ranking and address high-rank
- 5.2 — [REMOVAL] a threat traces to an optional feature, endpoint, service, or permission that is not required for the system's stated purpose → remove/disable the feature (avoid-by-elimination) rather than
- 5.3 — [REMOVAL] the DFD/asset survey turns up a running service, open port, or standing account not required by the current spec (e.g. a leftover integration, a temporary vend… → cut the unnecessary surface directly — "if a service does not
- 5.4 — a threat's root cause sits outside this system's control (e.g. a third-party processor's breach exposure) and no direct technical mitigation is available from this side → assign transfer disposition and name the specific
- 5.5 — a rated threat's residual severity, after considering available mitigations, falls at or below the org's stated risk tolerance for that asset class → record an explicit accept disposition naming the tolerance
- 6.1 — a mitigation has been selected and applied (or committed) for a threat → re-rate the threat's severity assuming the mitigation is in
- 6.2 — the post-mitigation residual rating remains above the asset's stated risk tolerance threshold → route the residual-risk-note to the approver named in
- 6.3 — [REMOVAL] a threat's residual rating has already been accepted (per Rule 5.5) at a stated tolerance and no new information (design change, new attack pattern, new asset… → remove that item from the active open-findings list for
- S1 — Academic layer: why the removal category is required, not optional → references/rules.md
- S2 — Sources → references/rules.md
