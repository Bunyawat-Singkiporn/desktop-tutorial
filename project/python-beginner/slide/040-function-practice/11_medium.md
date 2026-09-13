# Practice Function — Medium: รายชื่อนักเรียน

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง:
- `add_student(students, name)` — เพิ่มชื่อลง list
- `show_students(students)` — พิมพ์ชื่อทุกคนทีละบรรทัด

รับจำนวนคน แล้วรับชื่อทีละคน แล้วแสดงรายชื่อ

> ผสมความรู้: function + list + input + for

---

## ตัวอย่าง Session

```
How many students? 3
Name: Alice
Name: Bob
Name: Cara
Alice
Bob
Cara
```

---

## Starter Code

```python
def add_student(students, name):
    # Write your code here

def show_students(students):
    # Write your code here

students = []
n = int(input("How many students? "))
for i in range(n):
    name = input("Name: ")
    add_student(students, name)

show_students(students)
```
