---
name: compliance-scan
description: >-
  An execution harness for regulatory & compliance research: it maps which laws, licenses,
  certifications, and platform policies apply to a product across the product/data/customer/region
  axes, traces each to primary-source law or the regulator's guidance, grades legal risk, and
  stays on the research side of the research-vs-legal-advice line. Use whenever the user needs to
  know what rules apply before building or launching — "우리 서비스에 어떤 규제가 적용돼", "what
  regulations apply to this product", "do we need a license/permit for X", "is GDPR/개인정보보호법
  relevant", "what certifications does this need (KC/CE/FCC)", "app store policy check",
  "compliance requirements for market Y". Trigger it when a team is about to launch assuming
  they're compliant. It produces a researched compliance map and flags what needs a lawyer; it
  does NOT give legal advice or a compliance opinion. Do NOT use for contract drafting, a
  definitive legal determination (needs a licensed attorney — say so), or non-regulatory market
  research (market-recon).
---

# Compliance Scan — a regulatory-mapping harness that stops at the legal-advice line

When this triggers, **you do the research** — map the applicable rules, pull the primary-source law and the regulator's own guidance, grade the risk — and hand back a compliance map. The hard boundary: this is *research*, never legal advice. The failure mode it prevents two ways: launching on the assumption you're compliant and hitting a permit/privacy/certification wall (or a fine), and overstepping into "this is legal/you may do this," which only a licensed attorney can say.

## First: research, not a ruling

Two things this skill must never do: state that a specific product *is or isn't* subject to a law as a final determination, or advise that something is legal/compliant. Those are legal conclusions (an attorney applying law to your facts). What it does: establish that a rule exists, quote what the statute/regulator's guidance actually says, show how regulators have interpreted similar cases, and grade the risk — so a human (and, past a risk threshold, a lawyer) can decide. Also distinguish **legal obligation** (the law requires it) from **market-driven requirement** (no law requires SOC 2 or ISO 27001, but customers/deals do) — teams conflate these constantly.

## The one rule that carries the most weight

**Trace every requirement to primary source, or flag it unverified.** The authority hierarchy is strict: statute/regulation text and binding case law (primary) > the regulator's own guidance, official interpretations, no-action letters (quasi-primary, decisive for predicting enforcement) > law-firm newsletters and industry commentary (persuasive only) > blogs/wikis/forums (verify before trusting). A requirement sourced only to a blog or an AI summary is **unverified** — label it and point to the primary text (e.g. the national statute portal), because reg summaries and even AI-reconstructed statute text are frequently wrong on the number and the nuance that decide applicability.

## The protocol

### 1 — Map the applicability surface (four axes)

Applicability lives at the intersection of: **product** (what it is and does — payments, location, AI decisions, targets children, health-related), **data** (personal / sensitive / financial / health / children's data), **customer** (B2C/B2B, minors, vulnerable groups, regulated-industry customers), and **region** (where you're established, where customers are, where data is processed — plus extraterritorial reach). Build a compliance matrix: each candidate rule × applies?/citation/confidence/required action. Cells you can't resolve get marked "undetermined — needs legal review," not guessed.

### 2 — Work the high-frequency domains

- **Data privacy**: GDPR applies extraterritorially (establishment, or targeting/monitoring EU data subjects — judged by currency, language, EU shipping, tracking). Korea's PIPA has its own definitions (personal vs pseudonymized info, keyed on re-identification) and a *different* DPIA structure (public-body mandate + private voluntary) than GDPR's (high-risk-triggered for everyone) — never assume one region's rule maps to another.
- **Sector licensing**: run the regulator's own decision tree — e-finance (issue a monetary instrument → license; intermediate/process payments → register), medical (does the software's intended use make it a medical device / SaMD, and what risk class), telecom, etc.
- **Certifications & standards**: which are *legally mandatory for market entry* (KC in Korea, CE in EU, FCC for US radio/electronics — product-triggered) vs *market-driven* (ISO 27001, SOC 2).
- **Platform policy**: tag app features (payments, health data, kids, UGC, tracking) and map each to the App Store / Play policy section, plus region add-ons (DMA, COPPA).

### 3 — Grade the risk

For each identified obligation, rate likelihood of enforcement (× regulator activity, precedent) against severity (guidance → fine → criminal → license revocation / shutdown). The high×high cells (e.g., unlicensed financial activity, large-scale personal-data breach) are the threshold that *requires* a lawyer before proceeding — mark them as stop-and-consult, not as things you've cleared.

### 4 — Deliver with honest coverage

The compliance map ships with: each requirement, its primary-source citation (or an "unverified — primary source not reached" flag), legal-obligation-vs-market-requirement label, risk grade, and required action. Plus a coverage statement: domains and regions scanned, what wasn't reached (paywalled standards, blocked statute portals, jurisdictions not covered), and the date — regulation changes, so stamp it. When a statute portal or primary source couldn't be fetched, say so and tell the user to open the official source (e.g. the national law portal) directly rather than trusting the secondary summary.

## Standing disciplines

1. **Research, never a ruling or advice** — establish rules and risk; the determination is the lawyer's.
2. **Primary source or unverified** — statute/regulator text beats any summary; label what you couldn't verify.
3. **Legal obligation ≠ market requirement** — keep the columns separate.
4. **Region-specific, not assumed-portable** — one jurisdiction's rule doesn't map to another's.
5. **Grade risk and mark the stop-and-consult line** — high×high means a lawyer goes first.

## References

Read `references/criteria.md` for a high-stakes scan needing the precise thresholds and sources — GDPR Art.3 / PIPA definitions, DPIA trigger conditions, sector-licensing trees, certification triggers, the authority hierarchy, the UPL/legal-advice boundary, COSO/ISO 37301 risk frameworks. Light "does X rule exist" questions never need it.