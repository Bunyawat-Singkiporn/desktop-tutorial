# 🔥 Final Review — Question 4: Mini Project Assessment

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้าง **Student Management System** โดยใช้ทุกสิ่งที่เรียนมา:

**Features:**
- `add` — เพิ่มนักเรียน (ชื่อ + คะแนน)
- `show` — แสดงทั้งหมด (ชื่อ, คะแนน, เกรด)
- `search` — ค้นหาตามชื่อ
- `stats` — แสดง average, top, bottom
- `exit` — จบ

**ต้องใช้:**
- Functions แยกส่วน
- Dictionary เก็บข้อมูล
- เกรด: A≥80, B≥70, C≥60, F<60

**ตัวอย่าง Session:**
```
Command: add
Name: Alice
Score: 88
Command: add
Name: Bob
Score: 65
Command: show
Alice: 88 (A)
Bob: 65 (C)
Command: stats
Average: 76.5
Top: Alice (88)
Bottom: Bob (65)
Command: search
Name: Alice
Found: Alice - 88 (A)
Command: exit
```

---

## Starter Code

```python
# สร้าง functions ที่จำเป็น
# เขียน main loop

students = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
