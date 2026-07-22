# 🔥 Practice Collection Review — Question 4: Student Tracker

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างระบบติดตามนักเรียนโดยใช้ทั้ง 3 ชนิด:

- **list** — เก็บคะแนนทั้งหมด (อาจซ้ำ)
- **set** — เก็บเกรดที่ปรากฏ (ไม่ซ้ำ)
- **tuple** — ข้อมูลห้องเรียนคงที่ (ชื่อห้อง, ปีการศึกษา)

```python
all_scores = [85, 72, 91, 85, 60, 72, 95, 88]
class_info = ("Grade 9/1", "2025")
```

**Output:**
```
Class: Grade 9/1 (2025)
Scores: [85, 72, 91, 85, 60, 72, 95, 88]
Average: 81.0
Grades given: {'A', 'B', 'C'}
Top score: 95
```

โดย grade: A=>=80, B=>=70, C=>=60, F=<60

---

## Starter Code

```python
all_scores = [85, 72, 91, 85, 60, 72, 95, 88]
class_info = ("Grade 9/1", "2025")
grades_given = set()

# Write your code here
```
