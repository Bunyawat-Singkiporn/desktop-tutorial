# 🏁 Final Review — ข้อ 5: โปรเจกต์ตะกร้า

**Difficulty:** 🔴 Challenge

---

## โจทย์

ตะกร้าเป็น list ราคา และคูปองเป็น dict

**เงื่อนไข:**

- `prices = [100, 50]`
- `coupon = {"off": 20}`
- รวมราคาแล้วหัก coupon["off"] พิมพ์ยอด

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
130
```


---

## 💡 Hint

ผสม list กับ dict

---

## Starter Code

```python
prices = [100, 50]
coupon = {"off": 20}
print(sum(prices) - coupon["off"])
```
