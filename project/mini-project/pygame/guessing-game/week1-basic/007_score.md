## เป้าหมาย

เพิ่มคะแนนเมื่อเดาถูก + แสดงคะแนนบนจอ

---

## แนวคิด

**ตัวแปร** `score` เก็บคะแนน เริ่มที่ 0

```python
score = 0      # int เริ่มต้นที่ 0
score += 1     # เพิ่มทีละ 1
```

`score += 1` มาจาก `score = score + 1`
(operator `+=` ที่เรียนใน Python-beginner)

**f-string** แสดงตัวเลขในข้อความ:

```python
f"Score: {score}"    # ถ้า score = 2 → "Score: 2"
```

`{score}` = แทรกค่าตัวแปรเข้าไปในข้อความ
(output formatting ที่เรียนใน Python-beginner)

---

## อธิบายโค้ด

| บรรทัด | ความหมาย |
|--------|----------|
| `score = 0` | ตั้งค่าคะแนนเริ่มต้น |
| `score += 1` | บวก 1 เข้าคะแนนเดิม |
| `f"Score: {score}"` | แสดงตัวเลขคะแนนในข้อความ |
| `screen.blit(score_text, (20, 20))` | วางคะแนนมุมบนซ้าย |

---

## 📝 เพิ่มใน game.py

**1.** เพิ่ม **หลัง** `secret_number = 3`:

```python
score = 0
```

**2.** เพิ่ม **ใน** `if guess == secret_number:` **หลัง** `message = "Correct!"`:

```python
                    score += 1
```

**3.** เพิ่ม **ก่อน** `pygame.display.flip()`:

```python
    score_text = font.render(f"Score: {score}", True, "blue")
    screen.blit(score_text, (20, 20))
```

> รันทดสอบ — เดาถูกแล้วคะแนนเพิ่ม 🎉

---

## เช็คเฉลย

เปิด `game.py` ในโฟลเดอร์นี้ เปรียบเทียบกับของคุณ
