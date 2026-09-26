# 🏦 loop-safety — ข้อ 16: ตู้ฝาก-ถอนจน quit

**Difficulty:** 🔴 Challenge

---

## โจทย์

เริ่มยอดเงิน `balance = 1000`
ใช้ `while True` รับคำสั่ง
- `"quit"` → พิมพ์ยอดคงเหลือในกรอบแล้ว break
- `"deposit"` → รับจำนวนบวกเข้า balance
- `"withdraw"` → รับจำนวน ถ้ามากกว่า balance ให้พิมพ์ `Denied` แล้ว continue (ไม่หัก)
  ถ้าน้อยกว่าหรือเท่าให้หักได้
- คำสั่งอื่น → พิมพ์ `Unknown` แล้ว continue

---

## Input

คำสั่งและจำนวนตามลำดับ จบด้วย quit

## Output

Denied ถ้ามี และกรอบยอดคงเหลือท้ายสุด

---

## ตัวอย่าง

**Input:**

```text
deposit
200
withdraw
1500
withdraw
300
quit
```

**Output:**

```text
Denied
========================
Balance: 900
========================
```

---

## 💡 Hint

แยก if ตามชนิดคำสั่ง — withdraw ที่เกินให้ continue ก่อนหัก

---

## Starter Code

```python
balance = 1000

# เขียนโค้ดตรงนี้
```
