# 🐛 debugging-loops — ข้อ 16: แก้สรุปสต็อก

**Difficulty:** 🔴 Challenge

---

## โจทย์

จำนวนสินค้าในชั้น `[4, 0, 7, 0, 3]`
- ข้ามช่องที่เป็น 0
- รวมจำนวนที่เหลือ
- นับจำนวนชั้นที่มีของ
ต้องได้ `Shelves: 3` และ `Items: 14`
โค้ดเริ่มต้นนับศูนย์และสะสมผิด — แก้ให้ถูก

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

สองบรรทัดสรุป

---

## ตัวอย่าง

**Output:**

```text
Shelves: 3
Items: 14
```


---

## 💡 Hint

ข้ามศูนย์ก่อน แล้วค่อยนับชั้นและบวกจำนวน

---

## Starter Code

```python
stock = [4, 0, 7, 0, 3]
shelves = 0
items = 0
for qty in stock:
    shelves = shelves + 1
    items = qty
print(f"Shelves: {shelves}")
print(f"Items: {items}")
```
