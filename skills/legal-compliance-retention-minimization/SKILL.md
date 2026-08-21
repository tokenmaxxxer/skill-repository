---
name: legal-compliance-retention-minimization
description: Use when you need guidance on Data retention and minimization. Applies to the retention-and-minimization axis.
axis: retention-and-minimization
rule_count_floor: 2
---

# Data retention and minimization

Decision rules for setting how much personal data to collect and how
long to keep it, sourced live during issue #1174's legal-compliance
research pass (2026-08-13).

## Decision rules

1. When a field or data point is not required to fulfill the stated
   purpose (e.g. a birthdate collected "for personalization" that no
   feature actually reads), drop the field from collection entirely
   rather than collecting it and restricting its downstream use later.
   source: Art. 5(1)(c) GDPR (fetched 2026-08-13,
   https://gdpr-info.eu/art-5-gdpr/): personal data shall be "adequate,
   relevant and limited to what is necessary in relation to the
   purposes for which they are processed."
   counter-example: a field genuinely required by a downstream legal
   duty (e.g. date of birth for age-gated content) is not over-
   collection even if only one feature reads it — necessity is judged
   against the stated purpose, not against how many features use the
   field.

2. When defining a retention period for a data category, set the
   shortest period that still satisfies the operational, contractual,
   and legal-duty need for that specific purpose — do not set an
   organization-wide flat retention period (e.g. "keep everything 7
   years") across categories with different purposes.
   source: Secure Privacy DPO guidance (fetched 2026-08-13,
   https://support.secureprivacy.ai/article/data-retention-policies-dpo-guidance/):
   "For each data category and purpose, establish the shortest
   retention period that satisfies operational, contractual, and legal
   requirements."
   counter-example: a data category under an active legal hold (e.g.
   litigation, statutory audit) is exempt from its normal shortest-
   period rule for the hold's duration — do not auto-delete data under
   hold just because its ordinary retention clock has expired.

3. When a stated retention period lapses and no active hold or renewed
   purpose exists, delete or irreversibly anonymize the record rather
   than archiving it "in case it's useful later" — retaining data past
   its justified period is a direct violation regardless of storage
   security.
   source: GDPR Local storage-limitation guidance (fetched 2026-08-13,
   https://gdprlocal.com/gdpr-storage-limitation/), summarizing Art.
   5(1)(e) GDPR (https://gdpr-info.eu/art-5-gdpr/): data kept "for no
   longer than is necessary for the purposes for which the personal
   data are processed"; "Organizations that retain personal data
   beyond its legitimate retention period are in direct violation of
   GDPR — regardless of how securely the data is stored."
   counter-example: none — "might be useful later" is explicitly ruled
   out as a justification by the same source; this is a hard stop, not
   a case-by-case judgment call.

4. When a new feature proposes reusing an already-collected data
   category for a new purpose not covered by the original collection
   notice, treat that as new collection requiring its own necessity
   check and lawful basis, not as "already have the data, just use it."
   source: Art. 5(1)(c) GDPR purpose-limitation reading (fetched
   2026-08-13, https://gdpr-info.eu/art-5-gdpr/), corroborated by
   Usercentrics retention guidance (fetched 2026-08-13,
   https://usercentrics.com/knowledge-hub/gdpr-data-retention/): data
   minimization is scoped "to the purposes for which it is processed,"
   i.e. per-purpose, not per-dataset.
   counter-example: a purpose that is a genuine, foreseeable extension
   already disclosed in the original notice (e.g. "we may also use this
   to detect fraud," stated up front) does not require a fresh check —
   only an undisclosed new purpose does.

5. When a retention period is defined for a data category, name the
   actual enforcement mechanism that will delete or anonymize it at
   expiry (a scheduled job/TTL, or a manual process with a named owner
   and cadence) — a stated period with no named enforcement mechanism
   is not yet a retention policy, just a target.
   source: Art. 5(2) GDPR accountability principle (fetched 2026-08-13,
   https://gdpr-info.eu/art-5-gdpr/): "The controller shall be
   responsible for, and be able to demonstrate compliance with,"
   storage limitation — a period with no enforcement mechanism has
   nothing to demonstrate compliance with once the period lapses.
   counter-example: a category already covered by a platform-level TTL
   or automated deletion job that another rule/config already names
   does not need a second, redundant mechanism named here — cite the
   existing mechanism instead of inventing a new one.
