# 🗂️ Data Types — Kinds of Data

---

## Why Learn Data Types?

Just like in real life, different things have different types:

| Real-life thing | Data Type in Python |
|-----------------|---------------------|
| Whole numbers (1, 2, 3) | `int` |
| Decimal numbers (1.5, 3.14) | `float` |
| Text ("hello") | `str` |
| True / False | `bool` |

---

## int — Whole Numbers

```python
age = 15
score = 100
temperature = -5
floor = 3
```

> Numbers without decimals. Used for: age, scores, floor numbers, counting

---

## float — Decimal Numbers

```python
price = 29.99
pi = 3.14159
weight = 55.5
height = 1.75
```

> Numbers with a decimal point. Used for: price, weight, distance

---

## str — Text (String)

```python
name = "Alice"
city = "Bangkok"
greeting = "Hello, World!"
emoji_text = "I love 🐍"
```

> Text must always be inside `"..."` quotes
> A number inside `"..."` is also a str, e.g. `"123"`

---

## bool — True or False (Boolean)

```python
is_open = True
has_discount = False
is_student = True
game_over = False
```

> Can only be `True` or `False`
> The letters `T` and `F` must be uppercase!

---

## Check the Type with `type()`

```python
age = 15
name = "Alice"
price = 29.99
is_open = True

print(type(age))      # <class 'int'>
print(type(name))     # <class 'str'>
print(type(price))    # <class 'float'>
print(type(is_open))  # <class 'bool'>
```

---

## Watch Out! Numbers Inside Quotes

```python
a = 5       # int — a number
b = "5"     # str — text that looks like a number

print(a + a)   # 10  (adds numbers)
print(b + b)   # 55  (joins text!)
```

> `"5"` is not the number 5 — it is the text "5"

---

## Summary

| Type | Examples | Used for |
|------|----------|----------|
| `int` | `5`, `-3`, `100` | Counting, age, scores |
| `float` | `3.14`, `99.9` | Price, distance |
| `str` | `"hello"`, `"123"` | All text |
| `bool` | `True`, `False` | Conditions, status |
