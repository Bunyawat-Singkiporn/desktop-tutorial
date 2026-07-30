# 🔥 Practice: Output Formatting — Question 4: Shopping Receipt

**Difficulty:** 🔴 Hard

---

## Problem

Get customer and product data, then display a neat receipt.

**Input:**
```
Alice
Headphones
899.0
2
```

**Output:**
```
==============================
         TECH STORE
==============================
Customer : Alice
Item     : Headphones
Price    : 899.00 baht
Quantity : 2
------------------------------
Total    : 1798.00 baht
==============================
Thank you, Alice!
```

---

## 💡 Hint

- Total = price × quantity
- Use `{value:.2f}` for every number
- Align with spaces in the f-string

---

## Starter Code

```python
customer_name = input()
item_name = input()
price = float(input())
quantity = int(input())

total = price * quantity

# Print formatted receipt using f-string
```
