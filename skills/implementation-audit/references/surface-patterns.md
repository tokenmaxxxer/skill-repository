# Surface Patterns — a catalog of mock-like implementation patterns

When AI-generated code appears to address a requirement but doesn't actually fulfill it, the failure follows one of a finite set of recurring patterns. This catalog names them so the audit can classify a finding as "Surface, pattern: constant-return" rather than "it doesn't seem right."

Each pattern is a structural signature, not a vibes-based judgment. The signature is checkable by static inspection.

Sources: the VentureBeat, HackerNoon, and Pete Hodgson articles cited in the implementation-audit SKILL.md evidence section, plus the CodeMirage benchmark (Agarwal et al., arXiv 2408.08333) and the survey of bugs in AI-generated code (Gao et al., arXiv 2512.05239). Patterns marked `[codemirage]` are directly cataloged in the CodeMirage taxonomy; patterns marked `[field]` are from practitioner reports.

---

## Category 1: Logic Substitution

### constant-return `[codemirage]`
A function that should compute a result instead returns a fixed value regardless of input.

```python
def validate_password(pw: str) -> bool:
    return True  # should check length, complexity, etc.
```

**Check**: the function body contains a literal return with no computation path that references all arguments.

### identity-function `[codemirage]`
A function that should transform or validate input instead passes it through unchanged.

```python
def sanitize_input(user_input: str) -> str:
    return user_input  # no sanitization applied
```

**Check**: the function returns one of its arguments unmodified, with no transformation or conditional logic between entry and return.

### inverted-condition `[codemirage]`
A conditional branch that implements the opposite of what the requirement states — "only admins can delete" becomes `if role != 'admin': allow_delete()`.

**Check**: read the condition and the action it guards; compare to the requirement statement. If they contradict, it's inverted.

### all-paths-same-result
A function with multiple branches (if/else, switch) where every branch produces the same outcome — the branching is decorative.

```typescript
function getDiscount(userType: string): number {
  if (userType === 'premium') { return 0.1; }
  else if (userType === 'basic') { return 0.1; }
  else { return 0.1; }
}
```

**Check**: compute the result for each branch; if all are identical, the function is a dressed-up constant-return.

---

## Category 2: Placeholder Infrastructure

### stub-body `[field]`
A function whose body is a placeholder — `pass`, `return null`, `return undefined`, `throw new Error('Not implemented')`, `// TODO`, `return Promise.resolve({})`.

**Check**: the function body is fewer than 3 lines and contains exclusively placeholder constructs with no domain logic.

### empty-catch `[codemirage]`
An error handler that catches an exception and does nothing — no logging, no retry, no user feedback, no fallback.

```python
try:
    dangerous_operation()
except Exception:
    pass
```

**Check**: the catch block contains `pass`, a bare `return`, or an empty block. A catch that merely re-throws the same exception is also empty-catch.

### comment-as-implementation `[field]`
A comment describes what the code should do, but the code that follows does not do it, or there is no code following — the comment is the only artifact.

```python
def process_payment(amount: int) -> bool:
    # Validate amount, charge card, handle decline, log transaction
    return True
```

**Check**: the body contains a comment describing behavior that the subsequent code does not implement. If the comment says "validate" and there is no validation logic, it's comment-as-implementation.

### hardcoded-config `[field]`
A value that should be configurable (environment variable, config file, database entry) is instead hardcoded as a literal in source.

```python
API_BASE_URL = "https://api.example.com"  # should be from env
TIMEOUT_SECONDS = 30  # should be configurable per environment
```

**Check**: the value appears in source as a literal; the requirement implies it should vary by environment or be operator-adjustable; no configuration reading mechanism is present.

---

## Category 3: Missing Guards

### missing-validation `[codemirage]`
A function that accepts user/external input and processes it without validating that the input conforms to expected constraints (type, range, format, length).

```python
def create_user(name: str, age: int) -> User:
    return db.insert(User(name=name, age=age))  # no validation
```

**Check**: input parameters are used in downstream operations without any intermediate check against documented constraints. If the requirement says "age must be between 0 and 150," and there is no check, it's missing-validation.

### missing-auth `[codemirage]`
An endpoint or operation that should require authentication/authorization but has no guard.

**Check**: the code path from request entry to sensitive operation has no authentication check, authorization check, or token validation — and the requirement states one should exist.

### silent-failure `[field]`
An operation that can fail (network call, file I/O, database write) is called without checking its return value or handling its error, and without propagating the failure upward.

```javascript
fetch('/api/submit', { body: data });  // no await, no .catch, no error handling
```

**Check**: an async/fallible operation is invoked; its result is neither awaited, checked, nor passed to an error handler.

---

## Category 4: Scope Evasion

### happy-path-only `[field]`
The implementation handles the primary success scenario correctly but does not handle any of the failure or edge cases implied by the requirement.

**Check**: enumerate the states the requirement implies (success, invalid input, not found, unauthorized, rate-limited, etc.). If only the success state has implementation code, it's happy-path-only. This pattern often co-occurs with missing-validation and silent-failure.

### bypass-existing `[field]`
The AI reimplements functionality that already exists in the codebase — writing a new HTTP client instead of using the project's shared `ApiService`, or rolling a custom logger rather than using the established one. The new implementation is often thinner than the existing one.

**Check**: the implementation introduces a new mechanism where the codebase already has a shared utility, service, or abstraction for the same purpose. The new code does not reference the existing one.

### over-scoped `[field]`
The AI implements more than was asked for — adding features, UI flourishes, or abstractions that were not in the specification — while leaving the core requirement under-implemented. The over-scoped parts function as a diversion.

**Check**: compare the implementation's surface area (files, functions, components created) against the specification's scope. If peripheral artifacts outnumber core artifacts, it's over-scoped. This is Ponytail's central diagnosis.
