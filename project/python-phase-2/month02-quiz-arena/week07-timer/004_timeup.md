# 3) หมดเวลา = ตอบผิด + โบนัสความเร็ว

## เป้าหมาย
เวลาหมดแล้วข้ามไปโชว์เฉลยเอง และตอบไวได้คะแนนพิเศษ

---

## แนวคิด — ตรวจหมดเวลาในลูป

```python
if not finished and not showing_result:
    passed = (pygame.time.get_ticks() - question_start) / 1000
    time_left = TIME_LIMIT - passed

    if time_left <= 0:
        time_left = 0
        last_picked = 0          # 0 = ไม่ได้เลือกอะไรเลย
        showing_result = True    # ข้ามไปโชว์เฉลย
```

> `last_picked = 0` เป็นรหัสพิเศษที่แปลว่า "หมดเวลา"
> ตอนวาดสี ข้อ 1-4 ไม่มีข้อไหนเท่ากับ 0 → จะไม่มีกรอบแดง มีแต่กรอบเขียวเฉลย ✅

---

## แนวคิด — โบนัสความเร็ว

```python
if picked == answer:
    bonus = int(time_left)        # เหลือ 7.4 วิ → โบนัส 7
    score += 10 + bonus
    correct += 1
```

| ตอบถูกตอนเหลือ | ได้คะแนน |
|----------------|----------|
| 9.5 วิ | 10 + 9 = 19 |
| 5.2 วิ | 10 + 5 = 15 |
| 0.8 วิ | 10 + 0 = 10 |

> `int(7.4)` = 7 (ตัดทศนิยมทิ้ง)

---

## แนวคิด — ข้อความ 3 แบบ

```python
if last_picked == 0:
    msg = font_mid.render(f"หมดเวลา! คำตอบคือข้อ {answer}", True, "orange")
elif last_picked == answer:
    msg = font_mid.render(f"ถูกต้อง! +{10 + last_bonus}", True, "lightgreen")
else:
    msg = font_mid.render(f"ผิด! คำตอบคือข้อ {answer}", True, "salmon")
```

> ต้องเช็ก `last_picked == 0` **ก่อน** เสมอ ไม่งั้นหมดเวลาจะไปเข้าเงื่อนไข "ผิด"

---

## ⚠️ กับดักสำคัญ: หยุดเวลาตอนโชว์เฉลย

```python
if not finished and not showing_result:      # ← เงื่อนไขนี้สำคัญมาก
    ...คำนวณเวลา...
```

ถ้าลืมเงื่อนไข `not showing_result` → เวลาเดินต่อตอนอ่านเฉลย → เด้งข้ามข้อเอง 😱

---

## 📝 แก้ `quiz.py` (ดูโค้ดเต็มที่ `quiz.py`)

1. เพิ่มการเช็ก `time_left <= 0` → `showing_result = True`
2. เพิ่ม `last_bonus` เก็บโบนัสของข้อล่าสุด
3. แก้ข้อความ feedback ให้มี 3 แบบ
4. รีเซ็ต `question_start` ทุกครั้งที่ขึ้นข้อใหม่ (รวมตอนกด R ด้วย!)

---

> รันแล้วลอง **ไม่กดอะไรเลย** — ต้องขึ้น "หมดเวลา!" เอง ✅
> ลองตอบไวๆ — คะแนนต้องได้มากกว่า 10
