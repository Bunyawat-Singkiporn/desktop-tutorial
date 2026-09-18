# 📕 รันโปรแกรมและอ่าน Error — ข้อ 5: อ่าน error บอกบรรทัดที่ผิด

**Difficulty:** 🟢 Easy

---

## โจทย์

โปรแกรมหนึ่งรันแล้วขึ้นข้อความนี้

```text
  File "note.py", line 2
    print("Homework"
          ^
SyntaxError: '(' was never closed
```

จาก error บอกได้ว่า **บรรทัดที่ 2** มีปัญหาเรื่องวงเล็บไม่ปิด

เขียนโปรแกรม `note.py` ฉบับที่ถูกต้อง ให้ได้ผลลัพธ์ตามตัวอย่าง
โดยโปรแกรมมี 3 บรรทัดคือ `Today Note` , `Homework` และ `Math page 42`

---

## Input

ไม่มี

## Output

ข้อความ 3 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Today Note
Homework
Math page 42
```

---

## 💡 Hint

บรรทัดล่างสุดของ error บอก **ชนิด** ของปัญหา ส่วน `line 2` บอกว่าอยู่ **บรรทัดไหน** อ่านสองอย่างนี้ก่อนเสมอ

---

## Starter Code

```python
# เขียนโค้ดที่ถูกต้องตรงนี้
```
