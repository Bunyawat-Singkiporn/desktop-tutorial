# 🐛 debugging-loops — ข้อ 8: แก้พิมพ์สมาชิกทีม

**Difficulty:** 🟢 Easy

---

## โจทย์

ต้องการพิมพ์ชื่อสมาชิกทีมทีละคน แต่โค้ดพิมพ์ list ทั้งก้อนทุกรอบ

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

สามชื่อทีละบรรทัด

---

## ตัวอย่าง

**Output:**

```text
Ann
Ben
Cara
```


---

## 💡 Hint

ในลูปให้ใช้ตัวแปรวน ไม่ใช่ชื่อ list

---

## Starter Code

```python
members = ["Ann", "Ben", "Cara"]
for member in members:
    print(members)  # ← แก้ตรงนี้
```
