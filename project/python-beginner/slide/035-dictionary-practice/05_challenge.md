# 🔥 Practice Dictionary — Question 4: Inventory System

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างระบบสินค้าคงคลัง รองรับคำสั่ง: `add`, `update`, `remove`, `show`, `exit`

| คำสั่ง | ผล |
|--------|-----|
| `add` | เพิ่มสินค้า (ชื่อ + ราคา) |
| `update` | อัปเดตราคา |
| `remove` | ลบสินค้า |
| `show` | แสดงทั้งหมด |
| `exit` | จบ |

**ตัวอย่าง Session:**
```
Command: add
Name: Pen
Price: 15
Command: add
Name: Book
Price: 120
Command: show
Pen: 15 บาท
Book: 120 บาท
Command: update
Name: Pen
New price: 18
Command: show
Pen: 18 บาท
Book: 120 บาท
Command: exit
```

---

## Starter Code

```python
inventory = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
