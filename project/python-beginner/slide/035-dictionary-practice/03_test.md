# ❓ Practice Dictionary — Question 2: Quiz Checker

**Difficulty:** 🟡 Medium

---

## โจทย์

กำหนดเฉลยข้อสอบ 3 ข้อ รับคำตอบจากผู้ใช้ แสดงคะแนน

```python
answers = {"q1": "A", "q2": "C", "q3": "B"}
```

**ตัวอย่าง Session:**
```
q1: A
q2: B
q3: B
Score: 2/3
```

---

## 💡 Hint

Loop ผ่าน `answers.items()` รับ input สำหรับแต่ละข้อ นับถ้าตรง

---

## Starter Code

```python
answers = {"q1": "A", "q2": "C", "q3": "B"}
score = 0

for question, correct in answers.items():
    user = input(f"{question}: ")
    # Write your code here

print(f"Score: {score}/3")
```
