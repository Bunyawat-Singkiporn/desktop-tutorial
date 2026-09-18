# 3) ตรวจเสมอ + ประกาศผล

## เป้าหมาย
กระดานเต็มแต่ไม่มีใครชนะ = เสมอ และแสดงผลให้สวย

---

## แนวคิด — กระดานเต็มหรือยัง

```python
def board_full():
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                return False        # เจอช่องว่าง = ยังไม่เต็ม
    return True                     # ไล่ครบ 9 ช่องไม่เจอช่องว่าง = เต็ม
```

> เทคนิค **"เจอข้อขัดแย้งแล้วออกทันที"** — เจอช่องว่างแค่ช่องเดียวก็ตอบได้เลย
> ไม่ต้องไล่ให้ครบ 9 ช่อง

---

## ⚠️ ลำดับการตรวจสำคัญมาก

```python
winner = check_winner()
if winner != "":
    state = "result"           # ✅ ตรวจผู้ชนะก่อน
elif board_full():
    winner = "draw"            # แล้วค่อยตรวจเสมอ
    state = "result"
else:
    ...สลับตา...
```

```text
❌ ตรวจเสมอก่อน
   ถ้าช่องสุดท้ายเป็นช่องที่ทำให้ชนะพอดี
   → กระดานเต็ม → ประกาศเสมอ ทั้งที่มีคนชนะ!

✅ ตรวจผู้ชนะก่อนเสมอ
```

> บั๊กนี้เจอกันทุกคนที่ทำเกมนี้ครั้งแรก 😅

---

## แนวคิด — จอประกาศผล

```python
def draw_result():
    pygame.draw.rect(screen, PANEL, (70, 230, 460, 200), border_radius=14)
    if winner == "draw":
        text = "เสมอ!"
        color = GREY
    elif winner == "X":
        text = "ผู้เล่น 1 (X) ชนะ!"
        color = XCOL
    else:
        text = "ผู้เล่น 2 (O) ชนะ!"
        color = OCOL
    t = font_big.render(text, True, color)
    screen.blit(t, (300 - t.get_width() // 2, 275))
```

> ใช้ `elif` ต่อกัน 3 กรณี — สะอาดกว่า `if` ซ้อน `if`

---

## แนวคิด — เก็บสถิติ

```python
score_x = 0
score_o = 0
score_draw = 0
```

ตอนจบเกมบวกให้ถูกฝั่ง (ใช้ guard กันบวกซ้ำทุกเฟรม)

```python
    if winner == "X":
        score_x = score_x + 1
    elif winner == "O":
        score_o = score_o + 1
    else:
        score_draw = score_draw + 1
```

> เกม 2 คนต้องมีสถิติ ไม่งั้นเล่นจบแล้วไม่รู้ว่าใครเก่งกว่า

---

## 📝 แก้ `xo.py`

1. เพิ่ม `board_full()`
2. ตรวจผู้ชนะ **ก่อน** ตรวจเสมอ
3. เพิ่ม state `result` + `draw_result()`
4. เพิ่มสถิติ 3 ตัว

---

> เล่นจนเสมอให้ได้ 1 ครั้ง และเล่นจนชนะให้ได้ทั้ง X และ O ✅
> สถิติต้องบวกทีละ 1 ไม่ใช่พุ่งรัว
