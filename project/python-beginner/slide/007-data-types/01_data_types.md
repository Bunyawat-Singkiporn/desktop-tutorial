# 🗂️ Data Types — ชนิดของข้อมูล

---

## ทำไมต้องรู้ชนิดข้อมูล?

เหมือนในชีวิตจริง ของแต่ละอย่างมีประเภทต่างกัน:

| ของในชีวิตจริง | Data Type ใน Python |
|--------------|-------------------|
| จำนวนเต็ม (1, 2, 3) | `int` |
| ตัวเลขทศนิยม (1.5, 3.14) | `float` |
| ข้อความ ("hello") | `str` |
| จริง/เท็จ | `bool` |

---

## int — จำนวนเต็ม

```python
age = 15
score = 100
temperature = -5
floor = 3
```

> ตัวเลขไม่มีทศนิยม ใช้สำหรับ: อายุ, คะแนน, จำนวนชั้น, นับของ

---

## float — จำนวนทศนิยม

```python
price = 29.99
pi = 3.14159
weight = 55.5
height = 1.75
```

> ตัวเลขมีจุดทศนิยม ใช้สำหรับ: ราคา, น้ำหนัก, ระยะทาง

---

## str — ข้อความ (String)

```python
name = "Alice"
city = "Bangkok"
greeting = "Hello, World!"
emoji_text = "I love 🐍"
```

> ข้อความต้องอยู่ในเครื่องหมาย `"..."` เสมอ
> ตัวเลขในเครื่องหมาย `"..."` ก็เป็น str เช่น `"123"`

---

## bool — จริงหรือเท็จ (Boolean)

```python
is_open = True
has_discount = False
is_student = True
game_over = False
```

> มีค่าได้แค่ `True` หรือ `False` เท่านั้น
> ตัว `T` และ `F` ต้องเป็นตัวใหญ่!

---

## ตรวจสอบชนิดด้วย `type()`

```python
age = 15
name = "Alice"
price = 29.99
is_open = True

print(type(age))      # <class 'int'>
print(type(name))     # <class 'str'>
print(type(price))    # <class 'float'>
print(type(is_open))  # <class 'bool'>
```

---

## ระวัง! ตัวเลขในเครื่องหมายคำพูด

```python
a = 5       # int — ตัวเลข
b = "5"     # str — ข้อความที่หน้าตาเหมือนเลข

print(a + a)   # 10  (บวกเลข)
print(b + b)   # 55  (ต่อข้อความ!)
```

> `"5"` ไม่ใช่เลข 5 — มันคือข้อความ "5"

---

## สรุป

| Type | ตัวอย่าง | ใช้กับ |
|------|---------|-------|
| `int` | `5`, `-3`, `100` | การนับ, อายุ, คะแนน |
| `float` | `3.14`, `99.9` | ราคา, ระยะทาง |
| `str` | `"hello"`, `"123"` | ข้อความทุกอย่าง |
| `bool` | `True`, `False` | เงื่อนไข, สถานะ |
