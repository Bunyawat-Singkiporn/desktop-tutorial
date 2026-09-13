# Practice Function — Question 5: บิลซูเปอร์มาร์เก็ต + VAT

**Difficulty:** 🟡 Medium

---

## โจทย์

ทำเครื่องคิดเงินซูเปอร์มาร์เก็ต

| Function | หน้าที่ |
|----------|---------|
| `calc_total(prices)` | รวมราคาสินค้าใน list |
| `add_vat(total)` | คืนราคารวมหลัง VAT 7% |

ถามจำนวนสินค้า รับราคาทีละชิ้น แล้วแสดงยอดก่อน/หลัง VAT

---

## ตัวอย่าง Session

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
