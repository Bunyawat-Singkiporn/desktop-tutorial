# 🐛 debugging-loops — ข้อ 5: แก้รายงานยอดขาย

**Difficulty:** 🔴 Challenge

---

## โจทย์

จากยอด `[100, 50, 150]` ต้องพิมพ์ยอดทีละบรรทัด แล้ว `Total: 300` และ `Count: 3`
โค้ดเริ่มต้นผิดหลายจุด — แก้ให้ครบ

---

## Input

ไม่มี (แก้โค้ดที่ให้มา)

## Output

รายการ + Total + Count

---

## ตัวอย่าง

**Output:**

```text
100
50
150
Total: 300
Count: 3
```


---

## 💡 Hint

ตรวจทีละจุด: สิ่งที่พิมพ์ / วิธีสะสม / จุดที่นับ

---

## Starter Code

```python
sales = [100, 50, 150]
total = 0
count = 0
for sale in sales:
    print(sales)
    total = sale
print(f"Total: {total}")
print(f"Count: {count}")
```
