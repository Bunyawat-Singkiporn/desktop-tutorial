# 1) สุ่มตำแหน่งและความเร็ว

## เป้าหมาย
ผลไม้เกิดใหม่ที่ตำแหน่งสุ่ม และตกด้วยความเร็วไม่เท่ากัน

---

## แนวคิด — เก็บความเร็วไว้ในตัวผลไม้เอง

เดิมผลไม้เก็บ 2 ค่า ตอนนี้เพิ่มเป็น 3

```python
fruit = [x, y, speed]
#        0  1    2
```

```python
for fruit in fruits:
    fruit[1] = fruit[1] + fruit[2]      # ตกด้วยความเร็วของตัวเอง
```

> ผลไม้แต่ละลูกตกไม่เท่ากัน = เกมดูมีชีวิตขึ้นทันที

---

## แนวคิด — สุ่มค่าเริ่มต้น

```python
import random

x = random.randint(20, 780)     # สุ่มตำแหน่งแนวนอน
y = random.randint(-400, -20)   # สุ่มความสูงเหนือจอ (ทยอยลงมา ไม่มาพร้อมกัน)
speed = random.randint(2, 6)    # สุ่มความเร็ว
```

| ทำไม `y` ติดลบ? | เพราะอยู่ **เหนือขอบจอ** ยังมองไม่เห็น |
|---|---|
| ทำไมสุ่มช่วงกว้าง? | ผลไม้จะได้ทยอยโผล่ ไม่ตกลงมาพร้อมกันเป็นแถว |

---

## แนวคิด — สร้างผลไม้เริ่มต้นด้วย `for`

```python
fruits = []
for i in range(8):
    x = random.randint(20, 780)
    y = random.randint(-400, -20)
    speed = random.randint(2, 6)
    fruits.append([x, y, speed])
```

> `fruits.append([...])` = เพิ่มผลไม้ลูกใหม่เข้า list
> อยากได้ 20 ลูก เปลี่ยน `range(8)` เป็น `range(20)` จบ

---

## 📝 แก้ `fruit.py`

**1.** เพิ่มบรรทัดบนสุด:

```python
import random
```

**2.** **แทนที่** list `fruits` เดิมด้วย:

```python
fruits = []
for i in range(8):
    fruits.append([random.randint(20, 780), random.randint(-400, -20), random.randint(2, 6)])
```

**3.** **แทนที่** ก้อนที่ทำให้ผลไม้ตก:

```python
    for fruit in fruits:
        fruit[1] = fruit[1] + fruit[2]
        if fruit[1] > 620:
            fruit[0] = random.randint(20, 780)
            fruit[1] = random.randint(-400, -20)
            fruit[2] = random.randint(2, 6)
```

---

> รันดู 2-3 รอบ — ผลไม้ต้องลงมาไม่ซ้ำแบบเดิมเลย ✅
