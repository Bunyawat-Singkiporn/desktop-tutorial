## เป้าหมาย

รับการกดปุ่ม 1-5 จากผู้เล่น

---

## แนวคิด

`if` ตรวจเงื่อนไข — เหมือนที่เรียนใน Python-beginner

```python
if event.type == pygame.KEYDOWN:     # มีการกดปุ่ม?
    if event.key == pygame.K_1:      # กดเลข 1?
        message = "You pressed 1"    # เปลี่ยนข้อความ
```

ใช้ `elif` ตรวจทีละปุ่ม (ถ้าไม่ใช่ 1 ลองดู 2, 3, 4, 5):

```python
if event.key == pygame.K_1:
    ...
elif event.key == pygame.K_2:
    ...
```

---

## วิเคราะห์ Input → Process → Output

```text
Input:   กดเลข 1
           ↓
Process: if event.key == pygame.K_1
           ↓
Output:  message = "You pressed 1"  (ข้อความเปลี่ยน)
```

---

## อธิบายโค้ด

| บรรทัด | ความหมาย |
|--------|----------|
| `pygame.KEYDOWN` | มีการกดปุ่ม |
| `pygame.K_1` | ปุ่มเลข 1 บนคีย์บอร์ด |
| `pygame.K_2` ... `pygame.K_5` | ปุ่มเลข 2-5 |
| `message = "..."` | เปลี่ยนข้อความที่แสดงบนจอ |

---

## 📝 เพิ่มใน game.py

เพิ่มใน `for event` loop **หลัง** `pygame.QUIT`:

```python
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                message = "You pressed 1"
            elif event.key == pygame.K_2:
                message = "You pressed 2"
            elif event.key == pygame.K_3:
                message = "You pressed 3"
            elif event.key == pygame.K_4:
                message = "You pressed 4"
            elif event.key == pygame.K_5:
                message = "You pressed 5"
```

> รันทดสอบ — กดเลข 1-5 แล้วข้อความควรเปลี่ยนตาม
