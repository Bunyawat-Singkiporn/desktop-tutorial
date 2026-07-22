# 🎯 Sets — ชุดข้อมูลที่ไม่ซ้ำ

---

## Set คืออะไร?

Set คือโครงสร้างข้อมูลที่ **ค่าจะไม่ซ้ำกัน** และ **ไม่มีลำดับแน่นอน**

---

## การสร้าง Set

```python
fruits = {"apple", "banana", "mango"}
numbers = {1, 2, 3, 4, 5}
```

> ถ้าใส่ค่าซ้ำ — Set จะลบออกให้เองอัตโนมัติ

```python
nums = {1, 2, 2, 3, 3, 3}
print(nums)  # {1, 2, 3}
```

---

## ลบค่าซ้ำจาก List

```python
data = [1, 2, 2, 3, 4, 4, 5]
unique = set(data)
print(unique)  # {1, 2, 3, 4, 5}
```

---

## .add() และ .remove()

```python
fruits = {"apple", "banana"}
fruits.add("mango")       # เพิ่ม
fruits.remove("banana")   # ลบ
print(fruits)             # {'apple', 'mango'}
```

---

## ตรวจสอบค่า

```python
fruits = {"apple", "banana", "mango"}
print("apple" in fruits)   # True
print("grape" in fruits)   # False
```

---

## Union และ Intersection

**Union `|` — รวมทั้งหมด (ไม่ซ้ำ):**
```python
a = {"A", "B", "C"}
b = {"B", "C", "D"}
print(a | b)  # {'A', 'B', 'C', 'D'}
```

**Intersection `&` — ค่าที่ซ้ำกัน:**
```python
print(a & b)  # {'B', 'C'}
```

---

## สรุป Set Methods

| คำสั่ง | หน้าที่ |
|--------|---------|
| `set(list)` | แปลง list เป็น set (ลบซ้ำ) |
| `.add(x)` | เพิ่มค่า |
| `.remove(x)` | ลบค่า |
| `x in set` | ตรวจสอบ |
| `a \| b` | Union |
| `a & b` | Intersection |
