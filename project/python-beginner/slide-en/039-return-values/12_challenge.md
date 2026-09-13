# 🔥 Practice Return — Challenge: Online Food Order

**Difficulty:** 🔴 Hard

---

## Task

Build a food order system with **3 functions**:

| Function | Job |
|----------|-----|
| `get_price(menu)` | return price — `pizza`=120, `noodles`=50, else 0 |
| `calc_total(price, qty)` | return `price * qty` |
| `print_order(menu, qty, total)` | print the order |

---

## Example

**Input:**
```
pizza
2
```

**Output:**
```
=== Food Order ===
Menu: pizza
Qty: 2
Total: 240 baht
```

---

## Starter Code

```python
def get_price(menu):
    # Write your code here

def calc_total(price, qty):
    # Write your code here

def print_order(menu, qty, total):
    # Write your code here

menu = input()
qty = int(input())
price = get_price(menu)
total = calc_total(price, qty)
print_order(menu, qty, total)
```
