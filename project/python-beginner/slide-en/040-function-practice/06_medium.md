# Practice Function — Question 5: Supermarket Receipt + VAT

**Difficulty:** 🟡 Medium

---

## Task

Build a supermarket cash register.

| Function | Job |
|----------|-----|
| `calc_total(prices)` | sum item prices |
| `add_vat(total)` | total after 7% VAT |

Ask how many items, read each price, then print the receipt.

---

## Example Session

```
How many items? 3
Price: 100
Price: 50
Price: 25
=== Receipt ===
Before VAT: 175.0
After VAT: 187.25
```

---

## Starter Code

```python
def calc_total(prices):
    # Write your code here

def add_vat(total):
    # Write your code here

n = int(input("How many items? "))
prices = []
for i in range(n):
    prices.append(float(input("Price: ")))

total = calc_total(prices)
print("=== Receipt ===")
print(f"Before VAT: {total}")
print(f"After VAT: {add_vat(total)}")
```
