# 🗂️ Collection Review — ทบทวน Collections

---

## ทั้งสามชนิด ณ ที่เดียว

```python
# List — เรียงลำดับ, แก้ไขได้, ซ้ำได้
students = ["Alice", "Bob", "Charlie", "Alice"]

# Tuple — เรียงลำดับ, แก้ไขไม่ได้
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# Set — ไม่เรียงลำดับ, แก้ไขได้, ไม่ซ้ำ
unique_students = {"Alice", "Bob", "Charlie"}
```

---

## การเข้าถึงข้อมูล

```python
# List และ Tuple ใช้ index ได้
print(students[0])  # Alice
print(days[0])      # Mon

# Set ไม่มี index — ต้องใช้ loop
for s in unique_students:
    print(s)
```

---

## Immutability ของ Tuple

```python
days = ("Mon", "Tue", "Wed")

# ✅ สิ่งที่ทำได้
print(days[0])       # อ่านค่าได้
for d in days:       # loop ได้
    print(d)

# ❌ สิ่งที่ทำไม่ได้
days[0] = "Sunday"   # TypeError!
days.append("Sat")   # AttributeError!
```

---

## ตัวอย่างโปรแกรมใช้ทั้งสามแบบ

```python
# ข้อมูลนักเรียน
all_students = ["Alice", "Bob", "Alice", "Charlie"]
unique = set(all_students)           # ลบซ้ำ
grade_info = ("Grade 9", "Room 3")  # ข้อมูลคงที่

print("Total entries:", len(all_students))
print("Unique students:", len(unique))
print("Class:", grade_info[0], grade_info[1])
```

---

## สรุปเปรียบเทียบ

| | List | Tuple | Set |
|-|------|-------|-----|
| สร้าง | `[1,2]` | `(1,2)` | `{1,2}` |
| index | ✅ | ✅ | ❌ |
| เพิ่ม | `.append()` | ❌ | `.add()` |
| ลบ | `.remove()` | ❌ | `.remove()` |
| ซ้ำ | ✅ | ✅ | ❌ |
