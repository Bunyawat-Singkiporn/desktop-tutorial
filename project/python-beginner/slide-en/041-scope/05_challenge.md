# 🔥 Practice Scope — Question 4: Config and Compute

**Difficulty:** 🔴 Hard

---

## Problem

Build a price calculator that uses:
- `TAX_RATE = 0.07` — global config
- function `calculate_price(base_price)` — uses local variables for the calculation, then returns the final price
- function `show_receipt(item, price)` — displays a receipt line

**Output:**
```
=== Receipt ===
Coffee: 32.1 baht
Cake: 85.6 baht
Total: 117.7 baht
```

(Prices before tax: Coffee=30, Cake=80 — 7% tax)

---

## 💡 Hint

- `calculate_price(30)` should return `30 * (1 + TAX_RATE)`
- You can use a local variable `tax_amount` inside the function

---

## Starter Code

```python
TAX_RATE = 0.07

def calculate_price(base_price):
    # Use global TAX_RATE and a local variable inside
    # Write your code here

def show_receipt(item, price):
    # Write your code here

print("=== Receipt ===")
coffee_price = calculate_price(30)
cake_price = calculate_price(80)
show_receipt("Coffee", coffee_price)
show_receipt("Cake", cake_price)
print(f"Total: {coffee_price + cake_price:.1f} baht")
```
