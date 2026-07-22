# ⭐ Practice: Loop Review — Question 14: Star Rows with Count

**Difficulty:** 🔴 Hard

---

## โจทย์

รับ n แล้วแสดงสามเหลี่ยมดาวพร้อมบอกจำนวนดาวในแต่ละแถว

**Input:**
```
4
```

**Output:**
```
Row 1: * (1 star)
Row 2: ** (2 stars)
Row 3: *** (3 stars)
Row 4: **** (4 stars)
```

---

## 💡 Hint

- Loop นอก: แถว 1 ถึง n
- Loop ใน: สร้าง string ดาว `stars = ""` แล้ว `stars += "*"`
- แสดง `f"Row {row}: {stars} ({row} stars)"`

---

## Starter Code

```python
n = int(input())

for row in range(1, n + 1):
    stars = ""
    for j in range(row):
        # Add one star to stars
    # Print "Row row: stars (row stars)"
```
