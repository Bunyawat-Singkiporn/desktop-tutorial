# Practice Parameters — Medium: คำนวณจาก Input

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง function `show_total(price, qty)` ที่แสดงราคารวม (`price * qty`)

โปรแกรมหลัก:
1. รับ `price` และ `qty` จาก `input` (แปลงเป็นตัวเลข)
2. เรียก `show_total(price, qty)`

> ผสมความรู้: parameter + input + float/int + operators

---

## ตัวอย่าง

**Input:**
```
25.5
4
```

**Output:**
```
Total: 102.0
```

---

## Starter Code

```python
def show_total(price, qty):
    # Write your code here

price = float(input())
qty = int(input())
show_total(price, qty)
```
