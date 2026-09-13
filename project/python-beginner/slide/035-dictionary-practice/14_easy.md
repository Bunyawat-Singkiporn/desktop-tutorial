# Practice Dictionary — Question 13: มีสินค้านี้ไหม?

**Difficulty:** 🟢 Easy

---

## โจทย์

ร้านมีสินค้านี้อยู่ไหม? รับชื่อสินค้า แล้วตอบ

```python
stock = {"pen": 10, "book": 5, "eraser": 20}
```

ถ้ามี → `In stock`  
ถ้าไม่มี → `Sold out`

---

## ตัวอย่าง

**Input:**
```
pen
```

**Output:**
```
In stock
```

**Input:**
```
ruler
```

**Output:**
```
Sold out
```

---

## 💡 Hint

`if item in stock:`

---

## Starter Code

```python
stock = {"pen": 10, "book": 5, "eraser": 20}

item = input()
# Write your code here
```
