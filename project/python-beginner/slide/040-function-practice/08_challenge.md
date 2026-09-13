# 🔥 Practice Function — Challenge: Mini Quiz

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างแบบทดสอบสั้นๆ ด้วย functions:

| Function | หน้าที่ |
|----------|---------|
| `ask(question, answer)` | ถามคำถาม รับคำตอบจาก `input` — ถูก return `True` ผิด return `False` |
| `show_result(score, total)` | แสดงคะแนนและข้อความตามผล |

กฎ `show_result`:
- ได้เต็ม → `Perfect!`
- ได้ >= ครึ่ง → `Good job!`
- น้อยกว่าครึ่ง → `Keep practicing!`

ถาม **3 ข้อ** เก็บคะแนน

> ผสมความรู้: function + return + input + if + score += 1

---

## ตัวอย่าง Session

```
What is 2 + 2? 4
Correct!
Capital of Thailand? Bangkok
Correct!
Color of the sky? green
Wrong!
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

show_result(score, total)
```
