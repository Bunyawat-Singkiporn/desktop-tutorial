# 🔄 Type Conversion — แปลงชนิดข้อมูล

---

## ปัญหาที่พบบ่อย

`input()` คืนค่าเป็น **string เสมอ** แม้ผู้ใช้พิมพ์ตัวเลข!

```python
age = input()         # ผู้ใช้พิมพ์: 15
print(type(age))      # <class 'str'>  ← ยังเป็น string!
```

ถ้าคำนวณโดยไม่แปลง → Error!

```python
age = input()
print(age + 1)   # TypeError: can only concatenate str (not "int") to str
```

---

## วิธีแปลงชนิดข้อมูล

| ฟังก์ชัน | แปลงเป็น | ตัวอย่าง | ผลลัพธ์ |
|---------|---------|---------|--------|
| `int()` | จำนวนเต็ม | `int("15")` | `15` |
| `float()` | ทศนิยม | `float("3.5")` | `3.5` |
| `str()` | ข้อความ | `str(100)` | `"100"` |

---

## int() — แปลงเป็นจำนวนเต็ม

```python
age = int(input())      # รับ input แล้วแปลงเป็น int ทันที
next_year_age = age + 1
print("Next year:", next_year_age)
```

Input: `15`
Output: `Next year: 16`

---

## float() — แปลงเป็นทศนิยม

```python
price = float(input())
with_vat = price * 1.07    # บวก VAT 7%
print("Price with VAT:", with_vat)
```

Input: `100`
Output: `Price with VAT: 107.0`

---

## str() — แปลงเป็นข้อความ

```python
score = 95
message = "Your score is: " + str(score)  # ต้องแปลง int → str ก่อนต่อ
print(message)
```

Output: `Your score is: 95`

> ถ้าไม่ใช้ `str()` → `TypeError`

---

## แปลงในบรรทัดเดียว

```python
# รับแล้วแปลงพร้อมกันเลย
age = int(input())
price = float(input())
```

> วิธีนี้สะดวกที่สุด — ไม่ต้องแปลงแยกบรรทัด

---

## สรุป: เมื่อไหร่ใช้อะไร?

| สถานการณ์ | ใช้ |
|----------|-----|
| รับตัวเลขจาก `input()` มาคำนวณ | `int(input())` |
| รับตัวเลขทศนิยมจาก `input()` | `float(input())` |
| ต่อตัวเลขกับข้อความด้วย `+` | `str(number)` |
| รับข้อความจาก `input()` | ไม่ต้องแปลง — เป็น str อยู่แล้ว |
