# Practice Parameters — Question 7: วันลดราคา

**Difficulty:** 🟡 Medium

---

## โจทย์

ร้านค้ามีวันลดราคา

สร้าง `sale_price(price, percent)` ที่คำนวณราคาหลังลด:
`price * (100 - percent) / 100`

แล้วแสดงทั้งราคาเดิม ส่วนลด และราคาที่ต้องจ่าย

---

## ตัวอย่าง

**Input:**
```
200
10
```

**Output:**
```
Original: 200.0
Discount: 10%
Pay: 180.0
```

---

## Starter Code

```python
def sale_price(price, percent):
    # Write your code here

price = float(input())
percent = float(input())
sale_price(price, percent)
```
