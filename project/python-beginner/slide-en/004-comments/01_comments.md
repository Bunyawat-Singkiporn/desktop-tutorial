# 💬 Comments — Notes in Code

---

## What is a Comment?

A **Comment** is text in code that **Python does not read and does not run**.

Use it to explain the code so **people reading it** understand.

> Think of it like a **sticky note** 🗒️ that explains what you wrote

---

## How to Write a Comment

Put a `#` at the start:

```python
# This is a comment — Python will skip this line
print("Hello")  # you can also put a comment at the end of a line
```

Output:
```
Hello
```

> Comments **never appear** in the Output

---

## Why Use Comments?

```python
# ❌ No comment — hard to understand
x = 86400
print(x * 7)
```

```python
# ✅ With comments — clear right away
# Number of seconds in 1 day
seconds_per_day = 86400
# Calculate seconds in 1 week (7 days)
print(seconds_per_day * 7)
```

> Both programs do the same thing, but one is much easier to read!

---

## Good Comment vs Bad Comment

| ❌ Bad | ✅ Good |
|--------|---------|
| `# print hello` (says what you can already see) | `# Show a welcome message` |
| `# x = 5` | `# Product price (baht)` |
| `# this is code` | `# Calculate 7% VAT` |

> A good comment explains **why**, not just **what**

---

## Example of Good Comments

```python
# Display the shop sign header
print("====================")
print("   BEST SHOP EVER  ")   # shop name
print("====================")

# Display opening hours
print("Open: 8am - 10pm")
```

Output:
```
====================
   BEST SHOP EVER  
====================
Open: 8am - 10pm
```

---

## Multi-line Comments

```python
# =============================
# Program name: Hello World
# Author: Alex
# Date: 1 Jan 2025
# =============================
print("Hello, World!")
```

> Put `#` on every line you want to comment
