# ➕ Operators — Calculation Symbols

---

## Arithmetic Operators (number calculations)

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | add | `10 + 3` | `13` |
| `-` | subtract | `10 - 3` | `7` |
| `*` | multiply | `10 * 3` | `30` |
| `/` | divide (gives a decimal) | `10 / 3` | `3.333...` |
| `//` | floor divide (drops decimals) | `10 // 3` | `3` |
| `%` | remainder after division | `10 % 3` | `1` |
| `**` | power | `2 ** 3` | `8` |

---

## How are `/` and `//` Different?

```python
print(10 / 3)    # 3.3333333333333335  (decimal)
print(10 // 3)   # 3                   (decimals dropped)
```

> Use `//` when you only want a whole-number result

---

## % (Modulo) — Remainder After Division

```python
print(10 % 3)    # 1   (10 divided by 3 leaves remainder 1)
print(15 % 4)    # 3   (15 divided by 4 leaves remainder 3)
print(8 % 2)     # 0   (8 divided by 2 leaves remainder 0)
```

> Used a lot to check even/odd in the next lessons!

---

## Comparison Operators

The result is always `True` or `False`.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |
| `>` | greater than | `5 > 3` | `True` |
| `<` | less than | `5 < 3` | `False` |
| `>=` | greater than or equal to | `5 >= 5` | `True` |
| `<=` | less than or equal to | `3 <= 5` | `True` |

---

## Program Example

```python
price = int(input())
paid = int(input())
change = paid - price

print(f"Price: {price}")
print(f"Paid:  {paid}")
print(f"Change: {change}")
```

Input:
```
45
100
```

Output:
```
Price: 45
Paid:  100
Change: 55
```

---

## Order of Operations

Python follows order **just like math**:

| Order | Operator |
|-------|----------|
| 1 (highest) | `**` |
| 2 | `*`, `/`, `//`, `%` |
| 3 (lowest) | `+`, `-` |

```python
print(2 + 3 * 4)     # 14  (multiply first)
print((2 + 3) * 4)   # 20  (parentheses first)
```
