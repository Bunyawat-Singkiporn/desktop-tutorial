# elif

## ทำไมต้องมี elif

if / else มีได้แค่ 2 ทางเลือก

ตัวอย่าง

ผ่าน

ไม่ผ่าน

แต่บางครั้งเรามีมากกว่า 2 กรณี

เช่น

เกรด

A

B

C

F

เราจึงใช้ elif

รูปแบบ

```python
if condition:
    ...

elif condition:
    ...

elif condition:
    ...

else:
    ...
```

ตัวอย่าง

```python
score = int(input())

if score >= 80:
    print("A")

elif score >= 70:
    print("B")

elif score >= 60:
    print("C")

else:
    print("F")
```

Python จะตรวจจากบนลงล่าง

เมื่อเจอเงื่อนไขที่จริง

จะหยุดทันที