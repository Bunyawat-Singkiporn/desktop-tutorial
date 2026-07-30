# 🔥 Practice: Review — Question 4: Full Receipt

**Difficulty:** 🔴 Hard

---

## Problem

Get product data and display a complete receipt with discount.

**Input:**
```
Sam
T-Shirt
299.0
3
10
```

> (customer name, item name, unit price, quantity, discount %)

**Output:**
```
================================
          FASHION STORE
================================
Customer : Sam
Item     : T-Shirt
Price    : 299.00 baht
Qty      : 3
--------------------------------
Subtotal : 897.00 baht
Discount : 89.70 baht (10%)
Total    : 807.30 baht
================================
Thank you, Sam! See you again.
```

---

## 💡 Hint

1. subtotal = price × qty
2. discount_amount = subtotal × (discount_percent / 100)
3. total = subtotal - discount_amount

---

## Starter Code

```python
customer_name = input()
item_name = input()
price = float(input())
qty = int(input())
discount_percent = int(input())

# Calculate values
subtotal = 
discount_amount = 
total = 

# Print full receipt
```
