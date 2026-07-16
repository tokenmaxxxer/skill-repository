---
name: stride
description: >-
  A design-stage security threat analysis procedure (STRIDE per-element threat modeling):
  decompose a system as a data flow diagram (external entities, processes, data stores, data
  flows, trust boundaries), enumerate threats per element against the STRIDE applicability table
  (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of
  privilege), and disposition every threat as mitigate/accept/redesign. Structurally the security
  sibling of `fmea` — same enumerate-and-disposition shape, applied to threats instead of failure
  modes. Use when the user wants to find what could be attacked in a design before it ships — e.g.
  "이 설계 보안 위협 분석해줘", "위협 모델링 해줘", "threat model this design", "run a STRIDE analysis". Do
  NOT use for code-level vulnerability scanning, for compliance/regulatory mapping (point to
  `compliance-scan`), for privacy threats (identifiability, linkability — that's LINDDUN), or
  when there is no concrete design with enumerable elements yet.
---

# STRIDE (per-element threat modeling)

## First: does this even need the procedure?

Check these before running the full walk, because forcing it onto the wrong target wastes the user's time:

- **Is there a concrete design to decompose?** STRIDE threat-models a design — components, data flows, trust boundaries. If the user can't point to an architecture or design with distinguishable elements, there is nothing to draw a data flow diagram (DFD) against yet. That is a design/discovery gap, not a threat-modeling gap — say so.
- **Is this actually a request to scan existing code for vulnerabilities?** Per-element STRIDE analyzes a design on paper (or a diagram), not source code line by line. If the ask is "find the bugs in this codebase," that is static/dynamic analysis, not this skill.
- **Is this a compliance or regulatory question?** "What rules apply to this" is `compliance-scan`'s job, not STRIDE's. STRIDE answers "what can an attacker do," not "what does the law require."
- **Is the concern privacy rather than security** — identifiability, linkability, detectability, disclosure of information *to the wrong party by design*, unawareness, non-compliance, or difficulty of consent/control? That is LINDDUN's home turf, the deliberate privacy-side complement to STRIDE. Point there instead of forcing privacy harms into the six security categories below.
- **Does the SDL-derived scope gate (Step 1) come back all-no?** If the design has no network-facing interface, handles no personal/sensitive data, has no privilege boundaries, and is not itself a security feature, a full threat model is not warranted yet — see Step 1's gate.

Everything below applies when there is a real design on the table with elements, data flows, and real attackers who would benefit from breaking it.

## Evidence grade — read before citing this to anyone

- **Origin**: Loren Kohnfelder and Praerit Garg wrote "The threats to our products" for Microsoft's internal publication *Interface* on April 1, 1999 — Microsoft's first documented threat-modeling methodology, and the origin of what became STRIDE. Note the evidence character honestly: the 1999 document itself was not obtained in verification. The attribution rests on secondary sourcing — Adam Shostack's 2014 book bibliography (with an archive URL) and his 2008 ModSec paper's explicit authorship correction. Treat this as bibliographically confirmed secondary attribution, not a primary-source read of the original memo.
- **The six categories and their verbatim definitions are primary-sourced** (Microsoft SDL book, Howard & Lipner 2006, ch. 9): Spoofing (posing as something or somebody else), Tampering (malicious modification of data or code), Repudiation (denying an action that others can neither confirm nor contradict), Information disclosure (exposure of information to those not authorized to see it), Denial of service (denying or degrading service to valid users), Elevation of privilege (gaining capability beyond what was intended).
- **The security-property mapping is primary-sourced** (MSDN Magazine, Nov 2006, Hernan/Lambert/Ostwald/Shostack, Figure 3; Shostack 2014, Table 3-1): Spoofing↔Authentication, Tampering↔Integrity, Repudiation↔Non-repudiation, Information disclosure↔Confidentiality, Denial of service↔Availability, Elevation of privilege↔Authorization. Every mitigation in Step 5 cites one of these six labels — that is what makes "mitigated" mean something specific rather than a vague reassurance.
- **The DFD decomposition is primary-sourced**: the four standard element types — data flows, data stores, processes, and interactors (external entities) — plus trust boundaries added specifically for threat modeling, verbatim from the 2006 article.
- **The element × category applicability table is primary-sourced but explicitly bounded** (MSDN 2006, Figure 5; SDL book, Table 9-5): Processes → all six categories; Interactors/external entities → Spoofing and Repudiation; Data flows → Tampering, Information disclosure, Denial of service; Data stores → Tampering, Information disclosure, Denial of service, plus Repudiation conditionally when the store holds logs or audit data.
- **Critical limits of that table — bake this into every run, not just this section**: the table derives from an *unpublished* internal Microsoft CVE/MSRC vulnerability analysis by Hernan and Howard. Shostack explicitly disclaims universal applicability — the analysis was scoped to issues Microsoft ships updates for, and his 2014 book labels the matrix Microsoft-specific. The 2008 paper's version of the table literally contains a "?" cell (Data Store × Repudiation) — even the authors were unsure. Therefore: **the table is a heuristic floor that makes the enumeration space finite and checkable. It is not a proven-complete taxonomy.** Organizations are advised by the authors themselves to extend it per their own element types and history. State this plainly whenever the table is used, not just once.
- **Institutional adoption preceded empirical validation by roughly a decade.** Microsoft's "security push" began in early 2002 (Windows Server 2003 verification phase: threat modeling, code reviews, security testing); the SDL mandate was formalized by 2004 for software that is internet/network-connected, processes personal or sensitive data, or is used in enterprises (Lipner, ACSAC 2004). The SDL book's gate rules for when threat modeling is *required* are: networking interfaces, kernel/user-mode interaction, a high-privilege process reachable by non-admin users, or any security feature. Step 1's scope gate below BLENDS these with the 2004 mandate scope: its network-facing and security-feature conditions come from the book's gate rules; its privilege-boundary condition merges the book's kernel/user-mode and non-admin-to-high-privilege rules; its personal/sensitive-data condition comes from the 2004 mandate criteria.
- **The first empirical evaluation is Scandariato, Wuyts & Joosen** (Requirements Engineering, 2013/2015): a descriptive study with 57 master's students measuring valid threats per hour (productivity), false positives (correctness), and false negatives (completeness). Do not cite specific rates from it — the numbers were not confirmed as reliable claims in verification, only the study's existence and what it measured. A follow-up peer-reviewed study exists (Van Landuyt & Joosen 2021, SoSyM, analyzing 640 assumptions across 96 STRIDE models — study scope verified); its result percentages were confirmed only via secondary citation, so do not quote them.
- **Threat explosion is a documented, medium-grade premise**: follow-up literature treats it as established that real projects surface more threats than can all be addressed — this is why Step 4 (triage) is mandatory, not optional polish.
- **What must NOT appear in output from this skill** (refuted or unverified in adversarial verification — do not state these as fact): the precision-vs-speed trade-off claim from the Scandariato study (refuted); the STRIDE acronym's first public-publication attribution to Howard & LeBlanc's *Writing Secure Code* (unresolved); Microsoft Threat Modeling Tool specifics (unverified); PASTA comparisons (unverified); "STRIDE-per-interaction" as an officially sourced variant (unverified — this skill uses per-element only, for the sourced reason above).
- **Historiographic gap, worth stating honestly**: the *current* Microsoft SDL page does not name STRIDE by name — it describes a generic five-step threat-modeling flow. The per-element sources this skill relies on are the 2006–2014 historical documents. If asked "is this still Microsoft's current method," say so plainly rather than implying continuity that was not confirmed.
- **What this skill actually delivers**: a finite, blank-cell-checkable enumeration walk over a bounded (heuristic, Microsoft-derived) category table, plus a disposition ledger where every threat has exactly one owner-bearing outcome. It is not a guarantee of finding all threats, and it is not a proof of completeness — it is a floor, not a ceiling.

## Procedure

### Step 1 — Scope gate

Check each condition, adapted from the verified SDL trigger rules, against the design:

- Does it have a network-facing interface?
- Does it handle personal or sensitive data?
- Does it have privilege boundaries — components running at different privilege levels, or non-admin users able to reach a high-privilege process?
- Is the thing being built itself a security feature (auth, crypto, access control, etc.)?
- Is the primary concern actually privacy (identifiability, linkability, disclosure-by-design, unawareness) rather than these security properties? If so, this is LINDDUN's job — point there instead of continuing.

**Gate:** answer yes/no per condition, explicitly. If every condition is no, stop and exit — state "no threat model required by the SDL-derived trigger; revisit if the design gains one of these properties" rather than manufacturing threats for a design that doesn't need it yet.

### Step 2 — DFD decomposition

Enumerate the design as a data flow diagram:

- **External entities / interactors** — numbered list, with count.
- **Processes** — numbered list, with count.
- **Data stores** — numbered list, with count.
- **Data flows** — numbered list, with count; every flow names both of its endpoints (source and destination).
- **Trust boundaries** — listed explicitly, with the data flows that cross each one named.

**Gate:** every element type has a numbered list with a stated count (e.g., "3 interactors, 5 processes, 2 data stores, 9 data flows"). Every data flow names its two endpoints. Every trust boundary lists which flows cross it. An element that cannot be classified into the four types signals the DFD needs rework — do not force-fit it into one of the four just to move on.

### Step 2a — Classify elements by risk contribution

Before enumerating every cell, classify each element along two axes so the procedure invests depth where it matters and compresses where it doesn't. This gate prevents the output from expanding to N×M×K for elements that carry negligible threat surface.

Score every element from Step 2 against these two axes:

- **A: Exposure** — does it cross a trust boundary, or is it reachable from outside the trust boundary?
- **B: Sensitivity** — does it handle authentication material, cryptographic keys, sessions, access control decisions, personal data, or run at elevated privilege?

Classification rule (apply the higher of the two):

| Level | Rule | Enumeration depth |
|---|---|---|
| **High** | A or B is yes | Full per-category walk, each threat written as "an attacker could…", each "none identified" has a one-line reason. |
| **Medium** | Neither A nor B, but element is user-facing or touches data | Per-category threats enumerated, one line each. "None identified" cells may be grouped: "M of N cells for [element type] had no applicable threat." |
| **Low** | Neither A nor B, internal-only, no sensitive data | Aggregate: "N elements (list names) — no applicable threats beyond ambient controls." No per-category walk needed. |

**Gate:** every element has a written High/Medium/Low classification with a one-phrase rationale (e.g., "High — crosses trust boundary at auth flow"). No element is dropped; the classification itself is the audit record for why some elements received compressed treatment. Record this as a compact table before proceeding.

### Step 3 — Per-element threat enumeration against the applicability table

Apply the verified element × category table:

| Element type | Applicable STRIDE categories |
|---|---|
| Process | Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege (all six) |
| Interactor / external entity | Spoofing, Repudiation |
| Data flow | Tampering, Information disclosure, Denial of service |
| Data store | Tampering, Information disclosure, Denial of service; Repudiation also applies if the store holds logs or audit data |

Apply the depth rule from Step 2a per element:

- **High**: walk each category the table marks as applicable. For each cell, record at least one concrete threat phrased as "an attacker could ..." or an explicit "none identified" note with a one-line reason.
- **Medium**: walk each applicable category. Record threats, one line each. Group "none identified" cells into a single count line per element type (e.g., "3 of 5 cells for Process X had no applicable threat").
- **Low**: skip the per-category walk — the Step 2a aggregate note is sufficient.

State the table's heuristic-floor character again here, at the point of use: it bounds the walk so it terminates and is checkable — it does not prove the walk found everything, and teams are advised by the table's own authors to extend categories per their own element types where warranted.

**Gate:** every High element has no blank cells — every cell is either a named threat or a reasoned "none identified" note. Medium elements have threats enumerated per category; "none identified" may be grouped by count. Low elements are covered by the Step 2a aggregate note. No element is left unaccounted.

### Step 4 — Triage

Threat explosion is expected, not a sign something went wrong — plan for it rather than being surprised by it.

- Prioritize the enumerated threats.
- Elevation-of-privilege threats and any threat on a flow that crosses a trust boundary get **mandatory review** — a structural rule, not a probability-weighted cutoff, mirroring FMEA's severity-first discipline of never letting a low-likelihood, high-impact risk hide behind an aggregate score.

**Gate:** a priority ordering exists with its rationale written down. No threat is dropped silently — everything enumerated in Step 3 either appears in the ordering or is accounted for.

### Step 5 — Disposition per threat

Every threat gets exactly one of:

- **Mitigate** — name the mitigation, and name which of the six security properties it restores (Authentication, Integrity, Non-repudiation, Confidentiality, Availability, Authorization — per the verified mapping in Evidence grade).
- **Accept** — name the acceptor: a specific person, not "the team" or a role alone.
- **Redesign** — the element or flow changes; loop back to Step 2 to re-decompose the affected part of the DFD before re-enumerating.

**Gate:** every threat from Step 3/4 has exactly one disposition. Every mitigation cites its restored property label. Every acceptance names a real person. A threat with no disposition, or a mitigation with no property cited, is incomplete.

### Step 6 — Residual report

Summarize:

- Counts: threats identified, mitigated, accepted, redesigned-away.
- Element classification table from Step 2a (High/Medium/Low with rationale — the audit record for why depth varied).
- "None identified" cells: list individually for High elements only. For Medium elements, report grouped counts per element type (e.g., "4 none-identified cells across 2 Medium processes"). Low elements are covered by their Step 2a aggregate note.
- Standing caveats to restate every time: the applicability table is a Microsoft-derived heuristic floor, not a proven-complete taxonomy; institutional adoption of this method preceded empirical validation by roughly a decade; the current Microsoft SDL page no longer names STRIDE explicitly.

**Gate:** the report states all three counts, includes the Step 2a classification table, lists "none identified" cells at the depth dictated by element risk level, and includes the standing-caveats paragraph verbatim in substance — omitting the caveats is treating heuristic guidance as proven fact.
