# 🔥 Practice Function — Challenge: ใบรายงานผลการเรียน

**Difficulty:** 🔴 Hard

---

## โจทย์

ทำใบรายงานผลการเรียนของนักเรียน 1 คน

| Function | หน้าที่ |
|----------|---------|
| `read_scores(n)` | รับคะแนน n วิชา เป็น list |
| `average(scores)` | คืนค่าเฉลี่ย |
| `grade(avg)` | คืนเกรด A/B/C/F |
| `report(name, avg, g)` | พิมพ์ใบรายงาน |

เกรด: >=80 A, >=70 B, >=60 C, นอกนั้น F

---

## ตัวอย่าง Session

```
Name: Alice
Subjects: 3
Score: 80
Score: 90
Score: 70
=== Report Card ===
Student: Alice
Average: 80.0
Grade: A
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
