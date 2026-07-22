# 👁️ Read Code — การอ่านโค้ด

---

## ทำไมต้องอ่านโค้ดเป็น?

- แก้ bug ในโค้ดที่ไม่ได้เขียนเอง
- ทำงานร่วมกับทีม
- ทบทวนโค้ดเก่า

---

## วิธีอ่านโค้ดอย่างเป็นขั้นตอน

```
1. มองภาพรวมก่อน
2. หา Input: รับค่าอะไร?
3. ไล่บรรทัดจากบนลงล่าง
4. Trace ค่าตัวแปรทีละขั้น
5. ถ้ามี loop — คิด "กี่รอบ ค่าเปลี่ยนยังไง"
6. ถ้ามี if — คิด "เงื่อนไขเป็นจริงไหม"
7. หา Output: แสดงอะไร?
```

---

## ตัวอย่าง — ลองอ่านก่อน

```python
numbers = [3, 7, 2, 9, 4]
result = 0

for num in numbers:
    if num > result:
        result = num

print(result)
```

**คิดทีละขั้น:**
```
result = 0
รอบ 1: num=3, 3 > 0 → result=3
รอบ 2: num=7, 7 > 3 → result=7
รอบ 3: num=2, 2 > 7 → ไม่เปลี่ยน
รอบ 4: num=9, 9 > 7 → result=9
รอบ 5: num=4, 4 > 9 → ไม่เปลี่ยน
print(9)
```

**Output:** `9`

---

## ตัวอย่าง — โค้ดที่มี Function

```python
def double(x):
    return x * 2

def apply_all(lst):
    result = []
    for item in lst:
        result.append(double(item))
    return result

nums = [1, 2, 3]
print(apply_all(nums))
```

**Output:** `[2, 4, 6]`

---

## เคล็ดลับ

- **Trace บนกระดาษ** — เขียนค่าตัวแปรแต่ละรอบ
- **อ่านชื่อ function** — ชื่อดีบอกหน้าที่เลย
- **มองหา return** — นั่นคือผลลัพธ์ของ function
