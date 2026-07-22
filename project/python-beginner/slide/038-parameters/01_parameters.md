# 📥 Parameters — การส่งค่าเข้า Function

---

## Parameters คืออะไร?

Parameter คือ **ตัวแปรที่รับค่าจากภายนอก** เข้ามาใน function

```python
def greet(name):        # name = parameter
    print("Hello", name)

greet("Alice")          # "Alice" = argument
greet("Bob")
```

**Output:**
```
Hello Alice
Hello Bob
```

---

## หลาย Parameters

```python
def describe(name, age):
    print(f"{name} is {age} years old.")

describe("Alice", 15)
describe("Bob", 14)
```

**Output:**
```
Alice is 15 years old.
Bob is 14 years old.
```

---

## ตัวอย่าง — คำนวณ

```python
def add(a, b):
    print(a + b)

add(3, 5)   # 8
add(10, 20) # 30
```

---

## Parameter vs Argument

| คำ | ความหมาย | ตัวอย่าง |
|----|---------|---------|
| Parameter | ชื่อตัวแปรใน `def` | `def greet(name):` |
| Argument | ค่าที่ส่งตอนเรียก | `greet("Alice")` |

---

## ข้อควรระวัง

```python
def add(a, b):
    print(a + b)

add(3)        # ❌ ขาด argument
add(3, 5, 7)  # ❌ เกิน argument
add(3, 5)     # ✅ ถูกต้อง
```

---

## ตัวอย่างโปรแกรม — คำนวณ BMI

```python
def show_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.1f}")

show_bmi(60, 1.70)
show_bmi(75, 1.75)
```
