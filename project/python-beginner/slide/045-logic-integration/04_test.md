# 📊 Logic Integration — Question 3: Dict + Loop + Conditions

**Difficulty:** 🟡 Medium

---

## โจทย์

กำหนดสินค้าและราคา แสดงเฉพาะสินค้าที่ **ราคา <= 20** พร้อมระบุว่า "Cheap" หรือ "Fair"

| ราคา | ระดับ |
|------|------|
| <= 10 | `Cheap` |
| 11-20 | `Fair` |
| > 20 | (ไม่แสดง) |

```python
prices = {"apple": 15, "banana": 8, "mango": 35, "kiwi": 10, "orange": 22}
```

**Output:**
```
apple: 15 → Fair
banana: 8 → Cheap
kiwi: 10 → Cheap
```

---

## Starter Code

```python
prices = {"apple": 15, "banana": 8, "mango": 35, "kiwi": 10, "orange": 22}

for item, price in prices.items():
    # Write your code here
```
