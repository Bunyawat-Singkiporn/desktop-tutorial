# ✅ Practice: Loop Review — Question 3: Grade List

**Difficulty:** 🟡 Medium

---

## โจทย์

รับคะแนน 5 ครั้ง แล้วแสดงเกรดของแต่ละคน พร้อมสรุปจำนวนที่ผ่าน/ไม่ผ่าน

**Input:**
```
85
55
92
45
70
```

**Output:**
```
Score 85: Pass
Score 55: Fail
Score 92: Pass
Score 45: Fail
Score 70: Pass
---
Pass: 3
Fail: 2
```

---

## 💡 Hint

- ใช้ `for i in range(5):` รับ input 5 ครั้ง
- ถ้า score >= 60: Pass, นับ pass
- ถ้าไม่: Fail, นับ fail

---

## Starter Code

```python
pass_count = 0
fail_count = 0

for i in range(5):
    score = int(input())
    if score >= 60:
        print(f"Score {score}: Pass")
        pass_count += 1
    else:
        print(f"Score {score}: Fail")
        fail_count += 1

print("---")
print(f"Pass: {pass_count}")
print(f"Fail: {fail_count}")
```
