# ⌨️ Input — รับข้อมูลจากผู้ใช้

---

## input() คืออะไร?

`input()` คือคำสั่งให้โปรแกรม **หยุดรอ** รับข้อความจากผู้ใช้

```python
name = input()
print("Hello,", name)
```

```
→ โปรแกรมรอ... ผู้ใช้พิมพ์: Alex
Hello, Alex
```

---

## input() คืนค่าเป็น string เสมอ

ไม่ว่าผู้ใช้จะพิมพ์อะไร — ผลที่ได้เป็น `str` เสมอ

```python
age = input()
print(type(age))    # <class 'str'>
```

> ถ้าจะนำไปคำนวณ ต้องแปลงด้วย `int()` หรือ `float()` ก่อน

---

## รับหลาย Input

แต่ละ `input()` รับ **1 บรรทัด** จากผู้ใช้:

```python
first_name = input()
last_name = input()
print("Full name:", first_name, last_name)
```

Input:
```
Alice
Smith
```

Output:
```
Full name: Alice Smith
```

---

## รับตัวเลขและคำนวณ

```python
age = int(input())         # แปลงเป็น int ทันที
next_year = age + 1
print("Next year:", next_year)
```

Input: `14`
Output: `Next year: 15`

---

## ตัวอย่างโปรแกรมสมบูรณ์

```python
name = input()
age = int(input())

print("Name:", name)
print("Age:", age)
print("Next year:", age + 1)
```

Input:
```
Bob
14
```

Output:
```
Name: Bob
Age: 14
Next year: 15
```

---

## สรุป

| คำสั่ง | ผลลัพธ์ |
|--------|--------|
| `x = input()` | รับ string จากผู้ใช้ |
| `x = int(input())` | รับ string แล้วแปลงเป็น int |
| `x = float(input())` | รับ string แล้วแปลงเป็น float |

> **จำ:** `input()` ให้ string เสมอ — แปลงก่อนคำนวณเสมอ
