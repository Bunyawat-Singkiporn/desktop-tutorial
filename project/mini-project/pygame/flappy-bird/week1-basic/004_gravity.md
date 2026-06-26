## เป้าหมาย

ให้นกตกลงทุกเฟรม (แรงโน้มถ่วง)

---

## แนวคิด

**แรงโน้มถ่วง** = แรงที่ดึงของให้ตกลง (เหมือนปล่อยลูกบอล)

```python
bird_speed = 0      # ความเร็วตอนนี้ (0 = นิ่ง)
GRAVITY = 0.4       # แรงดึงลงทุกเฟรม

bird_speed += GRAVITY   # เร็วขึ้นเรื่อยๆ (ตกเร็วขึ้น)
bird_y += bird_speed    # ขยับลงตามความเร็ว
```

`+=` หมายถึง **เอาค่าเดิม + เพิ่มอีก** เช่น `bird_speed += 0.4` = บวก 0.4 เข้าไป

---

## ทำไมต้องมี clock.tick(60)?

คอมวิ่งเร็วมาก — ถ้าไม่จำกัด นกจะตกทันใจ!

```python
clock.tick(60)   # ให้เกมวิ่ง 60 ครั้งต่อวินาที
```

---

## อธิบาย int(bird_y)

`bird_y` มีทศนิยม (เช่น 300.7) แต่จุดบนจอต้องเป็นจำนวนเต็ม

```python
int(bird_y)   # ปัดเป็นจำนวนเต็ม เช่น 300.7 → 300
```

---

## 📝 เพิ่มใน flappy.py

**1.** เพิ่ม **หลัง** `pygame.display.set_caption(...)`:

```python
clock = pygame.time.Clock()
```

**2.** เพิ่ม **หลัง** `bird_size = 25`:

```python
bird_speed = 0
GRAVITY = 0.4
```

**3.** เพิ่ม **ก่อน** `screen.fill("skyblue")` ใน game loop:

```python
    bird_speed += GRAVITY
    bird_y += bird_speed
```

**4.** เปลี่ยน `bird_y` ใน `draw.circle` เป็น `int(bird_y)`

**5.** เพิ่ม **หลัง** `pygame.display.flip()`:

```python
    clock.tick(60)
```

> รันดู — นกควรตกลงช้าๆ (ไม่ใช่หายทันที)
