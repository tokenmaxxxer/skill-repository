---
name: secure-coding-input-validation-injection-defense
description: Use when untrusted input is about to cross a trust boundary — a shell, SQL query, HTML/JS/URL sink, or a validation layer — and you need to choose an allowlist, parameterization, or output-encoding approach.
axis: input-validation-injection-defense
rule_count_floor: 9
---

# Input validation / injection defense

Decision rules for validating and encoding untrusted input before it
crosses a trust boundary (parser, shell, query engine, template engine,
DOM). Research trail: layer 1 (OWASP practitioner cheat sheets) plus
layer 2 (named standard: OWASP ASVS 5.0 "Encoding and Sanitization"
chapter, CWE-20/CWE-89/CWE-78 families).

## Trigger

Use when untrusted input is about to cross a trust boundary — a shell,
SQL/query engine, HTML/JS/URL rendering sink, or a duplicated validation
layer — and a validation, parameterization, or encoding approach needs
to be chosen, or when scoping a security review pass itself. Do not use
it for authorization decisions once input has already been validated
(that is `secure-coding-authorization-access-control`).

## Procedure

1. Cite rule 1 when a field has a known finite structure, to validate
   with an allowlist regex rather than reaching for a denylist first.
2. Cite rule 2 when a denylist filter is proposed as the sole defense
   against injection, to remove it as the primary control.
3. Cite rule 3 when input is a fixed set of caller-visible options, to
   validate an exact match against the offered values.
4. Cite rule 4 when input is free-form Unicode text where legitimate
   users need special characters, to rely on context-aware output
   encoding at the sink instead of restrictive character-class
   validation.
5. Cite rule 5 when untrusted data reaches an OS shell, to choose
   parameterized OS calls/argument arrays over string-built commands.
6. Cite rule 6 when untrusted data reaches a SQL/query engine, to use
   parameterized queries or a bound-parameter ORM API, never string
   concatenation.
7. Cite rule 7 when output is rendered into HTML, JS, or a URL context,
   to apply encoding specific to that sink rather than one generic
   escaping function.
8. Cite rule 8 when a validation routine currently rejects then
   continues with a default/sanitized value for a security-relevant
   field, to remove the silent-fallback path and fail closed instead.
9. Cite rule 9 when a review finds two validation layers doing the same
   allowlist check on the same field, to remove the duplicate and keep
   validation at the trust-boundary crossing point only.
10. Cite rule 10 when conducting a security review pass, to scope it to
    changed lines and the trust boundaries they cross, triaging out
    low-signal or non-reachable matches before they reach the finding
    list.

## Output shape

An input-validation verdict: the chosen control (allowlist,
parameterization, sink-specific encoding) with its rule citation, any
denylist-only or silent-fallback path flagged for removal, and — for a
review pass — the scoped set of changed trust boundaries actually
checked with low-signal matches triaged out.

## Rules

1. When a field has a known finite structure (date, ZIP code, SSN,
   enum), validate with an **allowlist** regex that defines exactly
   what IS authorized — "allowlist validation involves defining exactly
   what IS authorized, and by definition, everything else is not
   authorized." Do not reach for a denylist first. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

2. When a denylist filter is proposed as the sole defense against
   injection, **REMOVE** it as the primary control — "it is a common
   mistake to use denylist validation... this is a massively flawed
   approach as it is trivial for an attacker to bypass such filters."
   A denylist may stay only as a supplementary layer, never the
   replacement for allowlisting. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

3. When input is a fixed set of caller-visible options (dropdown, radio,
   enum parameter), validate that the value matches exactly one of the
   values offered — free-text comparison against "looks plausible" is
   not sufficient. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

4. When input is free-form Unicode text (names, addresses, comments)
   where legitimate users need special characters, do not force
   restrictive character-class validation — rely on context-aware
   output encoding at the sink instead, because validation cannot
   distinguish a legitimate apostrophe from an attack payload.
   source: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

5. When untrusted data reaches an OS shell, choose parameterized OS
   calls / argument arrays over string-built commands with
   contextual escaping as a fallback only — ASVS's injection-prevention
   requirement is stated as "the application protects against OS
   command injection and that operating system calls use parameterized
   OS queries or use contextual command line output encoding." source:
   https://owasp.org/www-project-application-security-verification-standard/

6. When untrusted data reaches a SQL/query engine, use parameterized
   queries or an ORM's bound-parameter API — never string-concatenate
   the value into the query text, matching CWE-89's root cause
   (improper neutralization of special elements in SQL commands).
   source: https://cwe.mitre.org/data/definitions/89.html

7. When output is rendered into HTML, JS, or a URL context, apply
   encoding specific to that sink (HTML-entity, JS-string, URL-percent)
   rather than one generic escaping function — "all user data controlled
   must be encoded when returned in the HTML page to prevent the
   execution of malicious data," and a mismatched encoder (e.g. HTML
   encoding inside a `<script>` block) does not neutralize the payload.
   source: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

8. When a validation routine currently rejects then continues processing
   with a default/sanitized value, **REMOVE** the silent-fallback path
   for security-relevant fields (auth tokens, redirect targets, file
   paths) and fail closed instead — continuing on invalid input for
   these fields converts a rejected attack into a processed one under a
   different code path, defeating the allowlist rule 1 protects.
   source: https://cwe.mitre.org/data/definitions/20.html

9. When a code review finds two validation layers doing the same
   allowlist check on the same field (e.g. duplicated in controller and
   service layer with drifted regexes), **REMOVE** the duplicate and
   keep validation at the trust-boundary crossing point only — two
   independently maintained copies of the same rule diverge over time
   and the looser one becomes the actual enforced policy. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

10. When conducting a security review pass, scope it to the changed
    lines and the trust boundaries they cross rather than re-scanning
    the whole codebase on every pass, and explicitly triage out
    low-signal or non-reachable pattern matches before they reach the
    finding list instead of reporting every match — an unscoped,
    unfiltered review does not scale to the review cadence a codebase
    actually needs and buries the reachable findings under noise.
    ASVS V5.1.3.
</content>
