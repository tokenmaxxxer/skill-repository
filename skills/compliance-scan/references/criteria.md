# Compliance Scan — objective criteria and their sources

Grades: ●●● primary law/official · ●●○ industry/professional standard · ●○○ blog/secondary. Always cite the primary portal (e.g. law.go.kr, eur-lex, gdpr-info) over any summary — reg summaries and AI-reconstructed statute text are frequently wrong on the deciding number/nuance.

## Applicability mapping (●○○ method)

Four axes — product × data × customer × region — intersected into a compliance matrix (rule × applies?/citation/confidence/action). No ISO standard for the method itself; rigor comes from pairing it with sector-official checklists and citing primary law per cell. Undetermined cells are flagged for legal review, not guessed. Applicability filter: does the product meet the regulator's definition → is the activity within the jurisdiction → does an exemption apply.

## Data privacy (●●●)

**GDPR Art. 3 (extraterritorial):** applies via (1) establishment in EU (processing tied to it, wherever it happens), (2) targeting EU data subjects — offering goods/services (paid or free) or monitoring their behavior; "targeting" judged by currency, local language, EU shipping, tracking/cookies (EDPB Guidelines 3/2018). Source: gdpr-info.eu/art-3, EDPB.
**Korea PIPA:** personal info = identifies a living individual, alone or *easily combined* with other info; pseudonymized info = can't identify without separately-kept additional info (keyed on re-identifiability). Source: law.go.kr, pipc.go.kr.
**DPIA triggers differ by regime:** Korea PIPA Art. 33 — mandatory for *public bodies* over thresholds (≥50k sensitive/unique-ID subjects; ≥500k linked; ≥1M total); private sector voluntary unless a specific rule requires it. GDPR Art. 35 — mandatory for anyone when processing is "high risk" (WP29's 10 criteria: profiling/automated decisions, systematic monitoring, sensitive/large-scale, matching, vulnerable subjects, new tech/biometric, etc.), review ≥ every 3 years. Never assume one maps to the other.

## Sector licensing (●●● statute / ●●○ tree)

Run the regulator's decision tree. Korea e-finance (전자금융거래법): issuing a monetary instrument (e-money) → **license**; e-funds transfer, prepaid/debit issuance, payment-gateway (PG), escrow, EBPP → **register**; regulator FSC/FSS. Medical: is the software's *intended use* diagnosis/treatment/prevention → medical device / SaMD, risk class 1-4 (Korea MFDS classification rule; FDA SaMD framework). Telecom: facilities-based (허가) vs value-added (신고) under 전기통신사업법. Always confirm current statute text at law.go.kr — fee/registration structures change.

## Certifications — mandatory vs market-driven (●●● / ●○○)

Legally mandatory for market entry, product-triggered: KC (Korea, 전기용품·생활용품 안전관리법 + 전파법 for radio), CE (EU directives — LVD/EMC/RED), FCC (US radio/electronics, Part 15; SDoC vs Certification). Market-driven (no law requires; deals/customers do): ISO 27001, SOC 2 Type II — classify as market requirement, not regulation. Sources: safetykorea.kr, kats.go.kr, fcc.gov; ISO/SOC via iso.org / AICPA (the vendor blogs on these are ●○○ marketing — cross-check).

## Platform policy (●●● source)

Apple App Store Review Guidelines (Safety/Performance/Business/Design/Legal); Google Play Policy Center. Method: tag features (payments, health data, kids, UGC, location) → map to policy sections → add region rules (EU DMA alternative marketplaces, US COPPA). Read the official guideline pages directly — AI summaries of them drift from the actual section numbers.

## Authority hierarchy (●●○)

Primary/binding: statute, regulation, constitution/treaty, settled case law. Quasi-primary: administrative rules, regulator guidance/Q&A, no-action letters, official interpretations — weak binding force but decisive for predicting enforcement. Secondary/persuasive: law-firm alerts, academic articles, trade commentary. Tertiary/folklore: blogs, wikis, forums — verify against a higher source. Always reconcile a cited article/number against the primary portal.

## Legal-advice boundary (●●○)

Research vs legal advice: stating a rule exists, quoting statute, summarizing how a regulator interpreted similar facts = research. Concluding "your product is/isn't subject to this" or "this is legal" = legal advice, reserved for a licensed attorney (US: Model Rule 5.5 / UPL; Korea: 변호사법 §109). Risk grading = likelihood (regulator activity, precedent) × severity (guidance → fine → criminal → revocation/shutdown); high×high (unlicensed financial activity, mass personal-data breach) = stop-and-consult-a-lawyer threshold, not a cleared item.

## Change tracking & risk frameworks (●●● / ●●○)

Horizon scanning: monitor legislative-notice systems (Korea 국민참여입법센터 lawmaking.go.kr, ministry boards), regulatory sandbox tracks (실증특례 = temporary regulatory exemption for a pilot; 임시허가 = provisional authorization where no standard exists; sandbox.go.kr, better.go.kr) — score impact, report on a cadence. Formal risk frameworks: COSO ERM and ISO 37301 (compliance management, PDCA structure: identify obligations → assess compliance risk → policy/objectives → monitor). Both keep the full-text procedure behind paywalls — cite the framework and, for a real assessment, obtain the standard.

## Standing caveat

Statute portals and case databases are often robots/proxy-blocked to automated fetching (observed: casenote.kr, some wikisource, lbox). When primary text can't be retrieved, mark the item "unverified — primary source not reached" and direct the user to the official portal (law.go.kr, eur-lex.europa.eu) rather than relying on the secondary summary.