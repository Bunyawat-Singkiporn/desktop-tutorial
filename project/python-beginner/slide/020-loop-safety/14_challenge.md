# 📦 loop-safety — ข้อ 14: รับออเดอร์ข้ามรายการยกเลิก

**Difficulty:** 🔴 Challenge

---

## โจทย์

ใช้ `while True` รับชื่อสินค้า
- `"done"` → break
- `"cancel"` → continue (ไม่พิมพ์)
- อื่นๆ → พิมพ์ `Order: <ชื่อ>`
ท้ายสุดพิมพ์ `End of orders`

---

## Input

ชื่อสินค้าทีละบรรทัด จบด้วย done

## Output

Order ที่ไม่ถูกยกเลิก แล้ว End of orders

---

## ตัวอย่าง

**Input:**

```text
pen
cancel
book
done
```

**Output:**

```text
Order: pen
Order: book
End of orders
```

---

## 💡 Hint

ตรวจ done ก่อน แล้วค่อยตรวจ cancel แล้วค่อยพิมพ์

---

## Starter Code

```python
# เขียนโค้ดตรงนี้
```
