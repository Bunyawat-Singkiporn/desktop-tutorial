# 🔽 Practice: Loop Review — Question 9: Filter List

**Difficulty:** 🟡 Medium

---

## โจทย์

วนผ่าน list แล้วเก็บเฉพาะคะแนนที่ >= 60 ลงใน list ใหม่

```python
scores = [88, 45, 72, 30, 95, 58, 66]
```

**Output:**
```
Passed: [88, 72, 95, 66]
Count: 4
```

---

## 💡 Hint

- สร้าง `passed = []` ก่อน
- ถ้า `s >= 60` → `passed.append(s)`
- ใช้ `len(passed)` นับจำนวน

---

## Starter Code

```python
scores = [88, 45, 72, 30, 95, 58, 66]
passed = []

for s in scores:
    # If s >= 60, add to passed

print("Passed:", passed)
print("Count:", len(passed))
```
