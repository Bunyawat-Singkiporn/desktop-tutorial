# 🔀 if / else — two-way conditions

---

## What is if?

`if` is used for **check conditions**

> If the condition is **True** → execute the command
> If condition is **False** → Skip.

---

## if format

```python
if conditions:
    # Commands made when a condition is true
```

---

## if/else format

```python
if conditions:
    # Do it when the condition is true.
else:
    # done when the condition is false
```

> `else` is "if none of the above is the case"

---

## Program example

```python
score = int(input())

if score >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## Sample Input / Output

| Input | Output |
|-------|--------|
| `80` | `Pass` |
| `45` | `Fail` |
| `50` | `Pass` |

---

## Precautions

- `:` must be added after `if` and `else`.
- Internal commands **must indent** (leave 4 spaces)
- `else` Unconditional — Accepts all remaining cases.
