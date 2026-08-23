---
name: legal-compliance-consent-ux
description: >-
  Use when designing or reviewing a consent-collecting interface —
  cookie/consent banners, opt-in forms, or any accept/reject or checkbox
  control gating non-essential data processing. Trigger on requests like
  "cookie banner reject button placement", "pre-checked opt-in box", "쿠키 동의 배너
  검토해줘", "Accept All bundling". Do NOT use for deciding whether consent is
  even the right lawful basis (use legal-compliance-lawful-basis-selection).
metadata:
  axis: consent-mechanism-ux
  rule_count_floor: 2
---

# Consent mechanism UX

Decision rules for how a consent-collecting interface (cookie banners,
opt-in forms) must be built to be legally valid, sourced live during
issue #1174's legal-compliance research pass (2026-08-13).

## Trigger

Apply this skill when designing or reviewing a cookie/consent banner,
opt-in form, or any checkbox/toggle that gates non-essential data
processing (marketing, analytics, profiling) — distinguishing it from
sibling legal-compliance axes that govern the underlying lawful basis
(`legal-compliance-lawful-basis-selection`) or data handling after
consent is obtained (`legal-compliance-retention-minimization`), rather
than the consent-collecting interface itself.

## Procedure

1. Check the banner's accept/reject controls for equal visual
   prominence and click depth (rule 1).
2. Check that any non-essential consent checkbox/toggle initializes
   unchecked/off (rule 2).
3. Check that purpose text on the first screen names the specific
   processing purpose and rejection means in plain language (rule 3).
4. If reject is nested behind more clicks than accept, or purposes are
   bundled under one "Accept All" toggle, remove the bundling/friction
   structurally rather than adding disclosure text (rule 4).
5. Verify non-essential third-party scripts are technically blocked
   from loading until the affirmative accept act occurs (rule 5).

## Output shape

A pass/fail assessment of the reviewed consent interface against rules
1-5, naming which rule(s) are violated (if any) and the structural fix
required — not additional disclosure copy layered onto a violation.

## Decision rules

1. When designing a cookie or consent banner's accept/reject controls,
   give "Reject" the same visual prominence (size, color weight, one
   click away) as "Accept" — do not bury reject behind a secondary
   "manage preferences" screen while accept is a single primary button.
   source: GDPR Art. 7(4) via CookieYes dark-patterns guide (fetched
   2026-08-13, https://www.cookieyes.com/blog/dark-patterns-in-cookie-consent/):
   "withdrawing consent should be as easy as providing it... Rejecting
   cookies should be just as easy as accepting them."
   counter-example: a banner offering only "Accept" and "Customize" (no
   one-click "Reject All") fails this rule even if "Customize" leads to
   a reject option two steps later — the friction asymmetry itself is
   the violation, not the eventual availability of reject.

2. When a checkbox or toggle collects consent for a non-essential
   purpose (marketing, analytics, profiling), initialize it unchecked/
   off by default — never pre-tick a non-essential consent control and
   rely on the user not noticing it.
   source: GDPR Recital 32 (fetched 2026-08-13, via CookieYes summary
   https://www.cookieyes.com/blog/dark-patterns-in-cookie-consent/):
   "Silence, pre-ticked boxes or inactivity" do not constitute consent.
   counter-example: a checkbox for a purpose that is strictly-necessary
   processing (e.g. "I agree to the terms of service" required to
   create the account at all) is not a consent-basis control in the
   Art 6(1)(a) sense and is exempt from the unticked-default rule —
   necessity, not consent, is its basis.

3. When drafting the banner's purpose text, name the specific
   processing purpose and the specific means of rejecting it in plain
   language on the first screen — remove vague blanket language like
   "to improve your experience" that does not name what will actually
   happen to the data.
   source: TrueVault cookie-banner compliance guide (fetched
   2026-08-13, https://www.truevault.com/learn/keeping-your-cookie-banner-gdpr-compliant/),
   corroborated by GDPR Art. 7/Recital 32 unambiguous-indication
   standard: consent must be "informed" and the banner "must be clear
   and complete, specifying the purpose... and the means of
   rejecting."
   counter-example: none for the naming requirement itself — but a
   short banner may legitimately defer the FULL processing detail to a
   linked privacy policy, as long as the purpose category itself (not
   just a generic phrase) is stated on the banner surface.

4. When a consent flow currently nests reject behind more clicks or
   screens than accept, or bundles multiple distinct purposes behind
   one "Accept All" toggle, remove the bundling and the extra reject
   friction rather than adding more disclosure text around the existing
   flow — the fix is structural (equal friction, per-purpose toggles),
   not more copy.
   source: CNIL formal-notice action on dark-pattern cookie banners
   (fetched 2026-08-13, https://www.cnil.fr/en/dark-patterns-cookie-banners-cnil-issues-formal-notice-website-publishers),
   corroborated by the €150M Google cookie-banner fine reported in the
   CookieYes dark-patterns guide (https://www.cookieyes.com/blog/dark-patterns-in-cookie-consent/).
   counter-example: a single "Accept All" control is legitimate when
   every bundled purpose is genuinely strictly-necessary (e.g. session
   cookies required for the site to function) — bundling is only a
   violation when it merges necessary and non-essential purposes under
   one control.

5. When reviewing a consent banner implementation, verify that
   non-essential third-party scripts are technically prevented from
   loading/executing until the affirmative accept act actually
   happens — do not accept a banner where the tracker fires in the
   background as soon as the page renders and the banner is only a
   visual overlay on top of it.
   source: GDPR Recital 32 (fetched 2026-08-13,
   https://gdpr-info.eu/recitals/no-32/): "Consent should be given by a
   clear affirmative act establishing a freely given, specific,
   informed and unambiguous indication" — an act has no such effect if
   the processing it is meant to gate already started before the act
   occurred.
   counter-example: strictly-necessary scripts (session/security
   cookies) are exempt from this gating requirement by definition — the
   check applies only to the non-essential scripts already in scope for
   rules 1-4 above.
