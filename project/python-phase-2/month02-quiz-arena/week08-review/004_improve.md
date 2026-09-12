# 🔧 ปรับปรุงเกม — Quiz Arena v1.0

## เป้าหมาย
เพิ่ม 3 อย่างให้เกมสมบูรณ์: หน้าเริ่มเกม / สลับคำถาม / สถิติสูงสุด

---

## 1) หน้าเริ่มเกม (Start Screen)

เกมจริงไม่โยนผู้เล่นเข้าคำถามทันที — ต้องมีหน้าต้อนรับก่อน

```python
started = False           # ยังไม่เริ่ม

# ในส่วน INPUT
if not started:
    if event.key == pygame.K_SPACE:
        started = True
        question_start = pygame.time.get_ticks()   # เริ่มจับเวลาตอนกด Space!

# ในส่วน OUTPUT
if not started:
    screen.blit(font_big.render("QUIZ ARENA", True, "white"), (250, 200))
    screen.blit(font_mid.render("กด Space เพื่อเริ่ม", True, "yellow"), (270, 300))
elif finished:
    ...
else:
    ...
```

> ตอนนี้เกมเรามี **3 state**: `ยังไม่เริ่ม` → `กำลังเล่น` → `จบเกม`

---

## 2) สลับคำถามทุกรอบ

```python
import random

random.shuffle(questions)     # สลับลำดับใน list ทันที
```

| ก่อน | หลัง `shuffle` |
|------|----------------|
| `[Q1, Q2, Q3, Q4, Q5]` | `[Q3, Q1, Q5, Q2, Q4]` |

**ใส่ตรงไหน?** ตอนเริ่มเกมและตอนกด R

```python
if event.key == pygame.K_r:
    random.shuffle(questions)
    index = 0
    ...
```

> ต่างจาก `random.randint()` ตรงที่ `shuffle` **ไม่คืนค่าใหม่** แต่สลับ list เดิมเลย
> เขียน `questions = random.shuffle(questions)` = ❌ ได้ `None` (บั๊กยอดฮิต)

---

## 3) สถิติสูงสุด (High Score)

```python
best = 0                    # นอกลูป

# ตอนจบเกม
if score > best:
    best = score
```

ระวัง! อย่าให้มันทำงานทุกเฟรม — ให้ทำตอน **เพิ่งจบ** เท่านั้น

```python
                    if index >= len(questions):
                        finished = True
                        if score > best:      # ← ทำครั้งเดียวตอนจบ
                            best = score
```

แล้วโชว์บนจอสรุป:

```python
screen.blit(font_sml.render(f"สถิติสูงสุด {best}", True, "gold"), (250, 430))
```

> ตอนนี้สถิติหายเมื่อปิดเกม — **เดือน 5** เราจะเรียนวิธีบันทึกลงไฟล์ 💾

---

## 4) เก็บรายละเอียดเล็กๆ (Polish)

| เพิ่ม | โค้ด |
|-------|------|
| แถบความคืบหน้า | วาด rect ตามสัดส่วน `index / len(questions)` |
| นับจำนวนข้อที่เหลือ | `f"ข้อ {index+1}/{len(questions)}"` |
| ปุ่ม Esc ออกได้ทุกจอ | เช็ก `K_ESCAPE` นอกทุก state |

---

## 📝 ทำเอง แล้วเทียบกับ `quiz.py`

> ลองทำทีละข้อ รันทดสอบทุกครั้ง — อย่าทำ 3 อย่างพร้อมกันแล้วค่อยรัน!
> (ถ้าพัง จะไม่รู้ว่าพังเพราะอันไหน)
