# 📊 Logic Integration — Question 3: Dict + Loop + Conditions

**Difficulty:** 🟡 Medium

---

## Problem

Given a collection of products and prices, display only products with a **price <= 20**, labeling each one as `"Cheap"` or `"Fair"`.

| Price | Label |
|-------|-------|
| <= 10 | `Cheap` |
| 11-20 | `Fair` |
| > 20 | (Do not display) |

```python
prices = {"apple": 15, "banana": 8, "mango": 35, "kiwi": 10, "orange": 22}
```

**Output:**
```
apple: 15 → Fair
banana: 8 → Cheap
kiwi: 10 → Cheap
```

---

## Starter Code

```python
prices = {"apple": 15, "banana": 8, "mango": 35, "kiwi": 10, "orange": 22}

for item, price in prices.items():
    # Write your code here
```
