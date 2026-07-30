# 🏷️ Naming Rules — Rules for Naming Variables

---

## Why Do Variable Names Matter?

```python
# ❌ Hard to understand
x = 100
y = 50
print(x - y)
```

```python
# ✅ Clear right away
price = 100
discount = 50
print(price - discount)
```

> Both programs do the same thing, but good names make them readable instantly!

---

## Rules You Must Know

| Rule | ✅ Correct | ❌ Wrong |
|------|-----------|----------|
| Allowed: letters, digits, `_` | `player1`, `my_score` | `player 1`, `my-score` |
| Must not start with a digit | `score1` | `1score` |
| No spaces | `first_name` | `first name` |
| Use all lowercase | `my_name` | `MyName`, `MY_NAME` |
| Names must be meaningful | `total_price` | `tp`, `x`, `aaa` |

---

## What is Snake Case?

**snake_case** means writing multi-word names with `_` between words (like a snake slithering).

```python
# snake_case ✅ (Python style)
first_name = "Alice"
total_price = 100
player_score = 0
is_game_over = False

# camelCase ❌ (used in JavaScript, not Python)
firstName = "Alice"
totalPrice = 100
```

---

## Good Names vs Bad Names

| ❌ Bad | ✅ Good | Reason |
|--------|---------|--------|
| `n` | `name` | Too short |
| `p` | `price` | Not meaningful |
| `s1` | `student_name` | Numbers do not explain meaning |
| `MyAge` | `my_age` | Should use snake_case |
| `TOTAL` | `total` | Uppercase is only for constants |
| `data1` | `product_price` | Should say what is stored |

---

## Names You Must Not Use (Keywords)

Python has reserved words (Keywords) that you must not use as variable names:

```python
# ❌ Do not use:
if = 5       # SyntaxError
for = 10     # SyntaxError
print = "hi" # will break print()!
```

| Common Keywords |
|-----------------|
| `if`, `else`, `for`, `while` |
| `print`, `input`, `True`, `False` |

---

## Example Program with Good Names

```python
# Product data
product_name = "T-Shirt"
original_price = 500
discount_amount = 100
final_price = original_price - discount_amount

print("Product:", product_name)
print("Price:", final_price)
```

Output:
```
Product: T-Shirt
Price: 400
```
