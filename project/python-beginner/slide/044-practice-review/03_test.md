# 📊 Practice Review — Question 2: Dict + Loop + Function

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง function `print_report(students)` ที่รับ dict `{name: score}` แล้วแสดงรายงานพร้อมเกรด

| คะแนน | เกรด |
|-------|------|
| >= 80 | A |
| >= 70 | B |
| >= 60 | C |
| < 60 | F |

**Output:**
```
=== Report ===
Alice: 88 → A
Bob: 72 → B
Charlie: 55 → F
```

---

## Starter Code

```python
def get_grade(score):
    # Write your code here

def print_report(students):
    print("=== Report ===")
    for name, score in students.items():
        # Write your code here

print_report({"Alice": 88, "Bob": 72, "Charlie": 55})
```
