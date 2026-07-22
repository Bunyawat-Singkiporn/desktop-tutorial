# 💥 Debugging — Question 2: Fix Runtime Error

**Difficulty:** 🟢 Easy

---

## โจทย์

โค้ดด้านล่างมี **Runtime Error** 2 จุด — หาและแก้

```python
scores = [85, 92, 78]

# Bug 1: index เกิน
print(scores[5])

# Bug 2: ชนิดข้อมูลผิด
age = input("Age: ")
next_year = age + 1
print(next_year)
```

**Output ที่ถูกต้อง** (ถ้าผู้ใช้ป้อน `15`):
```
78
16
```

---

## 💡 Hint

- Bug 1: index สุดท้ายคือ `len(scores) - 1`
- Bug 2: `input()` return `str` เสมอ ต้องแปลงเป็น `int` ก่อน

---

## Starter Code

```python
scores = [85, 92, 78]

# แก้ Bug 1
print(scores[5])

# แก้ Bug 2
age = input("Age: ")
next_year = age + 1
print(next_year)
```
