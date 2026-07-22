# 📋 Lists — รายการข้อมูล

---

## List คืออะไร?

List คือโครงสร้างข้อมูลที่ใช้ **เก็บหลายค่าในตัวแปรเดียว**

แทนที่จะสร้างตัวแปรหลายตัว:
```python
name1 = "Alice"
name2 = "Bob"
name3 = "Charlie"
```

เราใช้ List แทนได้:
```python
names = ["Alice", "Bob", "Charlie"]
```

---

## การสร้าง List

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [10, "hello", True]
empty = []
```

---

## การเข้าถึงข้อมูล (Index)

Index เริ่มที่ **0** เสมอ

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # mango
print(fruits[-1])  # mango  ← ตัวสุดท้าย
print(fruits[-2])  # banana ← ตัวรองสุดท้าย
```

---

## len() — นับจำนวนสมาชิก

```python
fruits = ["apple", "banana", "mango"]
print(len(fruits))  # 3
```

---

## วนซ้ำด้วย for loop

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
mango
```

---

## ตัวอย่างโปรแกรม — รวมคะแนน

```python
scores = [85, 90, 78, 92, 88]
total = 0

for score in scores:
    total += score

print("Total:", total)
```

---

## ตัวอย่าง Index

| Index | -3 | -2 | -1 |
|-------|----|----|----|
| ค่า | `"apple"` | `"banana"` | `"mango"` |
| **Index** | **0** | **1** | **2** |
