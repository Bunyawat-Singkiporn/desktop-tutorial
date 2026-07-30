# 🔗 Logical Operators — Combining Conditions

---

## Why Do We Need Them?

Sometimes one condition is not enough — we need to combine several conditions.

There are 3 main operators:

| Operator | Meaning |
|----------|---------|
| `and` | Every condition must be true |
| `or` | Only one needs to be true |
| `not` | Flip the value (True → False, False → True) |

---

## `and` — All Must Be True

```python
age = 15
score = 80

if age >= 12 and score >= 50:
    print("Pass")
```

| age | score | Result |
|-----|-------|--------|
| 15 | 80 | ✅ `Pass` |
| 10 | 80 | ❌ not shown |
| 15 | 30 | ❌ not shown |

---

## `or` — One True Is Enough

```python
if score > 90 or score < 20:
    print("Special")
```

| score | Result |
|-------|--------|
| 95 | ✅ `Special` |
| 10 | ✅ `Special` |
| 50 | ❌ not shown |

---

## `not` — Flip the Value

```python
is_raining = False

if not is_raining:
    print("Go Outside")
```

| is_raining | not is_raining | Result |
|------------|----------------|--------|
| `False` | `True` | ✅ `Go Outside` |
| `True` | `False` | ❌ not shown |
