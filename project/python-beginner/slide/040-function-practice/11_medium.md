# Practice Function — Question 9: รายชื่อเข้าค่าย

**Difficulty:** 🟡 Medium

---

## โจทย์

ครูเก็บรายชื่อเด็กเข้าค่าย

สร้าง:
- `add_name(names, name)` — เพิ่มชื่อลง list
- `show_names(names)` — แสดงรายชื่อทีละคน

ถามจำนวนคน รับชื่อ แล้วพิมพ์รายชื่อทั้งหมด

---

## ตัวอย่าง Session

```
How many campers? 3
Name: Alice
Name: Bob
Name: Cara
=== Camp List ===
Alice
Bob
Cara
```

---

## Starter Code

```python
def add_name(names, name):
    # Write your code here

def show_names(names):
    # Write your code here

names = []
n = int(input("How many campers? "))
for i in range(n):
    add_name(names, input("Name: "))

print("=== Camp List ===")
show_names(names)
```
