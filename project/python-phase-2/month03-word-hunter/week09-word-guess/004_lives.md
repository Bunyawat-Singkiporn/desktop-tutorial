# 3) ระบบชีวิต + ชนะ/แพ้

## เป้าหมาย
เดาผิดเสียชีวิต 1 ดวง (มี 6 ดวง) — เดาครบทุกตัวชนะ, ชีวิตหมดแพ้

---

## แนวคิด — เดาผิดคือ "ไม่มีในคำ"

```python
if letter in word:
    pass                 # ถูก! ไม่ต้องทำอะไร (การวาดจะเปิดเผยให้เอง)
else:
    lives -= 1           # ผิด! เสียชีวิต
```

> `letter in word` — คำสั่งเดียวเช็กทั้งคำ ไม่ต้องวน `for` เอง 🎯

---

## แนวคิด — เช็กว่าชนะหรือยัง

"ชนะ" = **ทุกตัวอักษรในคำอยู่ใน guessed แล้ว**

```python
win = True
for ch in word:
    if ch not in guessed:
        win = False         # เจอตัวที่ยังไม่ถูกเดา → ยังไม่ชนะ
```

```text
word = "DOG", guessed = ["D", "O", "G"]
  D อยู่ใน guessed ✓
  O อยู่ใน guessed ✓
  G อยู่ใน guessed ✓
  → win ยังเป็น True = ชนะ!

word = "DOG", guessed = ["D", "G"]
  O ไม่อยู่ → win = False
```

> เทคนิคนี้เรียกว่า **"สมมติว่าจริงไว้ก่อน แล้วหาข้อขัดแย้ง"** ใช้บ่อยมากในการเขียนเกม

---

## แนวคิด — วาดหัวใจ ♥

```python
hearts = "♥ " * lives            # lives = 3 → "♥ ♥ ♥ "
screen.blit(font_mid.render(hearts, True, "red"), (600, 30))
```

ถ้าฟอนต์ไม่รองรับ ♥ ใช้แบบนี้แทน:

```python
screen.blit(font_mid.render(f"ชีวิต {lives}", True, "red"), (620, 30))
```

---

## แนวคิด — หยุดรับปุ่มเมื่อจบเกม

```python
if event.type == pygame.KEYDOWN and not game_over:
    ...รับตัวอักษร...
```

> ถ้าลืมเงื่อนไขนี้ ผู้เล่นจะเดาต่อได้ทั้งที่ชีวิตหมดแล้ว

---

## 📝 แก้ `word.py`

**1.** เพิ่มก่อนลูป:

```python
lives = 6
game_over = False
win = False
```

**2.** ในส่วนรับปุ่ม เพิ่มการหักชีวิต:

```python
                if letter not in guessed:
                    guessed.append(letter)
                    if letter not in word:
                        lives -= 1
```

**3.** หลังส่วนรับ event เพิ่มการเช็กชนะ/แพ้:

```python
    win = True
    for ch in word:
        if ch not in guessed:
            win = False

    if win or lives <= 0:
        game_over = True
```

**4.** วาดผลลัพธ์:

```python
    if game_over:
        if win:
            msg = font_mid.render("ชนะ! เก่งมาก", True, "lightgreen")
        else:
            msg = font_mid.render(f"แพ้! คำตอบคือ {word}", True, "salmon")
        screen.blit(msg, (40, 420))
```

---

> รันดู — เดาผิด 6 ครั้งต้องแพ้ / เดาถูกครบต้องชนะ ✅
