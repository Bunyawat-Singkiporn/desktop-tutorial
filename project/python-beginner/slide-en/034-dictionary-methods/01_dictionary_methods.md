# ✏️ Dictionary Methods — การจัดการ Dictionary

---

## แก้ไขค่า

```python
student = {"name": "Alice", "age": 15}
student["age"] = 16           # แก้ไขค่าเดิม
print(student["age"])         # 16
```

---

## .update() — อัปเดตหลายค่าพร้อมกัน

```python
student = {"name": "Alice", "age": 15}
student.update({"age": 16, "score": 90})
print(student)
# {'name': 'Alice', 'age': 16, 'score': 90}
```

---

## del — ลบ Key

```python
student = {"name": "Alice", "age": 15, "score": 90}
del student["score"]
print(student)
# {'name': 'Alice', 'age': 15}
```

---

## .values() — ดึงค่าทั้งหมด

```python
student = {"name": "Alice", "age": 15, "score": 90}

for value in student.values():
    print(value)
```

**Output:**
```
Alice
15
90
```

---

## .items() — ดึง key และ value พร้อมกัน

```python
student = {"name": "Alice", "age": 15}

for key, value in student.items():
    print(f"{key}: {value}")
```

**Output:**
```
name: Alice
age: 15
```

---

## สรุป Methods

| Method | หน้าที่ |
|--------|---------|
| `dict["key"] = x` | แก้ไข / เพิ่ม |
| `.update({...})` | อัปเดตหลายค่า |
| `del dict["key"]` | ลบ key |
| `.values()` | ดึงค่าทั้งหมด |
| `.items()` | ดึงคู่ key-value |
