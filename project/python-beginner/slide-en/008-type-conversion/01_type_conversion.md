# 🔄 Type Conversion — Changing Data Types

---

## A Common Problem

`input()` always returns a **string**, even when the user types a number!

```python
age = input()         # user types: 15
print(type(age))      # <class 'str'>  ← still a string!
```

If you calculate without converting → Error!

```python
age = input()
print(age + 1)   # TypeError: can only concatenate str (not "int") to str
```

---

## How to Convert Data Types

| Function | Converts to | Example | Result |
|----------|-------------|---------|--------|
| `int()` | whole number | `int("15")` | `15` |
| `float()` | decimal | `float("3.5")` | `3.5` |
| `str()` | text | `str(100)` | `"100"` |

---

## int() — Convert to a Whole Number

```python
age = int(input())      # get input and convert to int right away
next_year_age = age + 1
print("Next year:", next_year_age)
```

Input: `15`
Output: `Next year: 16`

---

## float() — Convert to a Decimal

```python
price = float(input())
with_vat = price * 1.07    # add 7% VAT
print("Price with VAT:", with_vat)
```

Input: `100`
Output: `Price with VAT: 107.0`

---

## str() — Convert to Text

```python
score = 95
message = "Your score is: " + str(score)  # must convert int → str before joining
print(message)
```

Output: `Your score is: 95`

> Without `str()` → `TypeError`

---

## Convert in One Line

```python
# Get input and convert at the same time
age = int(input())
price = float(input())
```

> This is the most convenient way — no separate conversion line needed

---

## Summary: When to Use What?

| Situation | Use |
|-----------|-----|
| Get a number from `input()` to calculate | `int(input())` |
| Get a decimal from `input()` | `float(input())` |
| Join a number with text using `+` | `str(number)` |
| Get text from `input()` | No conversion needed — it is already str |
