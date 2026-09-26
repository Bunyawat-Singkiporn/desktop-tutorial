# 💰 loop-safety — ข้อ 10: รวมเฉพาะยอดบวกจนเจอ 0

**Difficulty:** 🟡 Medium

---

## โจทย์

ใช้ `while True` รับจำนวน
ถ้าได้ `0` ให้ `break`
ถ้าได้ค่าน้อยกว่า 0 ให้ `continue` (ไม่บวก)
นอกนั้นบวกเข้า total แล้วท้ายสุดพิมพ์ผลรวม

---

## Input

จำนวนทีละบรรทัด จบด้วย 0

## Output

Total: <ผลรวมค่าบวก>

---

## ตัวอย่าง

**Input:**

```text
10
-3
5
0
```

**Output:**

```text
Total: 15
```

---

## 💡 Hint

ลำดับในลูป: รับค่า → ถ้า 0 break → ถ้าติดลบ continue → ค่อยบวก

---

## Starter Code

```python
total = 0

# เขียนโค้ดตรงนี้
```
