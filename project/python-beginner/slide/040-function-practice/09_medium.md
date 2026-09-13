# Practice Function — Medium: กรองคะแนนจาก Input

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง `pass_scores(scores)` ที่ return list ของคะแนน >= 50

โปรแกรมหลัก:
1. รับจำนวนคะแนน `n`
2. รับคะแนน `n` ครั้งเก็บใน list
3. พิมพ์เฉพาะคะแนนที่ผ่าน

> ผสมความรู้: function + return + input + for + list + if

---

## ตัวอย่าง Session

```
How many? 5
Score: 40
Score: 70
Score: 55
Score: 30
Score: 90
Passed: [70, 55, 90]
```

---

## Starter Code

```python
def pass_scores(scores):
    # Write your code here

n = int(input("How many? "))
scores = []
for i in range(n):
    scores.append(int(input("Score: ")))

print(f"Passed: {pass_scores(scores)}")
```
