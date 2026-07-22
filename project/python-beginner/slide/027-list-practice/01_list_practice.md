# 📝 List Practice — ฝึกใช้ List

---

## ทบทวน List ที่เรียนมา

| ทักษะ | ตัวอย่าง |
|-------|---------|
| สร้าง list | `items = ["a", "b", "c"]` |
| เข้าถึงด้วย index | `items[0]`, `items[-1]` |
| วนซ้ำ | `for item in items:` |
| เพิ่มข้อมูล | `items.append("d")` |
| ลบข้อมูล | `items.remove("b")` |
| เรียงข้อมูล | `items.sort()` |

---

## Pattern ที่พบบ่อย

**กรอง (Filter) — เลือกเฉพาะที่ตรงเงื่อนไข:**
```python
numbers = [3, 15, 7, 22, 8, 30]
big = []

for n in numbers:
    if n > 10:
        big.append(n)

print(big)  # [15, 22, 30]
```

**นับ (Count) — นับจำนวนที่ตรงเงื่อนไข:**
```python
scores = [85, 45, 92, 38, 77, 61]
passed = 0

for score in scores:
    if score >= 50:
        passed += 1

print("Passed:", passed)
```

---

## ตัวอย่างโปรแกรม — รายการ To-Do

```python
todos = ["Buy food", "Do homework", "Clean room"]

print("=== My To-Do List ===")
for i in range(len(todos)):
    print(i + 1, ".", todos[i])
```

**Output:**
```
=== My To-Do List ===
1 . Buy food
2 . Do homework
3 . Clean room
```

---

## ลำดับการทำงานกับ List

```
1. สร้าง list
2. เพิ่ม / แก้ไข ข้อมูล
3. ประมวลผลด้วย loop
4. แสดงผลลัพธ์
```
