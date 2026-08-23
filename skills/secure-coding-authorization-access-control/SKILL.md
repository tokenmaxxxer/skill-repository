---
name: secure-coding-authorization-access-control
description: >-
  Use when a design or review is deciding who may act on what and where that check runs —
  choosing deny-by-default for unmatched requests, granting a new permission, picking between
  RBAC and ABAC/ReBAC, modeling a multi-tenant resource, closing a client-side-only or
  single-entry-path check, or auditing accumulated role permissions. Trigger on requests like
  "RBAC vs ABAC 뭐가 맞아", "권한 체크 어디서 해야 해", "tenant isolation for this resource", "audit these
  role grants". Do NOT use for session/credential lifecycle once identity is established (use
  secure-coding-session-authentication).
metadata:
  axis: authorization-access-control
  rule_count_floor: 8
---

# Authorization / access control

Decision rules for deciding who may act on what, and where that check
runs. Research trail: layer 1 (OWASP Authorization Cheat Sheet) plus
layer 2 (ASVS V4 "Access Control", CWE-862 Missing Authorization,
CWE-863 Incorrect Authorization).

## Trigger

Use when a design or review is deciding who may act on what and where
that check runs — choosing a default for unmatched requests, granting a
new permission, picking between RBAC and ABAC/ReBAC, modeling a
multi-tenant resource, closing a client-side-only or single-entry-path
check, or auditing accumulated role permissions. Do not use it for
session/credential lifecycle concerns once identity is already
established (that is `secure-coding-session-authentication`).

## Procedure

1. Cite rule 1 when a request reaches a point with no explicit
   access-control rule matching it, to deny by default rather than
   permit-by-omission.
2. Cite rule 2 when a permission grant is being proposed, to require it
   be explicitly justifiable rather than granted broad-then-trimmed.
3. Cite rule 3 when the system has few, stable, non-overlapping roles,
   to choose RBAC as the simplest auditable model.
4. Cite rule 4 when access depends on dynamic context (tenant ownership,
   time, device posture) rather than a fixed role, to choose ABAC/ReBAC
   over RBAC and avoid role explosion.
5. Cite rule 5 when a multi-tenant resource is being modeled, to reject
   reusing a single-tenant RBAC role set that cannot express tenant
   ownership.
6. Cite rule 6 when an authorization check currently exists only in
   client-side code, to remove reliance on it and add a server-side
   enforcement point.
7. Cite rule 7 when an endpoint is reachable through more than one entry
   path, to apply the same permission check on every path rather than
   special-casing one as trusted.
8. Cite rule 8 when a role has accumulated permissions through
   incremental grants over time, to periodically audit and remove
   grants no longer justifiable under rule 2.

## Output shape

An authorization verdict: the applicable default (deny-unless-matched),
the chosen model (RBAC vs. ABAC/ReBAC) with its justification, any
client-side-only or single-entry-path gap identified with the required
server-side fix, and — for an existing role — a permission-audit note
naming any grant that no longer clears rule 2.

## Rules

1. When no explicit access-control rule matches a request, deny it —
   "the application must always make a decision, whether implicitly or
   explicitly, to either deny or permit the requested access," and the
   default when nothing matches is deny, not permit-by-omission.
   source: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

2. When granting a permission, require that it be explicitly
   justifiable — "one should be able to explicitly justify why a
   specific permission was granted" — rather than granting broad
   defaults and trimming later; broad-then-trim reliably leaves
   over-grants unnoticed. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

3. When the system has few, stable, non-overlapping roles, choose
   RBAC — it is the simplest model to reason about and audit under
   that condition. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

4. When access depends on dynamic context (multi-tenant ownership, time
   of day, device posture) rather than a fixed role, choose ABAC/ReBAC
   over RBAC — "ABAC greatly expands both the number and type of
   characteristics that can be considered," and RBAC forced into this
   shape produces role explosion. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

5. When a multi-tenant resource is being modeled, do not reuse a
   single-tenant RBAC role set — "RBAC is poorly suited for use cases
   where distinct organizations or customers will need access,"
   because a role alone cannot express "this instance belongs to
   org X." source:
   https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

6. When an authorization check currently exists only in client-side
   code (hidden UI elements, disabled buttons), **REMOVE** reliance on
   that check and add a server-side (or gateway/serverless-function)
   enforcement point — "access control checks must be performed
   server-side... client-side validation... is often easy to bypass."
   source: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

7. When an endpoint is reachable through more than one entry path (REST
   handler, AJAX handler, internal server-to-server call), apply the
   same permission check on every path — "permission should be
   validated correctly on every request, regardless of whether the
   request was initiated by an AJAX script, server-side, or any other
   source." An endpoint that special-cases one entry path as
   "internal, trusted" is the recurring root cause behind CWE-862.
   source: https://cwe.mitre.org/data/definitions/862.html

8. When a role accumulates permissions over time through incremental
   grants (a new feature adds "just one more" permission to an existing
   role), periodically audit and **REMOVE** grants no longer justifiable
   under rule 2 — role explosion and permission creep are the same
   failure observed at different time scales, and neither self-corrects
   without an explicit removal pass. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
</content>
