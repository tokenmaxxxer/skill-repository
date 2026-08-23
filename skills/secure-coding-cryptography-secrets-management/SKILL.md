---
name: secure-coding-cryptography-secrets-management
description: >-
  Use when you need to choose an encryption algorithm, key size, or cipher mode, or decide how a
  secret — password, token, key, credential — is created, stored, delivered to a running
  process, rotated, or removed from an image, env var, or log across its lifecycle. Trigger on
  requests like "AES 키 길이 얼마로 해", "secrets를 env var에 둬도 돼?", "how often should we rotate this
  API key", "is ECB mode acceptable here". Do NOT use for session-cookie or auth-token transport
  once a secret is a live session artifact (use secure-coding-session-authentication).
metadata:
  axis: cryptography-secrets-management
  rule_count_floor: 10
---

# Cryptography & secrets management

Decision rules for choosing algorithms/key sizes and handling secret
material through its lifecycle. Research trail: layer 1 (OWASP
Cryptographic Storage / Secrets Management Cheat Sheets) plus layer 2
(ASVS V6/V7 crypto chapters, CWE-798 Hard-coded Credentials, CWE-327
Broken/Risky Crypto).

## Trigger

Use when a proposal or review is choosing an encryption algorithm, key
size, or cipher mode, or deciding how a secret (password, token, key,
credential) is generated, stored, delivered to a running process,
rotated, or removed once it has leaked into an image or log. Do not use
it for session-cookie or auth-token transport decisions once a secret
is already a live session artifact (that is
`secure-coding-session-authentication`).

## Procedure

1. Cite rule 1 when encrypting data at rest with a symmetric cipher, to
   require AES with a key of at least 128 bits (256 preferred).
2. Cite rule 2 when public-key cryptography is required, to default to
   ECC/Curve25519 and require at least 2048-bit RSA if RSA is used
   instead.
3. Cite rule 3 when selecting a symmetric cipher mode, to prefer an
   authenticated mode and remove ECB wherever found.
4. Cite rule 4 when a proposal surfaces a custom/home-grown
   cryptographic algorithm, to remove it before it lands in favor of a
   vetted standard.
5. Cite rule 5 when storing passwords, to reject reversible encryption
   in favor of a secure password-hashing algorithm.
6. Cite rule 6 when code needs randomness for a token, key, or nonce, to
   require a CSPRNG and remove any non-cryptographic PRNG in that path.
7. Cite rule 7 when a secret needs to reach a running process, to prefer
   a vault/secret manager over an environment variable.
8. Cite rule 8 when a secret is currently baked into a Docker image via
   `ENV`/`ARG`, to remove it from the image build and inject it at
   runtime instead.
9. Cite rule 9 when scheduling rotation for a secret, to set a short
   cycle for high-risk secret classes and exempt ordinary user
   credentials from routine rotation.
10. Cite rule 10 when a secret value appears in application logs, to
    remove it from the log while preserving log integrity for
    surrounding entries.

## Output shape

A cryptography/secrets verdict: the chosen algorithm/key-size/mode with
its rule citation, the chosen secret-delivery mechanism, a rotation
cadence appropriate to the secret's risk class, and — when a secret has
already leaked into an image, env var, or log — the specific removal
step required before the finding is closed.

## Rules

1. When encrypting data at rest with a symmetric cipher, choose AES
   with a key of at least 128 bits, 256 preferred — "for symmetric
   encryption AES with a key that's at least 128 bits (ideally 256
   bits) and a secure mode should be used as the preferred algorithm."
   source: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

2. When public-key cryptography is required, choose ECC with Curve25519
   as the default; if RSA must be used instead, require a key of at
   least 2048 bits. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

3. When selecting a symmetric cipher mode, prefer an authenticated mode
   (GCM, CCM); CTR or CBC are acceptable only paired with a separate
   Encrypt-then-MAC step. **REMOVE** ECB mode wherever found outside a
   narrow documented exception — ECB leaks plaintext structure by
   design. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

4. When a proposal surfaces a custom/home-grown cryptographic algorithm,
   **REMOVE** it before it lands — the cheat sheet's guidance is
   unqualified: "don't do this." Use a vetted standard algorithm and
   library instead. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

5. When storing passwords, do not use reversible encryption — "passwords
   should not be stored using reversible encryption; secure password
   hashing algorithms should be used instead" (Argon2id/bcrypt/scrypt
   class, not a general-purpose cipher). source:
   https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

6. When code needs randomness for a token, key, or nonce, use the
   language's CSPRNG (`SecureRandom`, `crypto.randomBytes()`, the
   `secrets` module) and **REMOVE** any use of `Math.random()`/`rand()`
   in that path — non-cryptographic PRNGs are predictable and defeat
   the token's purpose even when every other control is correct.
   source: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

7. When a secret needs to reach a running process, prefer a vault/secret
   manager (sidecar injection, mounted volume, remote fetch) over an
   environment variable — env vars are "generally accessible to all
   processes and may be included in logs or system dumps... therefore
   not recommended unless the other methods are not possible." source:
   https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html

8. When a secret is currently baked into a Docker image via `ENV`/`ARG`,
   **REMOVE** it from the image build and inject it at runtime instead —
   "secrets themselves should never be hardcoded using docker ENV or
   docker ARG commands, as these can easily leak with the container
   definitions." source:
   https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html

9. When a secret's function is high-risk (API signing key, database
   root credential), schedule automated rotation on a short cycle;
   ordinary user credentials are the exception — "user credentials are
   excluded from regular rotation. These should only be rotated if
   there is suspicion or evidence that they have been compromised."
   Rotation policy is therefore per secret-class, not one blanket
   interval. source:
   https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html

10. When a secret value appears in application logs (captured
    accidentally by a debug statement or error dump), **REMOVE** it
    from the log while preserving log integrity for the surrounding
    entries — "secrets in logs must have a process for removing the
    secret while maintaining log integrity"; silently leaving it
    is treated as an unresolved exposure, not a low-priority cleanup.
    source: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
</content>
