# 2) Feedback — บอกถูก/ผิด ด้วยสี

## เป้าหมาย
ตอบแล้วหยุดโชว์เฉลย: กรอบเขียว = คำตอบถูก, กรอบแดง = ที่เราเลือกผิด
กด Space เพื่อไปข้อถัดไป

---

## แนวคิด — เพิ่ม state `showing_result`

เดิม: กด 1-4 → ข้ามข้อทันที (เร็วเกินไป ไม่ได้เรียนรู้อะไร)
ใหม่: กด 1-4 → **หยุดโชว์เฉลย** → กด Space → ค่อยไปต่อ

```python
showing_result = False

# ตอนกด 1-4
if picked > 0 and not showing_result:
    last_picked = picked
    if picked == questions[index][2]:
        score += 10
    showing_result = True          # ← หยุดไว้ก่อน

# ตอนกด Space
if event.key == pygame.K_SPACE and showing_result:
    showing_result = False
    index += 1
    if index >= len(questions):
        finished = True
```

> **ห้ามลืม** `showing_result = False` ตอนไปข้อใหม่ ไม่งั้นจะค้างอยู่จอเฉลยตลอด

---

## แนวคิด — เลือกสีตามเงื่อนไข

วาดกล่องตัวเลือก 4 กล่องเหมือนเดิม แต่เลือกสีก่อนวาด

```python
for i in range(4):
    number = i + 1                       # ข้อที่ 1-4
    color = (45, 55, 90)                 # สีปกติ

    if showing_result:
        if number == answer:
            color = (40, 140, 70)        # เขียว = ข้อที่ถูก
        elif number == last_picked:
            color = (170, 50, 60)        # แดง = ข้อที่เราเลือก (ผิด)

    pygame.draw.rect(screen, color, (100, y, 600, 55), border_radius=8)
```

```text
เฉลย = 2, เราเลือก 4

ข้อ 1 → สีปกติ
ข้อ 2 → เขียว  (นี่คือคำตอบที่ถูก)
ข้อ 3 → สีปกติ
ข้อ 4 → แดง    (เราเลือกอันนี้ ผิด)
```

> ถ้าเราเลือกถูก ข้อนั้นจะเข้าเงื่อนไขแรก (เขียว) — `elif` ทำให้ไม่ทับกัน

---

## แนวคิด — ข้อความ feedback

```python
if showing_result:
    if last_picked == answer:
        msg = font_mid.render("ถูกต้อง! +10", True, "lightgreen")
    else:
        msg = font_mid.render(f"ผิด! คำตอบคือข้อ {answer}", True, "salmon")
    screen.blit(msg, (100, 505))

    hint = font_sml.render("กด Space เพื่อไปข้อถัดไป", True, "white")
    screen.blit(hint, (100, 552))
```

---

## 📝 แก้ `quiz.py` (ดูโค้ดเต็มที่ `003_feedback.py`)

1. เพิ่ม `showing_result = False` ก่อนลูป
2. ตอนกด 1-4 → เซ็ต `showing_result = True` (ยังไม่ `index += 1`)
3. เพิ่มการรับปุ่ม `K_SPACE` → `index += 1` และรีเซ็ต `showing_result = False`
4. ใส่การเลือกสีในลูป `for i in range(4)`
5. วาดข้อความ feedback

---

> รันดู — ตอบผิดต้องเห็นกรอบแดงที่เราเลือก และกรอบเขียวที่เฉลย ✅
> กด Space ถึงจะไปข้อต่อไป
