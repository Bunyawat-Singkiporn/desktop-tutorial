# 🔥 Practice List — Question 4: To-Do Manager

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างโปรแกรม to-do ที่ผู้ใช้เลือกได้:

| คำสั่ง | ผล |
|--------|-----|
| `add` | เพิ่ม to-do ใหม่ |
| `remove` | ลบ to-do ที่ระบุ |
| `show` | แสดง to-do ทั้งหมด |
| `exit` | จบโปรแกรม |

---

## ตัวอย่าง Session

```
Command: add
Item: Buy milk
Command: add
Item: Do laundry
Command: show
1. Buy milk
2. Do laundry
Command: remove
Item: Buy milk
Command: show
1. Do laundry
Command: exit
Done!
```

---

## 💡 Hint

- ใช้ `while True:` และ `break` เพื่อออกจาก loop
- ใช้ `if command == "add":` สำหรับแต่ละคำสั่ง

---

## Starter Code

```python
todos = []

while True:
    command = input("Command: ")
    
    if command == "exit":
        print("Done!")
        break
    # Write your code here
```
