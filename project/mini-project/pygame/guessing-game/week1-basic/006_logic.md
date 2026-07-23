## เป้าหมาย

ตรวจว่าเดาถูกหรือผิด

---

## แนวคิด

**เลขลับ** (secret number) คือเลขที่เราซ่อนไว้ — ผู้เล่นต้องเดา

```python
secret_number = 3    # ตัวแปร int เก็บเลขลับ
```

เปรียบเทียบ `guess` กับ `secret_number` ด้วย `if / elif / else`:

```python
if guess == secret_number:     # เดาถูก
    message = "Correct!"
elif guess < secret_number:    # เดาน้อยไป
    message = "Too Low!"
else:                          # เดามากไป
    message = "Too High!"
```

`==` คือ **เปรียบเทียบ** (ต่างจาก `=` ที่เป็นการกำหนดค่า!)

```text
secret_number = 3    ← กำหนดค่า (=)
guess == 3           ← เปรียบเทียบ (==) → True หรือ False
```

---

## อธิบายโค้ด

| บรรทัด | ความหมาย |
|--------|----------|
| `secret_number = 3` | เลขลับที่ซ่อนไว้ |
| `guess = None` | ยังไม่มีการเดา (None = ไม่มีค่า) |
| `guess == secret_number` | เดาตรงกับเลขลับไหม? |
| `guess < secret_number` | เดาน้อยกว่าเลขลับไหม? |
| `else` | ถ้าไม่ตรงทั้งสอง = เดามากกว่า |
| `if guess is not None` | มีการกดเลขแล้ว (ไม่ใช่ None) |

---

## 📝 แก้ใน game.py

**1.** เพิ่ม **หลัง** `message = "Guess Number 1-5"`:

```python
secret_number = 3
```

**2.** **แทนที่** `if event.type == pygame.KEYDOWN:` ทั้งบล็อกด้วย:

```python
        if event.type == pygame.KEYDOWN:
            guess = None

            if event.key == pygame.K_1:
                guess = 1
            elif event.key == pygame.K_2:
                guess = 2
            elif event.key == pygame.K_3:
                guess = 3
            elif event.key == pygame.K_4:
                guess = 4
            elif event.key == pygame.K_5:
                guess = 5

            if guess is not None:
                if guess == secret_number:
                    message = "Correct!"
                elif guess < secret_number:
                    message = "Too Low!"
                else:
                    message = "Too High!"
```

> รันทดสอบ — กด 3 → "Correct!", กด 1 → "Too Low!", กด 5 → "Too High!"
