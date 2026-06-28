# 🐍 Python Beginner — Mid-Year Cheatsheet

> สรุปสิ่งที่เรียนมา 24 สัปดาห์ — เปิดดูแล้วพอนึกออก

---

## print() — แสดงผล

```python
print("Hello, World!")       # ข้อความต้องอยู่ใน "..."
print("สวัสดี")
print("Line 1")
print("Line 2")              # แต่ละ print ขึ้นบรรทัดใหม่อัตโนมัติ

name = "Alex"
print(name)                  # แสดงค่าใน variable
print("Hello,", name)        # แสดงหลายค่า (คั่นด้วย space)
```

| วิธี | ตัวอย่าง |
|-----|---------|
| ข้อความ | `print("Hi")` |
| variable | `print(age)` |
| หลายค่า | `print("Name:", name, "Age:", age)` |

---

## input() — รับข้อมูลจากผู้ใช้

```python
name = input()               # รอผู้ใช้พิมพ์ → ได้ string เสมอ
print("Hello,", name)

age = int(input())           # รับแล้วแปลงเป็น int ทันที
next_year = age + 1

price = float(input())       # รับทศนิยม
```

**รับหลาย input** — แต่ละ `input()` รับ **1 บรรทัด**

```python
first = input()    # บรรทัดที่ 1
last = input()     # บรรทัดที่ 2
print(first, last)
```

| คำสั่ง | ได้อะไร |
|--------|--------|
| `x = input()` | string |
| `x = int(input())` | int (เอาไปคำนวณได้) |
| `x = float(input())` | float |

> ⚠️ **`input()` ได้ string เสมอ** แม้พิมพ์ตัวเลข → ต้อง `int()` / `float()` ก่อนบวกลบ

```python
age = input()        # พิมพ์ 15 → ได้ "15" (string!)
print(age + 1)       # ❌ TypeError
print(int(age) + 1)  # ✅ 16
```

---

## Comment — หมายเหตุในโค้ด

```python
# นี่คือ comment — Python ข้าม ไม่ทำงาน ไม่แสดงใน output
print("Hello")       # comment ต่อท้ายโค้ดได้

# =============================
# ชื่อโปรแกรม: คำนวณคะแนน
# ผู้เขียน: Alex
# =============================
```

| เรื่อง | จำ |
|-------|-----|
| ใช้ `#` นำหน้า | 1 บรรทัด = 1 comment |
| หลายบรรทัด | ใส่ `#` ทุกบรรทัด |
| ทำไมใช้ | อธิบายให้ **คนอ่าน** เข้าใจ (ไม่ใช่ให้คอม) |
| comment ดี | อธิบาย **ทำไม** ไม่ใช่แค่บอกว่า print อะไร |

---

## Syntax & Error — กฎการเขียน + อ่าน Error

**กฎ 3 ข้อ**

| # | กฎ | ตัวอย่าง |
|---|-----|---------|
| 1 | ตัวพิมพ์เล็ก-ใหญ่สำคัญ | `print` ✅ &nbsp; `Print` ❌ |
| 2 | เครื่องหมายครบคู่ | `(` มี `)` &nbsp; `"` มี `"` |
| 3 | ย่อหน้า (indent) | โค้ดใน `if`/`for`/`while` → **4 spaces** |

**Error ที่เจอบ่อย**

| Error | สาเหตุ | วิธีแก้ |
|-------|--------|--------|
| `SyntaxError` | วงเล็บ/เครื่องหมายไม่ครบ | ตรวจ `"` `(` ปิดครบไหม |
| `NameError` | สะกดชื่อผิด / ตัวใหญ่ผิด | `print` ไม่ใช่ `Print` |
| `IndentationError` | ย่อหน้าผิด | ลบ space ที่ไม่จำเป็น |
| `TypeError` | ชนิดข้อมูลไม่ตรงกัน | `int(input())` ก่อนคำนวณ |

> อ่าน Error ให้ดี — มันบอก **บรรทัดที่** และ **อะไรผิด**

**รันโปรแกรม:** VS Code กด ▶ หรือ `python ชื่อไฟล์.py` ใน Terminal

---

## Variable — กล่องเก็บข้อมูล

```python
name = "Alex"        # = แปลว่า "เก็บค่า" (ไม่ใช่เท่ากับคณิต)
age = 12
age = 13             # เปลี่ยนค่าได้

total = price + tax  # ใช้ variable คำนวณได้
```

| ทำได้ ✅ | ทำไม่ได้ ❌ |
|---------|-----------|
| `name = "Alex"` | `"Alex" = name` |
| เปลี่ยนค่าได้ตลอด | ค่าซ้ายต้องเป็นชื่อ variable |

**ตั้งชื่อ (snake_case)**

| ✅ | ❌ |
|----|-----|
| `my_score`, `total_price` | `MyScore`, `x`, `1score` |
| ไม่มีช่องว่าง | `first name` |
| สื่อความหมาย | `a1`, `tp` |

**ห้ามใช้เป็นชื่อ:** `if`, `else`, `for`, `while`, `print`, `input`, `True`, `False`

---

## Data Types — ชนิดข้อมูล

```python
name = "Alice"       # str   — ข้อความ (อยู่ใน "...")
age = 15             # int   — จำนวนเต็ม
price = 29.99        # float — ทศนิยม
is_open = True       # bool  — True / False (T, F ใหญ่!)
```

**ตรวจชนิด:** `type(age)` → `<class 'int'>`

**ระวัง! ตัวเลขในเครื่องหมายคำพูด**

```python
a = 5        # int
b = "5"      # str — หน้าตาเหมือนเลข แต่เป็นข้อความ!
print(a + a) # 10  (บวกเลข)
print(b + b) # 55  (ต่อข้อความ!)
```

| Type | ตัวอย่าง | ใช้กับ |
|------|---------|-------|
| `int` | `5`, `-3`, `100` | อายุ, คะแนน, นับ |
| `float` | `3.14`, `99.9` | ราคา, น้ำหนัก |
| `str` | `"hello"`, `"123"` | ข้อความทุกอย่าง |
| `bool` | `True`, `False` | เงื่อนไข |

---

## แปลงชนิด (Type Conversion)

| ฟังก์ชัน | ตัวอย่าง | ใช้เมื่อ |
|---------|---------|---------|
| `int()` | `int("15")` → `15` | รับเลขจาก input มาคำนวณ |
| `float()` | `float("3.5")` → `3.5` | รับทศนิยมจาก input |
| `str()` | `str(100)` → `"100"` | ต่อ string ด้วย `+` |

```python
age = int(input())           # รับ + แปลงในบรรทัดเดียว
message = "Score: " + str(95)
```

---

## Operators — เครื่องหมายคำนวณ

**คำนวณ**

| `+` `-` `*` `/` | `//` หารเต็ม | `%` เศษ | `**` ยกกำลัง |
|----------------|-------------|---------|-------------|
| `10 / 3` → 3.33 | `10 // 3` → 3 | `10 % 3` → 1 | `2 ** 3` → 8 |

**ลำดับคำนวณ:** `**` → `*` `/` `//` `%` → `+` `-` &nbsp; (วงเล็บ `()` ก่อนสุด)

**เปรียบเทียบ** → ได้ `True` / `False`

| `==` เท่ากับ | `!=` ไม่เท่า | `>` `<` | `>=` `<=` |
|-------------|-------------|---------|-----------|

**เลขคู่/คี่:** `n % 2 == 0` → คู่ &nbsp;|&nbsp; `n % 2 != 0` → คี่

---

## แสดงผล f-string & print options

```python
name = "Sam"
score = 95
print(f"Name: {name}, Score: {score}")   # Name: Sam, Score: 95
print(f"Average: {87.6:.1f}")            # Average: 87.6  (ทศนิยม 1 ตำแหน่ง)
print(f"Price: {99.9:.2f}")              # Price: 99.90   (ทศนิยม 2 ตำแหน่ง)
```

| วิธี | ตัวอย่าง |
|-----|---------|
| f-string ✅ | `f"Hello {name}"` |
| ต่อ string | `"Score: " + str(score)` |
| คั่นค่า | `print("A", "B", sep="-")` → `A-B` |
| ไม่ขึ้นบรรทัด | `print("Hi", end=" ")` |

---

## if / elif / else — เงื่อนไข

```python
# if / else — 2 ทาง
number = int(input())
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# if / elif / else — หลายทาง
score = int(input())
if score >= 80:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
```

> ตรวจ **จากบนลงล่าง** — เจอจริงแล้วหยุดทันที

**Logical Operators**

| `and` | ทุกข้อต้องจริง |
| `or` | จริงแค่ข้อเดียวก็พอ |
| `not` | กลับค่า True ↔ False |

```python
if age >= 12 and score >= 50:
    print("Pass")
```

---

## List — เก็บข้อมูลหลายชิ้น

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])        # Apple  (index เริ่ม 0!)
print(len(fruits))      # 3

scores = []             # list ว่าง
scores.append(85)       # เพิ่มท้าย list

for item in fruits:
    print(item)
```

| เรื่อง | ตัวอย่าง |
|-------|---------|
| สร้าง | `items = ["a", "b", "c"]` |
| เข้าถึง | `items[0]` → ตัวแรก |
| นับ | `len(items)` |
| วนซ้ำ | `for item in items:` |
| เพิ่มค่า | `items.append(ค่า)` |

---

## Loop — วนซ้ำ

### for + range

```python
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):      # 1, 2, 3, 4, 5  (หยุดก่อน 6)
    print(i)

for i in range(2, 11, 2):  # 2, 4, 6, 8, 10  (กระโดดทีละ 2)
    print(i)
```

> **`range` หยุดก่อนตัว stop** — อยากได้ 1–5 ใช้ `range(1, 6)`

### while

```python
count = 1
while count <= 5:
    print(count)
    count = count + 1    # ต้องเปลี่ยนค่า! ไม่งั้นวนไม่หยุด
```

### break / continue

| คำสั่ง | ทำอะไร |
|--------|--------|
| `break` | หยุด loop ทันที |
| `continue` | ข้ามรอบนี้ ไปรอบถัดไป |

```python
while True:
    word = input()
    if word == "quit":
        break
    print(word)
```

### Nested Loop

```python
for row in range(3):
    for col in range(4):
        print("*", end="")
    print()              # ขึ้นบรรทัดใหม่
```

> รอบรวม = นอก × ใน &nbsp; (3 × 4 = 12 ครั้ง)

---

## เลือก Loop ยังไง?

```
รู้จำนวนรอบ?  → for + range()
มี list วน?   → for item in list
วนจนเงื่อนไข? → while
หยุดกลางคัน?  → break
ข้ามบางรอบ?   → continue
```

| | `for` | `while` |
|--|-------|---------|
| ใช้เมื่อ | รู้จำนวนรอบ | วนจนเงื่อนไขเป็น False |
| ตัวอย่าง | นับ 1–10 | รับ input ซ้ำจนถูก |

---

## Bug ที่เจอบ่อย 🐛

| ปัญหา | สาเหตุ | แก้ |
|-------|--------|-----|
| Off-by-one | `range(1, 5)` ได้แค่ 1–4 | ใช้ `range(1, 6)` |
| Infinite loop | ลืม `count = count + 1` | อัปเดตตัวแปรใน while |
| พิมพ์แค่ครั้งเดียว | `print` อยู่นอก loop | ย่อหน้าให้อยู่ใน loop |
| TypeError | บวก string กับ int | `int(input())` ก่อนคำนวณ |
| แสดง list ทั้งก้อน | `print(names)` ใน loop | ใช้ `print(name)` |
| input เป็นข้อความ | ลืมแปลงชนิด | `int(input())` |

**Debug tip:** ใส่ `print(f"[debug] i = {i}")` ดูค่าในแต่ละรอบ แล้วลบออกเมื่อเสร็จ

---

## โปรแกรมตัวอย่างรวมทุกอย่าง

```python
# รับชื่อและคะแนน 3 วิชา แล้วสรุปเกรด
name = input()
scores = []

for i in range(3):
    score = int(input())
    scores.append(score)

total = 0
for s in scores:
    total = total + s

average = total / len(scores)
print(f"Name: {name}")
print(f"Average: {average:.1f}")

if average >= 80:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")
```

---

*Python Beginner — Mid-Year 2026 🏆*
