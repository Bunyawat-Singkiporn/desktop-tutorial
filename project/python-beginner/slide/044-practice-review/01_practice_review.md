# 🏋️ Practice Review — ทบทวนรวม

---

## สิ่งที่เรียนมาทั้งหมด (Lessons 025–043)

| หัวข้อ | แนวคิดหลัก |
|--------|-----------|
| Lists | เก็บหลายค่า, index, loop, methods |
| Tuples | ข้อมูลคงที่, immutable |
| Sets | ค่าไม่ซ้ำ, union, intersection |
| Dictionaries | key-value, methods |
| Functions | def, parameters, return |
| Scope | local vs global |
| Debugging | Syntax, Runtime, Logic errors |
| Readability | clean code, naming, comments |

---

## ตัวอย่างรวมทุกหัวข้อ

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
```

---

## เคล็ดลับทบทวน

1. อ่านโค้ดทีละบรรทัด
2. ไล่ค่าตัวแปรด้วยมือ (trace)
3. ถ้าเจอ bug → ใช้ print ตรวจ
4. ถ้าโค้ดรันได้แต่ผิด → ตรวจ logic
