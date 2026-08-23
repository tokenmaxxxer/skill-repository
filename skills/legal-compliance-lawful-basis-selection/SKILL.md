---
name: legal-compliance-lawful-basis-selection
description: Use when selecting or auditing the GDPR Article 6(1) lawful basis (contract, legitimate interests, or consent) for a specific data processing activity.
metadata:
  axis: lawful-basis-selection
  rule_count_floor: 2
---

# Lawful basis selection

Decision rules for picking a GDPR Article 6(1) lawful basis for a given
processing activity, sourced live during issue #1174's legal-compliance
research pass (2026-08-13).

## Trigger

Apply this skill when a specific processing activity needs an Article
6(1) lawful basis assigned or audited — distinguishing it from sibling
axes that govern the interface collecting consent
(`legal-compliance-consent-ux`) or how long the resulting data is kept
(`legal-compliance-retention-minimization`), rather than which basis
justifies the processing in the first place.

## Procedure

1. If the activity is required to deliver what the data subject asked
   for, pick the contract basis over consent (rule 1).
2. If the activity serves the controller's own operational need with no
   requirement for the subject's free choice, pick legitimate interests
   and record a balancing test (rule 2).
3. If no contract, legal duty, or surviving legitimate-interest
   balancing test applies, fall back to consent — not as a first choice
   (rule 3).
4. If a purpose already has a basis, remove any duplicate basis stacked
   onto the same purpose "for safety" (rule 4).

## Output shape

A named Article 6(1) basis (contract / legitimate interests / consent)
per processing purpose, with the balancing-test record attached when
legitimate interests is chosen, or a flagged duplicate-basis removal
when rule 4 applies.

## Decision rules

1. When a processing activity is required to deliver what the data
   subject actually asked for (e.g. shipping an order, authenticating a
   login), pick the contract basis (Art 6(1)(b)) over consent — do not
   layer a consent checkbox on top of processing that is already
   contractually necessary.
   source: Art. 6 GDPR (fetched 2026-08-13, https://gdpr-info.eu/art-6-gdpr/):
   "processing is necessary for the performance of a contract to which
   the data subject is party."
   counter-example: an upsell or optional feature bundled into the same
   checkout flow (e.g. marketing profiling) is not "necessary" for that
   contract — it needs its own separate basis (usually consent), not a
   ride on the contract basis for the core transaction.

2. When processing serves the controller's own operational need (fraud
   prevention, direct marketing to existing customers, internal
   analytics) and does not require the data subject's free choice, pick
   legitimate interests (Art 6(1)(f)) and record a documented balancing
   test — do not default to consent just because it "feels safer."
   source: Art. 6 GDPR (fetched 2026-08-13, https://gdpr-info.eu/art-6-gdpr/):
   basis (f) applies "except where such interests are overridden by the
   interests or fundamental rights and freedoms of the data subject."
   counter-example: direct marketing to a person who has never
   transacted with the controller (cold outreach) cannot rely on
   legitimate interests under most member-state ePrivacy overlays —
   route that case to consent instead.

3. When a processing purpose cannot be tied to a contract, a legal
   duty, or a documented legitimate-interest balancing test that
   survives scrutiny, pick consent (Art 6(1)(a)) as the fallback basis,
   not as the default first choice — consent is the basis with the
   highest revocation/withdrawal exposure, so treat it as last-resort,
   not first-resort.
   source: gdprlocal.com summary of Art 6 (fetched 2026-08-13,
   https://gdprlocal.com/gdpr-legitimate-interest/): "Most major GDPR
   fines trace back to either invalid consent (basis a) or unsupported
   legitimate interest claims (basis f)."
   counter-example: none — this is the fallback rung itself; if no
   other basis fits, consent is correctly the answer, not a symptom of
   under-analysis.

4. When a processing activity is layered onto an existing lawful basis
   purely for internal convenience (e.g. a second consent banner
   requested "just in case" for data already covered by the contract
   basis), remove the duplicate basis instead of stacking two bases on
   one purpose — pick exactly one basis per purpose and drop the rest.
   source: ICO "A guide to lawful basis" (fetched 2026-08-13,
   https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/):
   each processing purpose is matched to the single most appropriate
   basis, not stacked; recorded once on the Record of Processing
   Activity entry.
   counter-example: a single data flow that genuinely serves two
   independent purposes (e.g. the same email used both to fulfill an
   order and, separately, for opted-in marketing) legitimately carries
   two bases — one per purpose — so do not collapse those into one
   basis just to simplify the record.
