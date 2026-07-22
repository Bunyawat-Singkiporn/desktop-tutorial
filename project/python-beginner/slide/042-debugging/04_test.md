# 🧩 Debugging — Question 3: Fix Logic Error

**Difficulty:** 🟡 Medium

---

## โจทย์

โค้ดรันได้แต่ผลลัพธ์ **ผิด** — หา Logic Error และแก้

```python
# โปรแกรมหาผลรวม 1 ถึง 5
total = 0
for i in range(1, 5):
    total = i        # ← Logic error!

print("Sum:", total)
# Expected: Sum: 15
# Got: Sum: 4
```

---

## 💡 Hint

ต้องการ **สะสม** ค่า ไม่ใช่ **ทับ** ค่า

---

## Starter Code

```python
total = 0
for i in range(1, 5):
    total = i   # แก้บรรทัดนี้

# แก้ range ให้ถูกต้องด้วย
print("Sum:", total)
```
