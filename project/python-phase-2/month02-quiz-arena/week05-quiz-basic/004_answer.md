# 3) กด 1-4 ตอบ → ไปข้อถัดไป

## เป้าหมาย
กดปุ่มเลข แล้วเปลี่ยนไปคำถามข้อถัดไป

---

## แนวคิด — จับปุ่มที่กด (KEYDOWN)

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:          # มีการกดปุ่ม
        if event.key == pygame.K_1:
            picked = 1
        if event.key == pygame.K_2:
            picked = 2
```

| ชื่อปุ่ม | ปุ่มจริง |
|----------|----------|
| `pygame.K_1` ... `K_4` | เลข 1-4 แถวบน |
| `pygame.K_r` | ปุ่ม R |
| `pygame.K_SPACE` | Space |
| `pygame.K_ESCAPE` | Esc |

> `KEYDOWN` = ตอนกดลง (เกิดครั้งเดียว) เหมาะกับการ "เลือกคำตอบ"
> ต่างจาก `pygame.key.get_pressed()` ที่เช็ก "ค้างอยู่ไหม" เหมาะกับการเดิน

---

## แนวคิด — เลื่อนไปข้อถัดไป

```python
index += 1                    # ไปข้อถัดไป
if index >= len(questions):   # เกินข้อสุดท้ายแล้ว
    finished = True           # จบเกม
```

> `len(questions)` = 4 → index ที่ใช้ได้คือ 0,1,2,3
> ถ้า index กลายเป็น 4 แล้วยังหยิบ `questions[4]` = **IndexError** 💥

---

## แนวคิด — หน้าจอมี 2 โหมด

```python
if finished:
    # วาดจอ "จบเกม"
else:
    # วาดคำถาม
```

> เกมทุกเกมมี "state" (สถานะ) — เล่นอยู่ / จบแล้ว / เมนู
> เดือนนี้เราใช้ตัวแปร `finished` เก็บ state แบบง่ายที่สุด

---

## 📝 แก้ `quiz.py`

**1.** เพิ่มหลัง `index = 0`:

```python
finished = False
```

**2.** **แทนที่** ก้อน `for event ...` ด้วย:

```python
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not finished:
            picked = 0
            if event.key == pygame.K_1:
                picked = 1
            if event.key == pygame.K_2:
                picked = 2
            if event.key == pygame.K_3:
                picked = 3
            if event.key == pygame.K_4:
                picked = 4

            if picked > 0:
                index += 1
                if index >= len(questions):
                    finished = True
```

**3.** **ครอบ** ส่วนที่วาดคำถามด้วย `if finished:` :

```python
    if finished:
        end = font_big.render("จบเกม!", True, "white")
        screen.blit(end, (300, 280))
    else:
        q = questions[index]
        choices = q[1]
        ...   # โค้ดวาดคำถามเดิม (เลื่อน indent เข้าไป 4 ช่อง)
```

---

> รันดู — กด 1-4 ต้องเปลี่ยนคำถาม กดครบ 4 ข้อ ต้องขึ้น "จบเกม!" ✅
> (ยังไม่มีคะแนน — Week 6 จะเพิ่มให้)
