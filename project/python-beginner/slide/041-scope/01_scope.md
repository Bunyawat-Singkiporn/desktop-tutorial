# 🔭 Scope — ขอบเขตของตัวแปร

---

## Scope คืออะไร?

Scope คือ **ขอบเขต** ที่ตัวแปรสามารถถูกเข้าถึงได้

---

## Local Variable — ตัวแปรภายใน

ตัวแปรที่สร้าง **ใน function** — ใช้ได้เฉพาะใน function นั้น

```python
def my_func():
    x = 10          # local variable
    print(x)        # ✅ ใช้ได้

my_func()
print(x)            # ❌ NameError — x ไม่มีอยู่นอก function
```

---

## Global Variable — ตัวแปรภายนอก

ตัวแปรที่สร้าง **นอก function** — ใช้ได้ทั้งโปรแกรม

```python
name = "Alice"      # global variable

def show():
    print(name)     # ✅ อ่านได้

show()              # Alice
print(name)         # Alice
```

---

## เมื่อชื่อซ้ำกัน

```python
x = 100             # global

def test():
    x = 50          # local (คนละตัวกัน!)
    print("Inside:", x)

test()
print("Outside:", x)
```

**Output:**
```
Inside: 50
Outside: 100
```

> Python จะใช้ local ก่อนเสมอ

---

## Variable Lifetime (อายุของตัวแปร)

```python
def calc():
    result = 42     # เกิดตอน function ทำงาน
    return result   # ส่งค่ากลับก่อนหาย

value = calc()
print(value)        # 42
# result ถูกลบไปแล้ว
```

---

## global keyword (ขั้นสูง)

```python
count = 0

def add_one():
    global count    # บอกว่าใช้ตัวแปร global
    count += 1

add_one()
add_one()
print(count)        # 2
```
