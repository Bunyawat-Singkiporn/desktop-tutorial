# ⌨️ Input — ข้อ 14: โปรไฟล์สุขภาพ

**Difficulty:** 🔴 Challenge

---

## โจทย์

แอปสุขภาพสร้างโปรไฟล์สั้น ๆ
รับชื่อ อายุ ส่วนสูง และเมือง แล้วแสดงในกรอบ

---

## Input

4 บรรทัด — ชื่อ อายุ (จำนวนเต็ม) ส่วนสูงเมตร (ทศนิยม) เมือง

## Output

โปรไฟล์ในกรอบ

---

## ตัวอย่าง

**Input:**

```text
Earth
15
1.7
Bangkok
```

**Output:**

```text
========================
       PROFILE
========================
Name   : Earth
Age    : 15
Height : 1.7
City   : Bangkok
========================
```

---

## 💡 Hint

ส่วนสูงใช้ `float(input())` ที่เหลือเลือก `input()` หรือ `int(input())` ให้ถูกชนิด

---

## Starter Code

```python
name = input()
age = int(input())
height = float(input())
city = input()

# เขียนโค้ดตรงนี้
```
