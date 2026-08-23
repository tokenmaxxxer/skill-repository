---
name: implementation-performance-data-structure-choice--list-membership-in-loop
---
Reviewing this dedup helper before it ships. It processes click-event
exports; a typical file is 300k-800k rows.

```python
def dedup_events(rows):
    seen = []
    out = []
    for row in rows:
        key = (row["user_id"], row["ts"], row["action"])
        if key not in seen:
            seen.append(key)
            out.append(row)
    return out
```

The author says: "Tested it on our 2k-row sample file and it finishes
instantly, lists are simpler than fancy structures, and premature
optimization is the root of all evil. No performance concern here." Is
this fine to ship as-is for the stated file sizes? Answer with a
concrete verdict and, if anything, the exact change.
