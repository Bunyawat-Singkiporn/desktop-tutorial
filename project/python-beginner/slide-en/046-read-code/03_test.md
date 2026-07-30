# 🔍 Read Code — Question 2: Trace Variables

**Difficulty:** 🟡 Medium

---

## Problem

Trace the variable values step by step and write the trace table in a comment.
Then run the code to check your answer.

```python
def mystery(items):
    count = 0
    total = 0
    for item in items:
        if item > 5:
            count += 1
            total += item
    return total, count

result = mystery([3, 8, 2, 9, 5, 7])
print(result)
```

---

## Questions

Complete the trace table:

| Iteration | item | item > 5? | count | total |
|-----------|------|-----------|-------|-------|
| 1 | 3 | False | 0 | 0 |
| 2 | 8 | True | ? | ? |
| 3 | 2 | ? | ? | ? |
| 4 | 9 | ? | ? | ? |
| 5 | 5 | ? | ? | ? |
| 6 | 7 | ? | ? | ? |

Output: ?

---

## Starter Code

```python
# Complete the trace table in a comment first

def mystery(items):
    count = 0
    total = 0
    for item in items:
        if item > 5:
            count += 1
            total += item
    return total, count

result = mystery([3, 8, 2, 9, 5, 7])
print(result)
```
