# 🛒 Practice Dictionary — Question 3: Shopping Total

**Difficulty:** 🟡 Medium

---

## โจทย์

กำหนดราคาสินค้า รับชื่อสินค้า 3 รายการจากผู้ใช้ คำนวณรวม

```python
prices = {"apple": 15, "banana": 8, "mango": 25, "orange": 20, "kiwi": 35}
```

**ตัวอย่าง Session:**
```
Item 1: apple
Item 2: mango
Item 3: banana
apple: 15
mango: 25
banana: 8
Total: 48 บาท
```

ถ้าสินค้าไม่มีในระบบ ให้แสดง `"Not found: [ชื่อ]"` และไม่นับราคา

---

## Starter Code

```python
prices = {"apple": 15, "banana": 8, "mango": 25, "orange": 20, "kiwi": 35}
total = 0

for i in range(3):
    item = input(f"Item {i+1}: ")
    # Write your code here

print(f"Total: {total} บาท")
```
