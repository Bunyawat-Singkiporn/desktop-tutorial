## เป้าหมาย

กด Space แล้วนกกระโดด

---

## แนวคิด

เลข **ติดลบ** = บินขึ้น, เลข **บวก** = ตกลง

```python
JUMP = -8    # กระโดด = ความเร็วขึ้น
```

```text
กด Space  → bird_speed = -8   (ขึ้น ↑)
ไม่กด     → bird_speed += 0.4 (ตก ↓)
```

---

## อธิบายโค้ดรับปุ่ม

```python
if event.type == pygame.KEYDOWN:          # มีการกดปุ่ม
    if event.key == pygame.K_SPACE:       # กด Space
        bird_speed = JUMP                 # สั่งให้กระโดด
```

รวมเป็นบรรทัดเดียวได้:

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
```

`and` = ต้องเป็นทั้ง **กดปุ่ม** และ **ปุ่ม Space**

---

## 📝 เพิ่มใน flappy.py

**1.** เพิ่ม **หลัง** `GRAVITY = 0.4`:

```python
JUMP = -8
```

**2.** เพิ่มใน for event loop **หลัง** `pygame.QUIT`:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = JUMP
```

> รันทดสอบ — กด Space นกกระโดด ปล่อยแล้วนกตกลง 🎉

---

## เช็คเฉลย

เปิด `flappy.py` ในโฟลเดอร์นี้ (ไฟล์เฉลย) เปรียบเทียบกับของคุณ
