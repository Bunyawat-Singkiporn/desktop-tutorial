# ✨ Code Readability — ข้อ 11: คอมเมนต์เท่าที่จำเป็น

**Difficulty:** 🟡 Medium

---

## โจทย์

คำนวณเงินทอน พร้อมคอมเมนต์หนึ่งบรรทัดอธิบายทำไม

**เงื่อนไข:**

- รับ price และ paid
- พิมพ์ `Change: <paid-price>`

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
70
100
```

**Output:**

```text
Change: 30
```


---

## 💡 Hint

คอมเมนต์อธิบายเหตุผล ไม่ใช่พูดซ้ำโค้ด

---

## Starter Code

```python
price = int(input())
paid = int(input())
# คำนวณเงินทอนให้ลูกค้า
change = paid - price
print(f"Change: {change}")
```
