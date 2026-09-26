# 🎒 loop-with-lists — ข้อ 16: งบซื้อของโรงเรียน

**Difficulty:** 🔴 Challenge

---

## โจทย์

โรงเรียนมีงบ `budget` และรายการราคาในลิสต์
รวมราคาสินค้าทั้งหมด แล้วเทียบกับงบ
ถ้าพอซื้อ → `Status: OK` ไม่งั้น → `Status: Over Budget`

---

## Input

ไม่มี

## Output

ใบสรุปในกรอบ

---

## ตัวอย่าง

**Input:**

```text

```

**Output:**

```text
========================
       BUDGET
========================
Budget : 500
Need   : 440
Status : OK
========================
```

---

## 💡 Hint

รวมราคาใน loop ก่อน แล้วค่อย if เทียบกับ budget ทีเดียวตอนท้าย

---

## Starter Code

```python
budget = 500
prices = [120, 80, 150, 90]

# เขียนโค้ดตรงนี้
```
