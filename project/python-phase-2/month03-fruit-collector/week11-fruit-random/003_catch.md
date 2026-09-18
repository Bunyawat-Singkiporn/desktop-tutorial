# 2) รับผลไม้ให้ได้ + คะแนน

## เป้าหมาย
ผลไม้ที่ตกลงตะกร้าต้องหายไปและได้คะแนน

---

## แนวคิด — การชนต้องจริงทั้ง 2 แกน

ผลไม้จะถือว่า "ลงตะกร้า" ก็ต่อเมื่อ **ตรงกันทั้งแนวตั้งและแนวนอน**

```text
แนวตั้ง (y)                     แนวนอน (x)
  ผลไม้ตกถึงระดับตะกร้าแล้ว       ผลไม้อยู่ในช่วงความกว้างตะกร้า

        ●                          │◄── basket_x ──►│
        │                          │   [=========]  │
   ─────┴─────  ← ระดับตะกร้า      │        ●       │  ✅ รับได้
                                   │                │
                                   │ ●              │  ❌ พลาด
```

```python
hit_y = fruit[1] > basket_y and fruit[1] < basket_y + BASKET_H + 10
hit_x = fruit[0] > basket_x and fruit[0] < basket_x + BASKET_W

if hit_y and hit_x:
    score = score + 1
```

> `and` แปลว่า **ต้องจริงทั้งคู่** — ขาดข้อใดข้อหนึ่งถือว่าพลาด

---

## แนวคิด — รับได้แล้วต้องเกิดใหม่ทันที

ถ้าไม่ย้ายผลไม้ออกไป มันจะยังอยู่ในตะกร้าและได้คะแนนรัวๆ ทุกเฟรม 😱

```python
if hit_y and hit_x:
    score = score + 1
    fruit[0] = random.randint(20, 780)     # เกิดใหม่ทันที
    fruit[1] = random.randint(-400, -20)
    fruit[2] = random.randint(2, 6)
```

> บั๊กนี้ชื่อว่า "คะแนนพุ่ง 60 แต้มต่อวินาที" เจอกันทุกคน 😂

---

## แนวคิด — โค้ดเกิดใหม่ใช้ซ้ำ 2 ที่

ตอนนี้เรามีโค้ด "เกิดใหม่" อยู่ 2 จุด — ตอนรับได้ และตอนตกพื้น

```python
    for fruit in fruits:
        fruit[1] = fruit[1] + fruit[2]

        caught = fruit[1] > basket_y and fruit[1] < basket_y + BASKET_H + 10 \
                 and fruit[0] > basket_x and fruit[0] < basket_x + BASKET_W
        missed = fruit[1] > 620

        if caught:
            score = score + 1
        if caught or missed:
            fruit[0] = random.randint(20, 780)
            fruit[1] = random.randint(-400, -20)
            fruit[2] = random.randint(2, 6)
```

> เขียนเงื่อนไขแยกไว้ในตัวแปรก่อน แล้วค่อยใช้ — อ่านง่ายกว่า `if` ยาวเหยียดเยอะ
> เดือน 4 จะได้เรียน `def` ซึ่งทำให้เรื่องนี้สวยกว่านี้อีก

---

## 📝 แก้ `fruit.py`

1. เพิ่ม `score = 0` **ก่อน** `running = True`
2. แทนก้อนที่ทำให้ผลไม้ตก ด้วยโค้ดข้างบน
3. วาดคะแนน: `screen.blit(font.render(f"คะแนน {score}", True, "yellow"), (20, 18))`

---

> รันดู — รับผลไม้แล้วคะแนนต้องขึ้น **ทีละ 1** ไม่ใช่พุ่งรัว ✅
