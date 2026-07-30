# 🏆 Practice: Mid-Year Review — Question 3: Shopping Cart

**Difficulty:** 🟡 Medium

---

## Problem

Get the product name and price repeatedly until you type `"done"` and the receipt is displayed.

**Input:**
```
Apple
15
Bread
40
Milk
35
done
```

**Output:**
```
=== Receipt ===
Apple: 15 baht
Bread: 40 baht
Milk: 35 baht
---
Total: 90 baht
```

---

## 💡 Hint

- Get the product name first if `== "done"` → `break`
- If not → get price → keep both in list.

---

## Starter Code

```python
items = []
prices = []

while True:
    name = input()
    if name == "done":
        break
    # Get price and store both name and price

print("=== Receipt ===")
# Print each item with price
print("---")
# Print total
```
