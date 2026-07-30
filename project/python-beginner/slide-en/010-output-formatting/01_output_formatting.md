# 🎨 Output Formatting — Formatting Display Output

---

## The Old Way of Joining Text

```python
name = "Alice"
age = 13
# Old way — messy and hard to read
print("My name is " + name + " and I am " + str(age) + " years old.")
```

---

## What is an f-string?

An **f-string** lets you put variable values directly into text — much more convenient!

```python
name = "Alice"
age = 13
print(f"My name is {name} and I am {age} years old.")
```

Output:
```
My name is Alice and I am 13 years old.
```

---

## How to Use an f-string

1. Put the letter `f` before the `"` quote
2. Put the variable inside curly braces `{}`

```python
price = 250
discount = 50
final = price - discount

print(f"Original: {price} baht")
print(f"Discount: {discount} baht")
print(f"Final:    {final} baht")
```

Output:
```
Original: 250 baht
Discount: 50 baht
Final:    200 baht
```

---

## Formatting Decimals :.2f

```python
pi = 3.14159
price = 99.9

print(f"Pi = {pi:.2f}")       # show 2 places → 3.14
print(f"Price: {price:.2f}")  # → 99.90
```

Output:
```
Pi = 3.14
Price: 99.90
```

> `:.2f` means "2 decimal places"

---

## sep= and end=

```python
# sep= sets the separator between values
print("A", "B", "C", sep="-")        # A-B-C
print("A", "B", "C", sep=" | ")      # A | B | C

# end= sets what comes at the end (default is "\n" = new line)
print("Hello", end=" ")
print("World")                        # Hello World (same line)
```

---

## Comparison: Before vs After f-strings

```python
name = "Sam"
score = 95
grade = "A"

# ❌ Old style
print("Name: " + name + " | Score: " + str(score) + " | Grade: " + grade)

# ✅ f-string
print(f"Name: {name} | Score: {score} | Grade: {grade}")
```

Same output:
```
Name: Sam | Score: 95 | Grade: A
```

---

## Summary

| Method | Example |
|--------|---------|
| `print("text", var)` | Easiest, but hard to format |
| `f"text {var}"` | ✅ Recommended — readable and flexible |
| `{var:.2f}` | 2 decimal places |
