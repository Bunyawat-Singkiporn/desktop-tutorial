# 🔥 Practice: Output Formatting — Question 4: Shopping Receipt

**Difficulty:** 🔴 Hard

---

## โจทย์

รับข้อมูลลูกค้าและสินค้า แล้วแสดงใบเสร็จสวยงาม

**Input:**
```
Alice
Headphones
899.0
2
```

**Output:**
```
==============================
         TECH STORE
==============================
Customer : Alice
Item     : Headphones
Price    : 899.00 baht
Quantity : 2
------------------------------
Total    : 1798.00 baht
==============================
Thank you, Alice!
```

---

## 💡 Hint

- Total = price × quantity
- ใช้ `{value:.2f}` สำหรับตัวเลขทุกตัว
- จัดแนวด้วย space ใน f-string

---

## Starter Code

```python
customer_name = input()
item_name = input()
price = float(input())
quantity = int(input())

total = price * quantity

# Print formatted receipt using f-string
```
