# 🔥 Debugging — Question 4: Fix All Three

**Difficulty:** 🔴 Hard

---

## โจทย์

โค้ดด้านล่างมี **3 บัค** (Syntax + Runtime + Logic) — หาและแก้ทั้งหมด

```python
scores = [85, 72, 90, 68, 95]
total = 0

for score in scores
    total = score

average = total / 0    # ← ตรวจดี ๆ

if average >= 70:
    print("Class passed)   # ← ตรวจดี ๆ
else:
    print("Class failed")

print("Average:", average)
```

**Output ที่ถูกต้อง:**
```
Class passed
Average: 82.0
```

---

## 💡 Hint

อ่านโค้ดทีละบรรทัด แล้วถามตัวเองว่า:
1. บรรทัดไหนผิด grammar Python?
2. บรรทัดไหนจะพังตอนรัน?
3. บรรทัดไหน logic ผิด?

---

## Starter Code

```python
scores = [85, 72, 90, 68, 95]
total = 0

for score in scores
    total = score

average = total / 0

if average >= 70:
    print("Class passed)
else:
    print("Class failed")

print("Average:", average)
```
