# 🔁 Loop Review — ทบทวน Loop ทุกแบบ

---

## สรุป Loop ที่เรียนมา

| Loop | ใช้เมื่อ | ตัวอย่าง |
|------|---------|---------|
| `for range()` | รู้จำนวนรอบแน่นอน | นับ 1–10 |
| `for list` | วนผ่านสมาชิกใน list | แสดงรายชื่อ |
| `while` | วนจนเงื่อนไขเป็น False | รับ input ซ้ำ |
| `nested` | loop ซ้อน loop | สร้าง pattern, ตาราง |
| `break` | หยุดกลางคัน | หาค่าที่ต้องการ |
| `continue` | ข้ามบางรอบ | กรองข้อมูล |

---

## ตัวอย่างรวม 1: หาผลรวม + เฉลี่ย

```python
scores = [85, 92, 78, 95, 88]
total = 0

for score in scores:
    total = total + score

average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.1f}")
```

```
Total: 438
Average: 87.6
```

---

## ตัวอย่างรวม 2: รับ Input ซ้ำจนพิมพ์ 0

```python
total = 0
count = 0

while True:
    number = int(input())
    if number == 0:
        break
    total += number
    count += 1

print(f"Count: {count}, Total: {total}")
```

---

## ตัวอย่างรวม 3: Pattern ตามขนาด

```python
n = int(input())

for row in range(1, n + 1):
    for col in range(row):
        print("*", end="")
    print()
```

Input: `4`
```
*
**
***
****
```

---

## เลือก Loop อย่างไร?

```
รู้จำนวนรอบ?
 YES → for range() หรือ for list
 NO  → while
       ต้องหยุดกลางคัน?  → ใช้ break
       ต้องข้ามบางรอบ?   → ใช้ continue
```
