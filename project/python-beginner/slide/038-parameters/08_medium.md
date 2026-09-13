# Practice Parameters — Medium: ส่วนลด

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง `apply_discount(price, percent)` ที่พิมพ์ราคาสุทธิหลังลด
สูตร: `price * (100 - percent) / 100`

รับ `price` และ `percent` จาก `input` แล้วเรียก function

> ผสมความรู้: parameter + input + float + operators

---

## ตัวอย่าง

**Input:**
```
200
10
```

**Output:**
```
Pay: 180.0
```

---

## Starter Code

```python
def apply_discount(price, percent):
    # Write your code here

price = float(input())
percent = float(input())
apply_discount(price, percent)
```
