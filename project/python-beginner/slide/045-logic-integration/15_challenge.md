# 🧠 Logic Integration — ข้อ 15: ตะกร้าคิดส่วนลด

**Difficulty:** 🔴 Challenge

---

## โจทย์

รวมราคาสินค้า ถ้าครบ 200 ลด 20

**เงื่อนไข:**

- `prices = [80, 70, 60]`
- รวมแล้วคิดส่วนลด
- พิมพ์ `Pay: <ยอด>`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Pay: 190
```


---

## 💡 Hint

รวมก่อนแล้วค่อยลด

---

## Starter Code

```python
prices = [80, 70, 60]
total = sum(prices)
if total >= 200:
    total = total - 20
print(f"Pay: {total}")
```
