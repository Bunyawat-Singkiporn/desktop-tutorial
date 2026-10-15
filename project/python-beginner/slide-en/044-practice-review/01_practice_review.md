♪ practice review

---

♪ All that learning ♪

▪ Comment ▪
•--------------------
^ Lists ^ Keep multiple values, index, log, metods
^Tuples ^ Static Information, mmmutt
^Sts ^
^ Dictionary ^ key-value, metods ^
□ Funactions
♫ Scope ♫ local vs globe ♫
▪ Debugging
♫ Readability ♫ clean code, naming, comments ♫

---

¶ Example all topics ¶

```python
def get_average(scores):
    """คำนวณค่าเฉลี่ยจาก list ของคะแนน"""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def get_grade(average):
    """แปลงค่าเฉลี่ยเป็นเกรด"""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

# โปรแกรมหลัก
student_scores = {"Alice": [85, 90, 78],
                  "Bob": [72, 68, 75]}

for name, scores in student_scores.items():
    avg = get_average(scores)
    grade = get_grade(avg)
    print(f"{name}: {avg:.1f} → {grade}")
```---

♪ A little review

1. Read code by line.
Two: Hand-strace
3. If you find a bg . . . . .
If code run is wrong, check log
