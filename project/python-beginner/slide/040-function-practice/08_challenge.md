# 🔥 Practice Function — Challenge: เกมตอบคำถามในห้องเรียน

**Difficulty:** 🔴 Hard

---

## โจทย์

ทำเกมควิซสั้นๆ ในห้องเรียน

| Function | หน้าที่ |
|----------|---------|
| `ask(question, answer)` | ถามแล้วรับคำตอบ — ถูก return `True` |
| `show_result(score, total)` | แสดงคะแนน + ข้อความ |

กฎข้อความ:
- ได้เต็ม → `Perfect!`
- ได้ครึ่งขึ้นไป → `Good job!`
- น้อยกว่าครึ่ง → `Keep practicing!`

ถาม 3 ข้อ เก็บคะแนน

---

## ตัวอย่าง Session

```
What is 2 + 2? 4
Correct!
Capital of Thailand? Bangkok
Correct!
Color of the sky? green
Wrong!
=== Result ===
Score: 2/3
Good job!
```

---

## Starter Code

```python
def ask(question, answer):
    # Write your code here

def show_result(score, total):
    # Write your code here

score = 0
total = 3

if ask("What is 2 + 2? ", "4"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

if ask("Capital of Thailand? ", "Bangkok"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

if ask("Color of the sky? ", "blue"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("=== Result ===")
show_result(score, total)
```
