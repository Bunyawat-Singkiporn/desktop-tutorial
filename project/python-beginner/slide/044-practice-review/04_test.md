# 🔄 Practice Review — Question 3: Input → Store → Display

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้างโปรแกรมที่รับชื่อและคะแนน 3 คน เก็บใน list แล้วแสดงผลสรุป

**ตัวอย่าง Session:**
```
Name: Alice
Score: 85
Name: Bob
Score: 72
Name: Charlie
Score: 90
=== Results ===
Alice: 85
Bob: 72
Charlie: 90
Average: 82.3
```

---

## Starter Code

```python
records = []

for i in range(3):
    name = input("Name: ")
    score = int(input("Score: "))
    records.append((name, score))

print("=== Results ===")
# แสดงทุกคน
# คำนวณและแสดงค่าเฉลี่ย
```
