# Practice Function — Medium: บิลช้อปปิ้งจาก Input

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง 2 functions:

| Function | หน้าที่ |
|----------|---------|
| `calc_total(prices)` | return ผลรวมของ list ราคา |
| `add_vat(total)` | return ราคาหลัง VAT 7% (`total * 1.07`) |

โปรแกรมหลัก:
1. ถามจำนวนสินค้า `n`
2. รับราคา `n` ครั้งเก็บใน list
3. แสดงยอดก่อน VAT และหลัง VAT

> ผสมความรู้: function + return + input + for + list + float

---

## ตัวอย่าง Session

```
How many items? 3
Price: 100
Price: 50
Price: 25
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
    price = float(input("Price: "))
    prices.append(price)

total = calc_total(prices)
print(f"Before VAT: {total}")
print(f"After VAT: {add_vat(total)}")
```
