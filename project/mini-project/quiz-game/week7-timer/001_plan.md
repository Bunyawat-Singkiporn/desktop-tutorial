# Week 7 — Timed Game

## Recap Week 6

```
score = 0

for i in range(len(questions)):
    print(f"\nQuestion {i + 1}: {questions[i]}")
    user_answer = input("> ").lower()
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {answers[i]}")

print(f"Score: {score}/{len(questions)}")
```

---

## เป้าหมายวันนี้

1. `import time` — นำ module มาใช้
2. จับเวลาเริ่ม/หยุดด้วย `time.time()`
3. ถ้าตอบช้าเกิน 10 วินาที → "Time's up!"

---

## ผลลัพธ์ที่จะได้

```
Question 1: What is 2 + 2?
(You have 10 seconds)
> 4
Correct! (1.2s)

Question 2: What color is the sky?
(You have 10 seconds)
> 
Time's up!
```
