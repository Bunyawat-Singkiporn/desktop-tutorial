# 🎢 Practice and/or/not — Question 1: Ride Allowed

**Difficulty:** 🟢 Easy

---

## โจทย์

รับอายุและส่วนสูง แล้วตรวจสอบว่าขึ้นเครื่องเล่นได้หรือไม่

**เงื่อนไข:** ต้องผ่าน **ทั้งสอง** ข้อ
- อายุ >= 12
- ส่วนสูง >= 140

| ผล | Output |
|----|--------|
| ผ่านทั้งคู่ | `Ride Allowed` |
| ไม่ผ่าน | `Cannot Ride` |

---

## ตัวอย่าง

**Input:**
```
14
150
```

**Output:**
```
Ride Allowed
```

---

## 💡 Hint

ใช้ `and` เพื่อตรวจสอบว่าเงื่อนไขทั้งสองเป็นจริงพร้อมกัน

---

## Starter Code

```python
age = int(input())
height = int(input())

# Write your code here
```