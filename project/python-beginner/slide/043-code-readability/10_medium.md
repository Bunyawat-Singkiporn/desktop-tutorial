# ✨ Code Readability — ข้อ 10: ค่าคงที่ค่าส่ง

**Difficulty:** 🟡 Medium

---

## โจทย์

ค่าส่งคงที่หักเมื่อยอดถึงเกณฑ์

**เงื่อนไข:**

- `SHIPPING_FEE = 40` `FREE_MIN = 300`
- รับยอดซื้อ
- ถ้า >= FREE_MIN พิมพ์ `Shipping: 0` ไม่งั้น `Shipping: 40`

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
320
```

**Output:**

```text
Shipping: 0
```


---

## 💡 Hint

เทียบกับ FREE_MIN

---

## Starter Code

```python
SHIPPING_FEE = 40
FREE_MIN = 300
total = int(input())

# ตัดสินใจค่าส่ง
```
