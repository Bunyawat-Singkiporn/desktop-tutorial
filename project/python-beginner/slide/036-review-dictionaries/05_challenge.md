# 🔥 Practice Review Dictionaries — Question 4: Grade Book

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างสมุดเกรด: เพิ่มนักเรียน อัปเดตคะแนน แสดงทั้งหมด หาคนที่ได้คะแนนสูงสุด

รับคำสั่ง: `add`, `update`, `show`, `top`, `exit`

**ตัวอย่าง Session:**
```
Command: add
Name: Alice
Score: 85
Command: add
Name: Bob
Score: 92
Command: top
Top: Bob (92)
Command: update
Name: Alice
Score: 95
Command: top
Top: Alice (95)
Command: show
Alice: 95
Bob: 92
Command: exit
```

---

## Starter Code

```python
gradebook = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
