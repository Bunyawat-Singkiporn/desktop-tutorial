# 🧾 Practice: Loop Review — Question 7: Running Total

**Difficulty:** 🟡 Medium

---

## โจทย์

วนผ่าน list ราคา แล้วแสดงยอดสะสมหลังเพิ่มแต่ละชิ้น

```python
prices = [100, 50, 200, 75]
```

**Output:**
```
100 → total: 100
50 → total: 150
200 → total: 350
75 → total: 425
```

---

## 💡 Hint

- `total` เริ่มที่ 0
- แต่ละรอบ: `total += p` แล้วพิมพ์ทันที

---

## Starter Code

```python
prices = [100, 50, 200, 75]
total = 0

for p in prices:
    # Add p to total
    # Print "p → total: total"
```
