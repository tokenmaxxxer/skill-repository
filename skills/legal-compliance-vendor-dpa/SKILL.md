---
name: legal-compliance-vendor-dpa
description: Use when you need guidance on Vendor / sub-processor DPA requirements. Applies to the vendor-dpa-requirements axis.
axis: vendor-dpa-requirements
rule_count_floor: 2
---

# Vendor / sub-processor DPA requirements

Decision rules for what a data processing agreement must contain before
a vendor can be onboarded, sourced live during issue #1174's
legal-compliance research pass (2026-08-13).

## Decision rules

1. When engaging any vendor, cloud provider, or third party that will
   handle personal data on the controller's behalf, require a signed
   DPA covering all eight Art 28(3) topics before data flows — do not
   proceed on a generic commercial contract or a vendor's own terms of
   service that omit processor obligations.
   source: Recording Law GDPR DPA guide (fetched 2026-08-13,
   https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-data-processing-agreement/):
   "a data processing agreement (DPA) is required whenever an
   organisation engages a vendor, cloud provider, payroll bureau, or
   any third party that handles personal data on its behalf," covering
   "documented instructions, confidentiality... security measures,
   subprocessor engagement rules, data subject rights assistance,
   breach notification..., return or deletion..., and audit rights."
   counter-example: a vendor that never receives or accesses personal
   data (e.g. a static-asset CDN serving no user-identifying content)
   is not a processor under Art 28 and does not need a DPA for that
   relationship.

2. When a processor proposes engaging a new sub-processor, require
   either specific prior written authorization for that named
   sub-processor, or confirm a standing general-authorization clause
   with a working objection window already exists in the DPA — do not
   allow a sub-processor to onboard on implicit or after-the-fact
   notice.
   source: Art. 28(2) GDPR via WatchDog Security summary (fetched
   2026-08-13, https://watchdogsecurity.io/gdpr/processor-safeguards-and-management):
   "a processor must not engage another processor without prior
   specific or general written authorisation of the controller."
   counter-example: none for the authorization requirement itself — but
   under a valid standing general-authorization clause, a new
   sub-processor may onboard without a fresh signature per addition, as
   long as the controller's objection window is honored.

3. When a sub-processor is added under a DPA, flow the same data-
   protection obligations imposed on the primary processor down to that
   sub-processor by contract — do not accept a sub-processor agreement
   that is weaker than the controller-processor DPA it sits under.
   source: Art. 28(4) GDPR via Recording Law (fetched 2026-08-13,
   https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-data-processing-agreement/):
   "the same data protection obligations in the controller-processor
   DPA be imposed on every sub-processor by contract, and the processor
   remains fully liable for the sub-processor's performance."
   counter-example: none — the flow-down and the processor's residual
   liability are both stated as unconditional in the same source.

4. When a DPA's sub-processor chain has grown to include processors
   that are no longer actually used (e.g. a decommissioned analytics
   vendor still listed), remove the stale entries from the
   sub-processor list and its authorization record rather than leaving
   an inflated list that overstates current data exposure.
   source: general audit-rights obligation under Art 28(3)(h) via
   KirkpatrickPrice DPA requirements guide (fetched 2026-08-13,
   https://kirkpatrickprice.com/blog/requirements-for-gdpr-data-processing-agreement/):
   the processor must give the controller "whatever information it
   needs to ensure they are both meeting their Article 28 obligations,"
   which an inflated stale sub-processor list defeats.
   counter-example: a sub-processor kept on the list for an active data
   deletion/wind-down period (data not yet fully purged) is correctly
   still listed until that deletion completes — remove it once deletion
   is confirmed, not before.

5. When personal data flows through a chain of more than one
   sub-processor (e.g. an analytics vendor that resells to further ad
   or enrichment partners), require that each downstream vendor
   actually receive and honor a current, per-vendor legal-basis/consent
   status at processing time — do not treat the top-level DPA's
   flow-down clause (rule 3) alone as proof that every party several
   hops down the chain is honoring it in practice.
   source: Art. 28(3)(a) GDPR via Recording Law's DPA-topics list
   (fetched 2026-08-13,
   https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/gdpr-data-processing-agreement/),
   which lists "documented instructions" as a required, checkable DPA
   element — a contractual flow-down clause is the documented
   instruction; verifying it is actually followed downstream is a
   separate, operational check.
   counter-example: a two-party chain with no further sub-processing
   (controller-processor only) has no downstream hop to verify — rule 3
   already covers the contractual requirement in full for that case.
