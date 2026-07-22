# 📚 Final Review — Question 2: Collections

**Difficulty:** 🟡 Medium

---

## โจทย์

กำหนดข้อมูลนักเรียนเป็น list of tuples `(ชื่อ, คะแนน)`
สร้าง dict `{ชื่อ: คะแนน}` จากข้อมูลนั้น แล้วหาคนที่ไม่ซ้ำและคะแนนเฉลี่ย

```python
records = [("Alice", 85), ("Bob", 72), ("Alice", 90), ("Charlie", 68)]
```

**Output:**
```
Unique students: {'Alice', 'Bob', 'Charlie'}
Latest scores: {'Alice': 90, 'Bob': 72, 'Charlie': 68}
Average: 76.7
```

(ถ้าชื่อซ้ำให้เก็บค่าล่าสุด)

---

## Starter Code

```python
records = [("Alice", 85), ("Bob", 72), ("Alice", 90), ("Charlie", 68)]

names = set()
scores = {}

# Build names set and scores dict
# Calculate average from scores.values()
```
