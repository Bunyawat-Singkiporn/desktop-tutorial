# 3) ทำให้เหตุการณ์มีผลจริง

## เป้าหมาย
เหตุการณ์ที่สุ่มได้ต้องเปลี่ยนเกมจริงๆ

---

## แนวคิด — ใช้เหตุการณ์ตอนเริ่มด่าน

```python
def_lives = MAX_LIVES        # (ยังไม่ใช้ def นะ นี่แค่ตัวแปร!)

# ตอนเริ่มด่านใหม่
guessed = []
lives = MAX_LIVES
multiplier = 1
event = random.choice(events)

if event[0] == "lucky":
    # เปิดตัวอักษรให้ฟรี 1 ตัว
    free = random.choice(words[level][0])    # สุ่มตัวอักษรจากคำ
    guessed.append(free)

elif event[0] == "bless":
    lives += 1

elif event[0] == "trap":
    lives -= 1

elif event[0] == "bonus":
    multiplier = 2
```

> `random.choice("RAINBOW")` ก็ใช้ได้! เพราะ string ก็เป็น "ลิสต์ของตัวอักษร" 🎯

---

## แนวคิด — ตัวคูณคะแนน

```python
points = (len(word) + lives * 2) * multiplier
score += points
```

| คำ | ชีวิต | multiplier | คะแนน |
|----|-------|-----------|-------|
| DOG (3) | 6 | 1 | 15 |
| DOG (3) | 6 | 2 | **30** |

---

## ⚠️ อย่าลืมรีเซ็ต multiplier

```python
multiplier = 1      # ← ตอนขึ้นด่านใหม่ต้องกลับเป็น 1
```

ไม่งั้นโบนัสจะติดตัวไปตลอดทั้งเกม 😅

---

## แนวคิด — สีตามชนิดเหตุการณ์

```python
if event[0] == "trap":
    ev_color = "salmon"
elif event[0] == "none":
    ev_color = GREY
else:
    ev_color = "orange"
```

> ผู้เล่นควร **รู้ทันทีจากสี** ว่าเจอของดีหรือของร้าย

---

## 📝 แก้ `game.py`

1. เพิ่ม `multiplier = 1`
2. ใส่ผลของเหตุการณ์ตอนเริ่มด่าน (และตอนกด R)
3. คูณคะแนนด้วย `multiplier`
4. ใส่สีตามชนิดเหตุการณ์

---

> รันหลายรอบจนเจอครบทุกเหตุการณ์ ✅
> เจอ "โชคดี" → ต้องมีตัวอักษรเปิดไว้ให้ตั้งแต่ต้นด่าน
> เจอ "โบนัส" → คะแนนที่ได้ต้องเป็น 2 เท่า

---

## 💡 เทคนิค: ธง `new_stage` (ใช้ในเฉลย)

โค้ดเริ่มด่านต้องใช้ถึง 3 ที่ (เริ่มเกม / ขึ้นด่านใหม่ / กด R) — copy 3 รอบก็เหนื่อย

แทนที่จะ copy ใช้ **ธง** แทน:

```python
new_stage = True        # ธง: "ขอเริ่มด่านใหม่หน่อย"

while running:
    # ...ในส่วน INPUT...
    #   ตอนกด Space ขึ้นด่าน  →  new_stage = True
    #   ตอนกด R              →  new_stage = True

    # ...ในส่วน PROCESS (เขียนที่เดียว!)...
    if new_stage:
        new_stage = False
        guessed = []
        lives = MAX_LIVES
        multiplier = 1
        event = random.choice(events)
        ...ใส่ผลของเหตุการณ์...
```

> ต้องเซ็ต `new_stage = False` **บรรทัดแรก** ไม่งั้นจะรีเซ็ตซ้ำทุกเฟรม!
>
> เดือน 4 เราจะได้เรียน `def` (ฟังก์ชัน) ซึ่งแก้ปัญหานี้ได้สวยกว่านี้อีก 🔧
