# 3) จอสรุปผล + เหรียญ

## เป้าหมาย
จบเกมแล้วโชว์คะแนน จำนวนข้อที่ถูก และเหรียญ + กด R เล่นใหม่

---

## แนวคิด — นับข้อที่ถูก

```python
correct = 0
...
if picked == answer:
    score += 10
    correct += 1        # ← ตัวนับ (เหมือน Week 3 เป๊ะ)
```

---

## แนวคิด — เหรียญจากสัดส่วน

```python
total = len(questions)

if correct == total:
    medal = "GOLD"
elif correct >= total / 2:
    medal = "SILVER"
elif correct > 0:
    medal = "BRONZE"
else:
    medal = "ลองใหม่นะ"
```

| ถูก | จาก 4 ข้อ | ได้ |
|-----|-----------|-----|
| 4 | ครบ | GOLD |
| 2-3 | ครึ่งขึ้นไป | SILVER |
| 1 | มีถูกบ้าง | BRONZE |
| 0 | ไม่ถูกเลย | ลองใหม่นะ |

> `total / 2` = 2.0 — Python เทียบ `2 >= 2.0` ได้ปกติ ไม่ต้องกังวล

---

## แนวคิด — รีเซ็ตเกม (กด R)

การเริ่มใหม่ = **ตั้งตัวแปรทุกตัวกลับเป็นค่าเริ่มต้น**

```python
if event.key == pygame.K_r and finished:
    index = 0
    score = 0
    correct = 0
    last_picked = 0
    showing_result = False
    finished = False
```

> ลืมรีเซ็ตตัวไหน = บั๊ก! เช่นลืม `score = 0` → คะแนนสะสมข้ามรอบ

---

## 📝 แก้ `quiz.py`

**1.** เพิ่ม `correct = 0` ก่อนลูป และ `correct += 1` ตอนตอบถูก

**2.** แทนที่ก้อน `if finished:` ด้วยจอสรุปผล:

```python
    if finished:
        total = len(questions)
        if correct == total:
            medal = "GOLD"
        elif correct >= total / 2:
            medal = "SILVER"
        elif correct > 0:
            medal = "BRONZE"
        else:
            medal = "ลองใหม่นะ"

        pygame.draw.rect(screen, (45, 55, 90), (150, 180, 500, 260), border_radius=12)
        t1 = font_big.render("จบเกม!", True, "white")
        t2 = font_mid.render(f"คะแนน {score} / {total * 10}", True, "white")
        t3 = font_mid.render(f"ตอบถูก {correct} / {total} ข้อ", True, "white")
        t4 = font_big.render(medal, True, "gold")
        screen.blit(t1, (330, 205))
        screen.blit(t2, (250, 275))
        screen.blit(t3, (250, 320))
        screen.blit(t4, (250, 370))

        hint = font_sml.render("กด R เพื่อเล่นใหม่  |  Esc เพื่อออก", True, "white")
        screen.blit(hint, (250, 470))
```

**3.** เพิ่มการรับปุ่ม R และ Esc

---

> รันจนจบ — ต้องเห็นการ์ดสรุปผล กด R แล้วเริ่มใหม่ คะแนนกลับเป็น 0 ✅
