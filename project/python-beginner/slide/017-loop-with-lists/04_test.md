# 🏆 Practice: Loop with Lists — Question 3: Score Report

**Difficulty:** 🟡 Medium

---

## โจทย์

วนซ้ำ list คะแนนแล้วแสดงหมายเลขและคะแนนพร้อมผลลัพธ์เฉลี่ย

```python
scores = [88, 95, 72, 100, 65]
```

**Output:**
```
Student 1: 88
Student 2: 95
Student 3: 72
Student 4: 100
Student 5: 65
Average: 84.0
```

---

## 💡 Hint

- ใช้ `range(len(scores))` เพื่อได้ index
- `scores[i]` เข้าถึงค่าในแต่ละรอบ
- `i + 1` เพื่อให้นับเริ่มที่ 1

---

## Starter Code

```python
scores = [88, 95, 72, 100, 65]
total = 0

for i in range(len(scores)):
    # Print "Student X: score"
    # Add to total

# Print average
```
