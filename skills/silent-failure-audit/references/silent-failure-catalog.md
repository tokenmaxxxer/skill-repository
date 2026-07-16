# Silent-Failure Patterns — a catalog of error-handling anti-patterns in AI-generated code

Each pattern is a structural signature detectable by static inspection. A finding cites the pattern by name so the classification is objective, not impressionistic.

Sources: CodeMirage taxonomy (Agarwal et al., arXiv 2408.08333) marked `[codemirage]`, survey of AI-generated code bugs (Gao et al., arXiv 2512.05239) marked `[survey]`, practitioner reports marked `[field]`.

---

## Category 1: Absorption (error caught and discarded)

### empty-catch `[codemirage]`
A catch block with no body, or a body containing only whitespace/comments.

```javascript
try { await fetch('/api/data'); }
catch (e) {}  // nothing
```

### bare-return `[field]`
A catch block that returns a falsy/sentinel value without the caller checking.

```javascript
function getConfig(): Config | null {
  try { return JSON.parse(readFileSync('config.json')); }
  catch { return null; }  // every caller must check, none does
}
```

The downstream trace must show at least one call site that uses the return value without a null check.

### return-default `[field]`
A catch block that returns a default value (empty array, empty string, zero) indistinguishable from a legitimate empty result.

```python
def get_users():
    try:
        return db.query("SELECT * FROM users")
    except:
        return []  # empty result = no users OR database failure — same thing
```

The default value is the same as what a successful-but-empty operation would return, making the failure invisible.

### log-then-continue `[field]`
The error is logged but execution continues on the success path as if the operation succeeded.

```python
try:
    payment = charge_card(amount)
except Exception as e:
    logger.error(f"Payment failed: {e}")
    # continues to ship the order anyway
```

The log exists but the control flow doesn't branch — the code after the catch assumes success.

---

## Category 2: Substitution (error caught and replaced with wrong behavior)

### exception-type-replacement `[codemirage]`
An error is caught and a different exception is thrown that loses the original context (no `cause`, no wrapping, different message that doesn't reference the original).

```python
try:
    result = external_api.call()
except Exception:
    raise RuntimeError("Something went wrong")  # original error and stack trace lost
```

### silent-rollback `[field]`
A catch block attempts to undo partial work but doesn't report that the rollback itself succeeded or failed.

```typescript
try {
  await db.insert(order);
  await payment.process(order);
} catch (e) {
  await db.delete(order);  // if this also fails, nothing tells anyone
  return { success: false };  // doesn't say why, doesn't say if rollback worked
}
```

---

## Category 3: Propagation failure (error should bubble up but doesn't)

### swallowed-in-loop `[field]`
An error inside a loop is caught per-iteration, allowing the loop to continue with bad state from the failed iteration.

```javascript
for (const item of items) {
  try { await processItem(item); }
  catch (e) { continue; }  // item silently skipped, aggregate result is wrong
}
```

### no-error-boundary `[field]`
An async operation or event handler has no error handler at all — unhandled Promise rejection, no `.catch()`, no `try/catch` around `await`.

```javascript
button.onclick = async () => {
  const data = await fetch('/api');  // no .catch, no try — rejection is unhandled
  render(data);
};
```

The operation is fallible but the error has nowhere to go — it becomes an unhandled rejection.

### partial-propagation `[field]`
The error is propagated but only to an intermediate layer that also catches and absorbs it — the error never reaches a decision point.

```
Controller catches → returns { error: true }
  → Middleware catches → logs and returns 200 with generic "error occurred"
    → Client receives 200 OK with no indication of failure
```

This requires a multi-layer trace: each layer claims to "handle" the error by passing it upward, but the terminal layer absorbs it.

---

## Category 4: Deceptive handling (looks handled, isn't)

### only-happy-path-log `[field]`
A catch block logs the error with enough context to diagnose, but the log level is `debug` or `trace` in a production environment that only retains `warn` and above.

```python
except Exception as e:
    logger.debug(f"Operation failed: {e}")  # never seen in production
    return None
```

### todo-catch `[survey]`
A catch block containing a TODO/FIXME comment indicating the handler is intentionally incomplete.

```python
except TimeoutError:
    # TODO: implement retry logic
    pass
```

### catch-and-throw-same `[field]`
A catch that catches an exception and immediately throws the exact same exception — decorative error handling that adds nothing.

```java
try { doWork(); }
catch (IOException e) { throw e; }  // identical to not catching at all
```

---

## Category 5: Context loss

### stack-trace-destruction `[codemirage]`
A catch block throws a new exception without chaining the original, destroying the stack trace that leads to the root cause.

```python
except DatabaseError:
    raise AppError("Database failure")  # no `from` clause, original trace gone
```

### generic-message `[survey]`
A catch block surfaces a generic message ("An error occurred", "Something went wrong") that gives no information about what failed or how to fix it, even though the caught exception contained specifics.
