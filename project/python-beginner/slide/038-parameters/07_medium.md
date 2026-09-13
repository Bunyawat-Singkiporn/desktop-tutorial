# Practice Parameters — Question 6: บิลร้านอาหาร

**Difficulty:** 🟡 Medium

---

## โจทย์

ทำบิลร้านอาหารง่ายๆ

สร้าง `print_bill(price, qty)` ที่แสดง:
- ราคาต่อจาน
- จำนวน
- รวม = `price * qty`

รับราคาและจำนวนจาก `input` แล้วเรียก function

---

## ตัวอย่าง

**Input:**
```
45
2
```

**Output:**
```
Food Bill
Price: 45.0
Qty: 2
Total: 90.0
```

---

## Starter Code

```python
def print_bill(price, qty):
    # Write your code here

price = float(input())
qty = int(input())
print_bill(price, qty)
```
