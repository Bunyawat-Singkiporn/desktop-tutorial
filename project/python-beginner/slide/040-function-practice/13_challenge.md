# 🔥 Practice Function — Challenge: ระบบเกรดนักเรียน

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างระบบเกรดจาก input:

| Function | หน้าที่ |
|----------|---------|
| `read_scores(n)` | รับคะแนน n ครั้ง return list |
| `average(scores)` | return ค่าเฉลี่ย |
| `grade(avg)` | return A/B/C/F |
| `report(name, avg, g)` | พิมพ์รายงาน 1 บรรทัด |

รับชื่อนักเรียน + จำนวนวิชา แล้วแสดงผล

กฎเกรด: >=80 A, >=70 B, >=60 C, นอกนั้น F

> ผสมความรู้: หลาย functions + input + list + for + elif + f-string

---

## ตัวอย่าง Session

```
Name: Alice
Subjects: 3
Score: 80
Score: 90
Score: 70
Alice | avg=80.0 | grade=A
```

---

## Starter Code

```python
def read_scores(n):
    # Write your code here

def average(scores):
    # Write your code here

def grade(avg):
    # Write your code here

def report(name, avg, g):
    # Write your code here

name = input("Name: ")
n = int(input("Subjects: "))
scores = read_scores(n)
avg = average(scores)
g = grade(avg)
report(name, avg, g)
```
