# 2) นับถอยหลัง + แถบเวลา

## เป้าหมาย
แต่ละข้อมีเวลา 10 วินาที แสดงเป็นแถบที่สั้นลงเรื่อยๆ

---

## แนวคิด — นับถอยหลัง

```python
TIME_LIMIT = 10                                     # วินาทีต่อข้อ

question_start = pygame.time.get_ticks()            # ตอนเริ่มข้อ

# ในลูป (ทุกเฟรม)
passed = (pygame.time.get_ticks() - question_start) / 1000
time_left = TIME_LIMIT - passed                     # เหลือกี่วินาที
```

```text
passed = 0    →  time_left = 10.0
passed = 3.5  →  time_left = 6.5
passed = 10   →  time_left = 0.0   ← หมดเวลา!
```

> **สำคัญ** ต้อง `question_start = pygame.time.get_ticks()` ใหม่ **ทุกครั้งที่ขึ้นข้อใหม่**
> ไม่งั้นเวลาจะไหลต่อจากข้อเก่า

---

## แนวคิด — แถบเวลา (progress bar)

แถบคือสี่เหลี่ยม 2 อัน วางทับกัน

```python
BAR_W = 600                                    # ความกว้างเต็ม

ratio = time_left / TIME_LIMIT                 # เหลือกี่ส่วน (0.0 - 1.0)
if ratio < 0:
    ratio = 0

pygame.draw.rect(screen, (60, 65, 90), (100, 105, BAR_W, 16), border_radius=8)      # พื้นหลัง
pygame.draw.rect(screen, bar_color, (100, 105, int(BAR_W * ratio), 16), border_radius=8)  # แถบจริง
```

```text
time_left = 10  →  ratio = 1.00  →  กว้าง 600 px  ████████████
time_left = 5   →  ratio = 0.50  →  กว้าง 300 px  ██████
time_left = 2   →  ratio = 0.20  →  กว้าง 120 px  ██
```

---

## แนวคิด — เปลี่ยนสีตามเวลา

```python
if time_left > 5:
    bar_color = (60, 200, 110)      # เขียว = สบาย
elif time_left > 2:
    bar_color = (240, 200, 60)      # เหลือง = เริ่มลุ้น
else:
    bar_color = (230, 70, 70)       # แดง = จวนแล้ว!
```

> การเปลี่ยนสีแบบนี้เรียกว่า **feedback ทางสายตา** ทำให้เกมตื่นเต้นขึ้นมาก

---

## 📝 แก้ `quiz.py`

**1.** เพิ่มก่อนลูป:

```python
TIME_LIMIT = 10
question_start = pygame.time.get_ticks()
time_left = TIME_LIMIT
```

**2.** เพิ่มใน game loop **ก่อน** `screen.fill(...)`:

```python
    if not finished and not showing_result:
        passed = (pygame.time.get_ticks() - question_start) / 1000
        time_left = TIME_LIMIT - passed
```

**3.** เพิ่มการวาดแถบ (ในส่วน `else:` ที่วาดคำถาม)

**4.** ตอนไปข้อถัดไป (กด Space) เพิ่ม:

```python
                    question_start = pygame.time.get_ticks()
```

---

> รันดู — แถบต้องสั้นลงและเปลี่ยนสี เขียว → เหลือง → แดง ✅
> ตอนนี้หมดเวลาแล้วยังไม่เกิดอะไร — สไลด์หน้าจัดให้
