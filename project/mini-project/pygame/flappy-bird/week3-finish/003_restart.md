## เป้าหมาย

กด Space เล่นใหม่หลัง Game Over

---

## แนวคิด

ปุ่ม Space ทำ 2 อย่าง — ขึ้นกับสถานะเกม:

```python
if game_over:
    # แพ้แล้ว → รีเซ็ตกลับค่าเริ่มต้น
else:
    # ยังเล่นอยู่ → กระโดด
```

**รีเซ็ต** = ตั้งค่ากลับเหมือนตอนเริ่มเกม (นกกลับกลางจอ, คะแนน 0)

---

## อธิบาย if / else

```text
กด Space
  │
  ├─ game_over = True?  →  รีเซ็ตเกม
  │
  └─ game_over = False? →  นกกระโดด
```

---

## 📝 แก้ใน flappy.py

**แทนที่** บล็อกกด Space ด้วย:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                bird_y = 300
                bird_speed = 0
                pipe_x = 800
                pipe_h = 180
                score = 0
                game_over = False
            else:
                bird_speed = JUMP
```

> รันทดสอบ — ชนแล้วกด Space เล่นใหม่ได้! 🎉

---

## ทดสอบเกม

- [ ] กด Space นกกระโดด
- [ ] ท่อเลื่อนซ้าย
- [ ] ผ่านท่อ → คะแนนเพิ่ม
- [ ] ชนท่อ → Game Over
- [ ] กด Space → เล่นใหม่

---

## เช็คเฉลย

เปิด `flappy.py` ในโฟลเดอร์นี้ (ไฟล์เฉลย) เปรียบเทียบกับของคุณ
