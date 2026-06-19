# 📊 Practice: Output Formatting — Question 3: Score Report

**Difficulty:** 🟡 Medium

---

## โจทย์

รับชื่อและคะแนน 3 วิชา แล้วแสดงรายงานผลการเรียนพร้อมคะแนนเฉลี่ย

**Input:**
```
Sam
80
90
70
```

**Output:**
```
=== Score Report ===
Name: Sam
Math: 80
English: 90
Science: 70
Average: 80.00
```

---

## 💡 Hint

- เฉลี่ย = (คะแนนรวม) / 3
- ใช้ `{average:.2f}` แสดงทศนิยม 2 ตำแหน่ง

---

## Starter Code

```python
name = input()
math = int(input())
english = int(input())
science = int(input())

average = (math + english + science) / 3

# Print report using f-string
```
