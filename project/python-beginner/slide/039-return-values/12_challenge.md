# 🔥 Practice Return — Challenge: สั่งอาหารออนไลน์

**Difficulty:** 🔴 Hard

---

## โจทย์

ทำระบบสั่งอาหารง่ายๆ ด้วย **3 functions**:

| Function | หน้าที่ |
|----------|---------|
| `get_price(menu)` | return ราคา — `pizza`=120, `noodles`=50, อื่นๆ=0 |
| `calc_total(price, qty)` | return `price * qty` |
| `print_order(menu, qty, total)` | แสดงใบสั่งซื้อ |

รับชื่อเมนูและจำนวนจาก `input`

---

## ตัวอย่าง

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
