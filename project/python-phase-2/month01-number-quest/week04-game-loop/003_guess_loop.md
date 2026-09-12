# 2) ทายจนกว่าจะถูก (หรือหมดโอกาส)

## เป้าหมาย
เขียนโค้ดการทาย **แค่ชุดเดียว** แล้วให้มันวนเอง

---

## แนวคิด — `while` + `break`

```python
tries = 0
while tries < 3:              # ยังเหลือโอกาส
    tries += 1
    guess = int(input(f"  ครั้งที่ {tries}: "))
    if guess == secret:
        print("  ถูกต้อง!")
        break                 # ← ออกจากลูปทันที ไม่ต้องทายต่อ
    elif guess > secret:
        print("  มากไป")
    else:
        print("  น้อยไป")
```

| คำสั่ง | ทำอะไร |
|--------|--------|
| `break` | ออกจากลูปทันที |
| `tries += 1` | นับครั้งที่ทาย → ทำให้ลูปมีวันจบ |

---

## เทียบกับ Week 2

```text
Week 2  : เขียนบล็อกทาย 3 ครั้ง = 30 บรรทัด  😩
Week 4  : เขียนบล็อกทายครั้งเดียว = 10 บรรทัด  😎
          อยากได้ 100 ครั้ง? เปลี่ยนเลข 3 เป็น 100 จบ
```

---

## รู้ได้ยังไงว่าชนะหรือแพ้?

ใช้ตัวแปรจำสถานะเหมือน Week 2

```python
won = False
...
    if guess == secret:
        won = True
        break
...
if won:
    print("  ชนะด่านนี้!")
else:
    print(f"  แพ้! เลขคือ {secret}")
```

---

## 📝 เขียน `quest.py` ใหม่

```python
import random

secret = random.randint(1, 20)
tries = 0
won = False

print("[ ด่าน 1 ] ทายเลข 1-20")
while tries < 3:
    tries += 1
    guess = int(input(f"  ครั้งที่ {tries}: "))
    if guess == secret:
        won = True
        break
    elif guess > secret:
        print("  มากไป")
    else:
        print("  น้อยไป")

if won:
    print("  ถูกต้อง! ชนะด่านนี้")
else:
    print(f"  แพ้! เลขลับคือ {secret}")
```

---

> รันดู — ทายถูกตั้งแต่ครั้งแรก ลูปต้องหยุดทันที ✅
