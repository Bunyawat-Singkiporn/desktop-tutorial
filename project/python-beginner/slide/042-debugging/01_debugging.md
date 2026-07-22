# 🐛 Debugging — การหาและแก้ข้อผิดพลาด

---

## ข้อผิดพลาด 3 ประเภท

---

## 1. Syntax Error — เขียนผิดกฎ

Python อ่านโค้ดไม่ออก → **รันไม่ได้เลย**

```python
# ❌ ลืม :
if x > 5
    print(x)

# ✅ แก้แล้ว
if x > 5:
    print(x)
```

> Python จะบอก: `SyntaxError: invalid syntax`

---

## 2. Runtime Error — พังตอนรัน

โค้ด syntax ถูก แต่เกิดปัญหาขณะทำงาน

```python
# ❌ หารด้วยศูนย์
x = 10 / 0          # ZeroDivisionError

# ❌ index เกินขนาด
nums = [1, 2, 3]
print(nums[5])       # IndexError

# ❌ ชนิดข้อมูลผิด
print("5" + 3)       # TypeError
```

---

## 3. Logic Error — ผลลัพธ์ผิด

โค้ดรันได้ แต่ **ให้ผลลัพธ์ที่ไม่ถูกต้อง**

```python
# ❌ Logic error
total = 0
for i in range(1, 5):
    total = i       # ผิด! ทับค่าทุกรอบ

print(total)        # 4 (ไม่ใช่ 10)

# ✅ ถูกต้อง
total = 0
for i in range(1, 5):
    total += i

print(total)        # 10
```

---

## วิธี Debug ด้วย print

```python
def calc(x, y):
    print("x =", x, "y =", y)   # ตรวจค่า
    result = x * y
    print("result =", result)    # ตรวจผล
    return result
```

---

## สรุป

| ประเภท | เกิดเมื่อ | วิธีแก้ |
|--------|---------|--------|
| Syntax | เขียนผิดกฎ | อ่าน error message |
| Runtime | รันแล้วพัง | ตรวจชนิดข้อมูล, ขอบเขต |
| Logic | ผลผิด | ใช้ print trace ค่าตัวแปร |
