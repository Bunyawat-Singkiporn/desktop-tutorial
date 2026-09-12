# 1) เช็กคำตอบ + เก็บคะแนน

## เป้าหมาย
กด 1-4 แล้วรู้ว่าถูกหรือผิด และคะแนนขึ้น

---

## แนวคิด — เฉลยอยู่ในตัวคำถามอยู่แล้ว

```python
questions = [
    ["2 + 3 เท่ากับเท่าไร?", ["4", "5", "6", "7"], 2],
    #                                              ↑ เฉลยคือข้อ 2 ("5")
]

q = questions[index]
answer = q[2]              # 2
```

เช็กง่ายมาก:

```python
if picked == answer:
    score += 10
```

| ตัวแปร | ตัวอย่าง | มาจากไหน |
|--------|----------|----------|
| `picked` | 2 | ปุ่มที่ผู้เล่นกด |
| `answer` | 2 | `questions[index][2]` |
| `score` | 10 | สะสมทั้งเกม (ตั้ง `score = 0` นอกลูป) |

---

## ⚠️ กับดัก: ตั้งตัวแปรผิดที่

```python
running = True
while running:
    score = 0        # ❌ ผิด! คะแนนโดนล้างทุกเฟรม (60 ครั้ง/วินาที)
```

```python
score = 0            # ✅ ถูก! ตั้งครั้งเดียวก่อนเข้าลูป
running = True
while running:
    ...
```

> บั๊กเดียวกับ Week 4 เป๊ะ — "ของที่ต้องสะสม ต้องอยู่นอกลูป"

---

## 📝 แก้ `quiz.py`

**1.** เพิ่มก่อน `running = True`:

```python
score = 0
last_picked = 0        # จำว่าเพิ่งกดข้อไหน (ใช้ตอนวาดสีในสไลด์หน้า)
```

**2.** ในส่วน `if picked > 0:` **แทนที่** ด้วย:

```python
                if picked > 0:
                    last_picked = picked
                    if picked == questions[index][2]:
                        score += 10
                    index += 1
                    if index >= len(questions):
                        finished = True
```

**3.** วาดคะแนนที่มุมขวาบน — เพิ่มหลัง `screen.blit(title, (50, 40))`:

```python
    sc = font_mid.render(f"คะแนน {score}", True, "lightgreen")
    screen.blit(sc, (600, 50))
```

---

> รันดู — ตอบถูกคะแนนต้อง +10 ตอบผิดต้องเท่าเดิม ✅
> (ตอนนี้ยังไม่มี feedback บอกว่าถูก/ผิด — ต้องเดาจากคะแนน! สไลด์หน้าจะแก้)
