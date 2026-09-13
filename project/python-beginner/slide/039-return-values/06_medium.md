# Practice Return Values — Medium: เกรดจาก Input

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง function `get_grade(score)` ที่ **return** เกรด:

| คะแนน | เกรด |
|-------|------|
| >= 80 | `A` |
| >= 70 | `B` |
| >= 60 | `C` |
| < 60  | `F` |

โปรแกรมหลักรับคะแนนจาก `input` แล้วพิมพ์เกรด

> ผสมความรู้: return + input + int() + elif

---

## ตัวอย่าง

**Input:**
```
73
```

**Output:**
```
Grade: B
```

---

## Starter Code

```python
def get_grade(score):
    # Write your code here

score = int(input())
grade = get_grade(score)
print(f"Grade: {grade}")
```
