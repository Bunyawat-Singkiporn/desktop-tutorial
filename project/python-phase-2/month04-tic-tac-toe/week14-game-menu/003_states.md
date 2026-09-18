# 2) สลับหน้าจอ

## เป้าหมาย
เลือกเมนูแล้วไปหน้าที่ถูกต้อง และกลับมาได้

---

## แนวคิด — state เก็บว่าอยู่หน้าไหน

```python
state = "menu"       # "menu" / "howto" / "playing"
```

**ส่วน INPUT**

```python
if state == "menu":
    if event.key == pygame.K_RETURN:
        if selected == 0:
            state = "playing"
        if selected == 1:
            state = "howto"
        if selected == 2:
            running = False

elif state == "howto":
    if event.key == pygame.K_ESCAPE:
        state = "menu"

elif state == "playing":
    if event.key == pygame.K_ESCAPE:
        state = "menu"
```

**ส่วน OUTPUT**

```python
if state == "menu":
    draw_menu()
elif state == "howto":
    draw_howto()
else:
    draw_grid()
    draw_marks()
```

> โครงนี้เหมือน Quiz Arena และ Fruit Collector เป๊ะ
> **ต่างกันแค่ชื่อ state** — นี่คือโครงมาตรฐานของเกมทุกเกม 🧩

---

## ⚠️ กับดัก: Esc ที่ทำงานสองอย่าง

เดิมเรากด `Esc` เพื่อออกโปรแกรม แต่ตอนนี้ `Esc` ต้อง **กลับเมนู**

```python
if event.key == pygame.K_ESCAPE:
    if state == "menu":
        running = False        # อยู่เมนูแล้ว → ออกโปรแกรม
    else:
        state = "menu"         # อยู่หน้าอื่น → กลับเมนู
```

> ปุ่มเดียวทำงานต่างกันตาม state — เกมจริงทำแบบนี้ทั้งนั้น

---

## แนวคิด — หน้าวิธีเล่น

```python
def draw_howto():
    lines = [
        "ผู้เล่น 2 คนผลัดกันวางเครื่องหมาย",
        "ผู้เล่น 1 = X   ผู้เล่น 2 = O",
        "ใครเรียงได้ 3 ช่องติดกันก่อนชนะ",
        "แนวนอน แนวตั้ง หรือแนวทแยงก็ได้",
        "",
        "กด Esc เพื่อกลับเมนู",
    ]
    for i in range(len(lines)):
        t = font_sml.render(lines[i], True, GREY)
        screen.blit(t, (300 - t.get_width() // 2, 240 + i * 34))
```

> เก็บข้อความไว้ใน list แล้ววนวาด — เพิ่มบรรทัดง่าย ไม่ต้องคำนวณ y เอง

---

## 📝 เพิ่มใน `xo.py`

1. เพิ่ม `state = "menu"`
2. เพิ่ม `draw_howto()`
3. แยก INPUT และ OUTPUT ตาม state

---

> รันดู — เลือกข้อ 2 ต้องเข้าหน้าวิธีเล่น กด Esc กลับเมนูได้ ✅
> เลือกข้อ 3 ต้องปิดโปรแกรม
