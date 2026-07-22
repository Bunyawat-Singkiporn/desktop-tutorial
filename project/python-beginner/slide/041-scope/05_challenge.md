# 🔥 Practice Scope — Question 4: Config and Compute

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างระบบคำนวณราคาที่ใช้:
- `TAX_RATE = 0.07` — global config
- function `calculate_price(base_price)` — ใช้ local variable สำหรับการคำนวณ แล้ว return ราคาสุดท้าย
- function `show_receipt(item, price)` — แสดงใบเสร็จ

**Output:**
```
=== Receipt ===
Coffee: 32.1 บาท
Cake: 85.6 บาท
Total: 117.7 บาท
```

(ราคาก่อน tax: Coffee=30, Cake=80 — tax 7%)

---

## 💡 Hint

- `calculate_price(30)` ควร return `30 * (1 + TAX_RATE)`
- ใช้ local variable `tax_amount` ข้างใน function ได้

---

## Starter Code

```python
TAX_RATE = 0.07

def calculate_price(base_price):
    # ใช้ TAX_RATE global และ local variable ข้างใน
    # Write your code here

def show_receipt(item, price):
    # Write your code here

print("=== Receipt ===")
coffee_price = calculate_price(30)
cake_price = calculate_price(80)
show_receipt("Coffee", coffee_price)
show_receipt("Cake", cake_price)
print(f"Total: {coffee_price + cake_price:.1f} บาท")
```
