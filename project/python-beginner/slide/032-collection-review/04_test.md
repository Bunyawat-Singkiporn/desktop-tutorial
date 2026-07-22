# 📊 Practice Collection Review — Question 3: List + Set Mixed

**Difficulty:** 🟡 Medium

---

## โจทย์

ระบบเช็คชื่อ: ใช้ list เก็บรายชื่อที่เช็คมาแล้ว (อาจมีซ้ำ) และใช้ set ติดตามว่ามีใครมาแล้วบ้าง

```python
checkins = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
```

**Output:**
```
Total check-ins: 6
Unique students: 3
Most check-ins: Alice (3 times)
```

---

## 💡 Hint

- ใช้ `set(checkins)` เพื่อหาชื่อไม่ซ้ำ
- ใช้ `.count(name)` เพื่อนับจำนวนครั้ง

---

## Starter Code

```python
checkins = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

total = len(checkins)
unique = set(checkins)

# หาคนที่เช็คมาบ่อยที่สุด
```
