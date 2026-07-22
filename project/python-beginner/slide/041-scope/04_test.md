# 🌐 Practice Scope — Question 3: Local and Global

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้างโปรแกรมที่ใช้ทั้ง global และ local variable อย่างถูกต้อง

**เงื่อนไข:**
- `SCHOOL_NAME = "True Coding"` — global (ใช้ใน function ได้)
- function `introduce(name, score)` — ใช้ local variables ข้างใน
- แสดงผลด้วย global school name

**Output:**
```
[True Coding] Alice scored 90
[True Coding] Bob scored 75
```

---

## Starter Code

```python
SCHOOL_NAME = "True Coding"

def introduce(name, score):
    # ใช้ SCHOOL_NAME (global) และ name, score (local parameter)
    # Write your code here

introduce("Alice", 90)
introduce("Bob", 75)
```
