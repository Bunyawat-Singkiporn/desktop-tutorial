# 2) กดตัวอักษรเพื่อเดา

## เป้าหมาย
กด A-Z แล้วตัวอักษรนั้นถูกเปิดเผย (ถ้ามีในคำ)

---

## แนวคิด — แปลงปุ่มเป็นตัวอักษร

เดือนที่แล้วเราเช็กทีละปุ่ม (`K_1`, `K_2`, ...) — ถ้าต้องเช็ก 26 ตัวคงบ้าไปแล้ว 😵

Pygame มีทางลัด:

```python
if event.type == pygame.KEYDOWN:
    letter = pygame.key.name(event.key).upper()    # กด a → "a" → "A"
```

| กดปุ่ม | `pygame.key.name()` | `.upper()` |
|--------|---------------------|------------|
| a | `"a"` | `"A"` |
| z | `"z"` | `"Z"` |
| space | `"space"` | `"SPACE"` |
| 1 | `"1"` | `"1"` |

> ปุ่มอื่นๆ ได้ชื่อยาวๆ แบบ `"space"` — เราต้องกรองออก!

---

## แนวคิด — กรองเฉพาะ A-Z

```python
if len(letter) == 1 and letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ...ใช้ได้...
```

| เช็ก | ทำไม |
|------|------|
| `len(letter) == 1` | ตัดพวก `"space"`, `"left"` ที่ยาวเกิน 1 |
| `letter in "ABC...Z"` | ตัดตัวเลขและสัญลักษณ์ |

---

## แนวคิด — กันการเดาซ้ำ

```python
if letter not in guessed:
    guessed.append(letter)
```

> `guessed.append(x)` = เพิ่ม x เข้าไปท้าย list (เหมือน `fruits.append()` ในเกม Fruit Collector)
> `not in` = "ไม่มีอยู่ใน"

---

## แนวคิด — โชว์ตัวที่เดาไปแล้ว

```python
used = " ".join(guessed)         # ["A","D"] → "A D"
screen.blit(font_mid.render(f"เดาไปแล้ว : {used}", True, "grey"), (40, 330))
```

> `" ".join(list)` = เอาสมาชิกใน list มาต่อกัน คั่นด้วยช่องว่าง

---

## 📝 แก้ `word.py`

**1.** เปลี่ยน `guessed = ["D"]` เป็น `guessed = []`

**2.** เพิ่มใน `for event ...`:

```python
        if event.type == pygame.KEYDOWN:
            letter = pygame.key.name(event.key).upper()
            if len(letter) == 1 and letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if letter not in guessed:
                    guessed.append(letter)
```

**3.** เพิ่มการวาดตัวที่เดาไปแล้ว (ก่อน `pygame.display.flip()`):

```python
    used = " ".join(guessed)
    screen.blit(font_mid.render(f"เดาไปแล้ว : {used}", True, (170, 180, 175)), (40, 340))
    screen.blit(font_mid.render("กดตัวอักษร A-Z เพื่อเดา", True, (170, 180, 175)), (40, 420))
```

---

> รันดู — กด D O G ต้องเปิดครบทั้งคำ ✅
> กดตัวอื่นก็ขึ้นในรายการ "เดาไปแล้ว" แต่คำยังไม่เปิด
> (ตอนนี้เดาผิดยังไม่เสียอะไร — สไลด์หน้าจะใส่ระบบชีวิต)
