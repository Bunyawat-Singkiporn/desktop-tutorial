# Week 6 — Quiz Feedback

## Recap Week 5

```
questions = [...]
answers = [...]

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("> ").lower()
    if user_answer == answers[i]:
        print("Correct!")
    else:
        print("Wrong! The answer is", answers[i])
```

---

## เป้าหมายวันนี้

1. เพิ่มตัวแปร `score` นับคะแนน
2. แสดง feedback ชัดขึ้น (หมายเลขข้อ + เฉลยถ้าผิด)
3. สรุปคะแนนตอนจบ

---

## ผลลัพธ์ที่จะได้

```
Question 1: What is 2 + 2?
> 4
Correct!

Question 2: What color is the sky?
> red
Wrong! The answer is blue

=== Result ===
Score: 1/2
Keep practicing!
```
