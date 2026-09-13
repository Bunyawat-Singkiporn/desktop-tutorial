# 🔥 Practice Function — Challenge: ห้องสมุดยืมหนังสือ

**Difficulty:** 🔴 Hard

---

## โจทย์

ทำระบบห้องสมุดเล็กๆ ด้วย **3 functions**:

| Function | หน้าที่ |
|----------|---------|
| `add_book(books, title)` | เพิ่มชื่อหนังสือลง list |
| `count_books(books)` | return จำนวนหนังสือ |
| `show_books(books)` | แสดงรายชื่อทุกเล่ม |

รับจำนวนหนังสือ แล้วรับชื่อทีละเล่ม สุดท้ายแสดงรายการ + จำนวน

---

## ตัวอย่าง Session

```
How many books? 3
Title: Python Basics
Title: Fun Games
Title: Space Kids
=== Library ===
Python Basics
Fun Games
Space Kids
Total books: 3
```

---

## Starter Code

```python
def add_book(books, title):
    # Write your code here

def count_books(books):
    # Write your code here

def show_books(books):
    # Write your code here

books = []
n = int(input("How many books? "))
for i in range(n):
    add_book(books, input("Title: "))

print("=== Library ===")
show_books(books)
print(f"Total books: {count_books(books)}")
```
