# 1) แสดงคำลับแบบซ่อน

## เป้าหมาย
มีคำลับ 1 คำ แสดงเป็น `_ _ _` บนหน้าจอ

---

## แนวคิด — string คือ "ลิสต์ของตัวอักษร"

```python
word = "DOG"

print(word[0])      # D   ← ตัวแรก (นับจาก 0 เหมือน list!)
print(word[1])      # O
print(len(word))    # 3   ← ยาวกี่ตัว
```

วนดูทีละตัวด้วย `for`

```python
for ch in word:
    print(ch)
# D
# O
# G
```

| เขียน | ได้ |
|-------|-----|
| `word[0]` | ตัวอักษรตัวแรก |
| `len(word)` | จำนวนตัวอักษร |
| `for ch in word:` | วนทีละตัว |
| `"D" in word` | `True` (มี D อยู่) |

---

## แนวคิด — สร้างข้อความที่จะโชว์

```python
guessed = ["D"]              # ตัวที่เดาไปแล้ว
shown = ""                   # ข้อความที่จะวาดบนจอ

for ch in word:
    if ch in guessed:
        shown = shown + ch + " "      # เปิดเผยตัวนี้
    else:
        shown = shown + "_ "          # ยังซ่อนอยู่

# shown = "D _ _ "
```

```text
รอบที่ 1: ch = "D"  →  อยู่ใน guessed  →  shown = "D "
รอบที่ 2: ch = "O"  →  ไม่อยู่         →  shown = "D _ "
รอบที่ 3: ch = "G"  →  ไม่อยู่         →  shown = "D _ _ "
```

> `shown = shown + ch` คือการ **ต่อข้อความ** เขียนสั้นได้ว่า `shown += ch`
> (เหมือน `score += 10` เลย! แค่เปลี่ยนจากบวกเลขเป็นต่อคำ)

---

## 📝 สร้างไฟล์ `word.py`

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Word Hunter")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 56)
font_mid = pygame.font.SysFont("tahoma", 28)

word = "DOG"
hint = "สัตว์เลี้ยงที่ชอบเห่า"
guessed = ["D"]              # ทดลองใส่ D ไว้ก่อน

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 40, 35))

    screen.blit(font_mid.render("WORD HUNTER", True, "white"), (40, 30))
    screen.blit(font_mid.render(f"คำใบ้ : {hint}", True, "yellow"), (40, 110))

    shown = ""
    for ch in word:
        if ch in guessed:
            shown += ch + " "
        else:
            shown += "_ "

    screen.blit(font_big.render(shown, True, "white"), (250, 210))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

> รันดู — ต้องเห็น `D _ _` ✅
> ลองเปลี่ยน `guessed = ["D", "G"]` → ต้องได้ `D _ G`
