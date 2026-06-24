# Week 5 — Quiz Game (Basic)

## วันนี้จะสร้างอะไร

Quiz game แบบ multiple choice ด้วย pygame — กด 1/2/3/4 เลือกคำตอบ

---

## Recap จาก Guessing Game

- `pygame.init()` + `screen` + game loop
- `font.render()` แสดงข้อความ
- `KEYDOWN` ตรวจการกดปุ่ม

---

## เป้าหมายวันนี้

1. สร้างหน้าต่างเกม
2. แสดงคำถามและตัวเลือก 4 ข้อ
3. กด 1/2/3/4 → ตรวจถูก/ผิด

---

## ผลลัพธ์ที่จะได้

```
[หน้าต่าง pygame สีขาว]

What is 2 + 2?

1. 2
2. 3
3. 4
4. 5

[กด 3 → แสดง Correct! สีเขียว ข้างล่าง]
```
