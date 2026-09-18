# 1) รายการเมนูและตัวชี้

## เป้าหมาย
แสดงเมนู 3 ข้อ แล้วเลื่อนตัวชี้ขึ้น-ลงด้วยปุ่มลูกศร

---

## แนวคิด — เก็บเมนูไว้ใน list

```python
menu_items = ["เริ่มเกมใหม่", "วิธีเล่น", "ออกจากเกม"]
selected = 0        # ตอนนี้ชี้อยู่ข้อไหน (0 = ข้อแรก)
```

> อยากเพิ่มเมนู "ตั้งค่า" → เพิ่มใน list เท่านั้น
> โค้ดวาดและโค้ดเลื่อนตัวชี้ **ไม่ต้องแก้เลยสักตัวอักษร** ♻️

---

## แนวคิด — วาดเมนูด้วยฟังก์ชัน

```python
def draw_menu():
    for i in range(len(menu_items)):
        y = 280 + i * 55
        if i == selected:
            text = "▸ " + menu_items[i]
            color = "yellow"
        else:
            text = "   " + menu_items[i]
            color = GREY
        t = font_mid.render(text, True, color)
        screen.blit(t, (200, y))
```

```text
selected = 0          selected = 1
▸ เริ่มเกมใหม่           เริ่มเกมใหม่
  วิธีเล่น            ▸ วิธีเล่น
  ออกจากเกม             ออกจากเกม
```

> `i == selected` คือหัวใจ — ข้อที่ตรงกับตัวชี้วาดคนละแบบ

---

## แนวคิด — เลื่อนแบบวนรอบด้วย `%`

```python
if event.key == pygame.K_DOWN:
    selected = (selected + 1) % len(menu_items)
if event.key == pygame.K_UP:
    selected = (selected - 1) % len(menu_items)
```

```text
มี 3 ข้อ (0, 1, 2)

selected = 2, กดลง  →  (2 + 1) % 3 = 0   ← วนกลับข้อแรก 🔄
selected = 0, กดขึ้น →  (0 - 1) % 3 = 2   ← วนไปข้อสุดท้าย
```

> ถ้าไม่ใช้ `%` ต้องเขียน `if selected > 2: selected = 0` เพิ่มอีก 2 บล็อก
> `%` ทำให้เมนูกี่ข้อก็ได้ โดยไม่ต้องแก้โค้ด

---

## 📝 เพิ่มใน `xo.py`

1. เพิ่ม `menu_items` และ `selected = 0`
2. เพิ่มฟังก์ชัน `draw_menu()`
3. ในลูป event รับปุ่มขึ้น-ลง
4. ในส่วนวาด เรียก `draw_menu()`

---

> รันดู — ตัวชี้ `▸` ต้องเลื่อนขึ้น-ลงได้ และวนรอบเมื่อถึงข้อสุดท้าย ✅
