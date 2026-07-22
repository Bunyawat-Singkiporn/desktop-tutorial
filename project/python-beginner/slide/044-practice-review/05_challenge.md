# 🔥 Practice Review — Question 4: Mini Grade System

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างระบบจัดการเกรดโดยใช้ list, dict, และ functions

**Commands:** `add`, `show`, `average`, `top`, `exit`

| Function | หน้าที่ |
|----------|---------|
| `add_student(db, name, score)` | เพิ่มนักเรียน |
| `show_all(db)` | แสดงทั้งหมดพร้อมเกรด |
| `get_average(db)` | return ค่าเฉลี่ย |
| `get_top(db)` | return ชื่อคนได้สูงสุด |

**ตัวอย่าง Session:**
```
Command: add
Name: Alice
Score: 88
Command: add
Name: Bob
Score: 72
Command: show
Alice: 88 (A)
Bob: 72 (B)
Command: average
Average: 80.0
Command: top
Top: Alice (88)
Command: exit
```

---

## Starter Code

```python
def add_student(db, name, score):
    # Write your code here

def show_all(db):
    # Write your code here

def get_average(db):
    # Write your code here

def get_top(db):
    # Write your code here

db = {}
while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
