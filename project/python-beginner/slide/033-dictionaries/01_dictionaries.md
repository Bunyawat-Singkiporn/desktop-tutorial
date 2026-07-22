# 📖 Dictionaries — ข้อมูลแบบคู่

---

## Dictionary คืออะไร?

Dictionary เก็บข้อมูลแบบ **คู่** (key → value) เหมือนพจนานุกรม

```python
student = {
    "name": "Alice",
    "age": 15,
    "score": 92
}
```

---

## การสร้าง Dictionary

```python
contact = {
    "name": "Bob",
    "phone": "081-234-5678",
    "city": "Bangkok"
}
```

---

## การเข้าถึงข้อมูล

```python
student = {"name": "Alice", "age": 15}

print(student["name"])  # Alice
print(student["age"])   # 15
```

---

## การเพิ่ม Key ใหม่

```python
student = {"name": "Alice", "age": 15}
student["score"] = 92
print(student)
# {'name': 'Alice', 'age': 15, 'score': 92}
```

---

## ตรวจสอบว่า Key มีอยู่

```python
if "name" in student:
    print("Found:", student["name"])
```

---

## วนซ้ำ (Loop)

```python
student = {"name": "Alice", "age": 15, "score": 92}

for key in student:
    print(key, ":", student[key])
```

**Output:**
```
name : Alice
age : 15
score : 92
```

---

## ตัวอย่างโปรแกรม — ข้อมูลติดต่อ

```python
contact = {
    "name": "Charlie",
    "phone": "089-111-2222"
}

print("Name:", contact["name"])
print("Phone:", contact["phone"])
```
