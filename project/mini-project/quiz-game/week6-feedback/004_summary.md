## เป้าหมาย

แสดงสรุปคะแนนตอนจบ

---

## แนวคิด

หลังออกจาก loop → แสดง score และ message ตามผลลัพธ์

```
score == 5  →  "Perfect!"
score >= 3  →  "Good job!"
score < 3   →  "Keep practicing!"
```

---

## ตัวอย่าง

```python
print("\n=== Result ===")
print(f"Score: {score}/{len(questions)}")
if score == len(questions):
    print("Perfect!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
```

---

## 📝 เพิ่มใน quiz.py

เพิ่ม **หลัง for loop** (ไม่มี indent):

```python
print("\n=== Result ===")
print(f"Score: {score}/{len(questions)}")
if score == len(questions):
    print("Perfect!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
```

> รันทดสอบ — ควรแสดงสรุปหลังถามครบทุกข้อ
