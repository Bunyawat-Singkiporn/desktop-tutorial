# 🔗 Logic Integration — รวมทุกทักษะ

---

## การคิดแบบ Algorithmic

ก่อนเขียนโค้ด ให้ถามตัวเอง:
```
1. Input คืออะไร?
2. ต้องการ Output แบบไหน?
3. ขั้นตอนจากอินพุตไปเอาต์พุตคืออะไร?
4. ต้องใช้ tools อะไร?
```

---

## เลือก Tool ให้เหมาะ

| สถานการณ์ | ใช้ |
|----------|-----|
| เก็บหลายค่า, เพิ่มลบได้ | List |
| ข้อมูลคู่ key-value | Dictionary |
| ค่าคงที่ | Tuple |
| ค่าไม่ซ้ำ | Set |
| ทำซ้ำตามจำนวน | for loop |
| ทำซ้ำจนเงื่อนไขจบ | while loop |
| โค้ดที่ใช้ซ้ำ | Function |

---

## ตัวอย่างการแก้ปัญหา

**โจทย์:** รับชื่อนักเรียน 5 คน แสดงชื่อที่ขึ้นต้นด้วย "A"

```
Input:  ชื่อ 5 คน
Output: ชื่อที่ขึ้นต้นด้วย A

ขั้นตอน:
1. สร้าง list ว่าง
2. รับชื่อ 5 ครั้งด้วย loop
3. loop ผ่าน list
4. if ชื่อขึ้นต้นด้วย "A" → print
```

```python
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

for name in names:
    if name.startswith("A"):
        print(name)
```

---

## หลักสำคัญ

- แก้ปัญหาทีละขั้นตอน
- ทดสอบ output ทุกขั้น
- แบ่ง function เมื่อโค้ดซับซ้อน
