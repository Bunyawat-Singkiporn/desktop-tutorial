# 🏆 Mid-Year Review — ทบทวนครึ่งปี

---

## สิ่งที่เรียนมาตลอด 24 สัปดาห์

### เดือน 1–3: พื้นฐาน

| สัปดาห์ | หัวข้อ | สิ่งสำคัญ |
|--------|--------|----------|
| 1–4 | Python, Environment, Syntax, Comments | `print()`, อ่าน Error |
| 5–8 | Variables, Naming, Data Types, Conversion | `int()`, `float()`, `str()` |
| 9–12 | Input, Formatting, Operators, Review | `input()`, f-string |

### เดือน 4: Conditions

| สัปดาห์ | หัวข้อ | สิ่งสำคัญ |
|--------|--------|----------|
| 13 | Even/Odd | `%` modulo |
| 14 | elif | เงื่อนไขหลายกรณี |
| 15 | Logical Operators | `and`, `or`, `not` |
| 16 | for Loop | `range()` |

### เดือน 5–6: Loops

| สัปดาห์ | หัวข้อ | สิ่งสำคัญ |
|--------|--------|----------|
| 17–18 | for + Lists, while Loop | `for item in list`, `while` |
| 19–20 | Loop Safety, Nested | `break`, `continue`, nested |
| 21–22 | Loop Review, Debugging | รวมทุก loop |

---

## โปรแกรมตัวอย่างที่รวมทุกอย่าง

```python
# รับชื่อและคะแนน 3 วิชา สรุปผล
name = input()
scores = []

for i in range(3):
    score = int(input())
    scores.append(score)

total = 0
for s in scores:
    total = total + s

average = total / len(scores)

print(f"Name: {name}")
print(f"Average: {average:.1f}")

if average >= 80:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")
```

---

## Checklist ก่อนจบครึ่งปี

- [ ] `print()` / `input()` / f-string ได้คล่อง
- [ ] Variable, Data Types, Type Conversion
- [ ] `if` / `elif` / `else` / logical operators
- [ ] `for` range และ list
- [ ] `while`, `break`, `continue`
- [ ] Nested loops
- [ ] Debug loop เบื้องต้นได้
