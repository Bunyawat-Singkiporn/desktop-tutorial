# Practice Return — Question 5: บัตรเกรดนักเรียน

**Difficulty:** 🟡 Medium

---

## โจทย์

ทำบัตรเกรดง่ายๆ

สร้าง `get_grade(score)` ที่ **return** เกรด:

| คะแนน | เกรด |
|-------|------|
| >= 80 | `A` |
| >= 70 | `B` |
| >= 60 | `C` |
| < 60  | `F` |

รับคะแนนจาก `input` แล้วแสดงบัตรเกรด

---

## ตัวอย่าง

**Input:**
```
73
```

**Output:**
```
Score: 73
Grade: B
```

---

## Starter Code

```python
def get_grade(score):
    # Write your code here

score = int(input())
grade = get_grade(score)
print(f"Score: {score}")
print(f"Grade: {grade}")
```
