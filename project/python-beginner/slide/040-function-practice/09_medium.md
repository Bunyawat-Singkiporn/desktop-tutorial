# Practice Function — Question 7: ตรวจใครสอบผ่าน

**Difficulty:** 🟡 Medium

---

## โจทย์

ครูตรวจคะแนนสอบ — คะแนน >= 50 ถือว่าผ่าน

สร้าง `get_passed(scores)` ที่ return list ของคะแนนที่ผ่าน  
รับคะแนนจากผู้ใช้แล้วแสดงรายการผู้ผ่าน

---

## ตัวอย่าง Session

```
How many scores? 5
Score: 40
Score: 70
Score: 55
Score: 30
Score: 90
Passed scores: [70, 55, 90]
```

---

## Starter Code

```python
def get_passed(scores):
    # Write your code here

n = int(input("How many scores? "))
scores = []
for i in range(n):
    scores.append(int(input("Score: ")))

print(f"Passed scores: {get_passed(scores)}")
```
