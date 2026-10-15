# 🔄 Review Lists — ทบทวน List

---

## สิ่งที่เรียนมาทั้งหมด

### สร้างและเข้าถึง
```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])    # apple
print(fruits[-1])   # mango
print(len(fruits))  # 3
```

### Loop
```python
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i, ":", fruits[i])
```

### Methods
```python
fruits.append("kiwi")        # เพิ่มท้าย
fruits.remove("banana")      # ลบตามค่า
fruits[0] = "grape"          # แก้ไขตามตำแหน่ง
fruits.sort()                # เรียงน้อย→มาก
fruits.sort(reverse=True)    # เรียงมาก→น้อย
```

---

## Pattern รวมคะแนนและหาค่าเฉลี่ย

```python
scores = [80, 75, 90, 65, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("Average:", average)
```

---

## ข้อผิดพลาดที่พบบ่อย

| ปัญหา | ตัวอย่าง | แก้ไข |
|-------|---------|-------|
| Index เกินขนาด | `fruits[5]` (มีแค่ 3 ตัว) | ตรวจด้วย `len()` |
| ลบค่าที่ไม่มี | `fruits.remove("grape")` | ตรวจด้วย `in` ก่อน |
| ลืม index เริ่มที่ 0 | `fruits[1]` คือตัวที่สอง | จำ: ตัวแรก = `[0]` |

---

## Checklist ก่อนสอบ

- [ ] สร้าง list ได้
- [ ] เข้าถึงข้อมูลด้วย index (บวก / ลบ) ได้
- [ ] ใช้ `len()` ได้
- [ ] loop ผ่าน list ได้ทั้งสองแบบ
- [ ] ใช้ `.append()`, `.remove()`, `.sort()` ได้
- [ ] filter และ count ด้วย loop ได้
