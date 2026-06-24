## เป้าหมาย

หมดเวลา → ข้ามข้ออัตโนมัติ

---

## แนวคิด

ตรวจ `elapsed > TIME_LIMIT` **นอก** event loop (game loop รันทุก frame)

ถ้าหมดเวลา: แสดง feedback, เลื่อน `current_q += 1`, reset `start_time`

---

## 📝 เพิ่มใน quiz.py

เพิ่ม **หลัง** `time_left = ...` ก่อน `screen.fill`:

```python
    if current_q < len(questions) and elapsed > TIME_LIMIT:
        feedback = "Time's up! Answer: " + choices[current_q][answers[current_q]]
        current_q += 1
        start_time = time.time()   # รีเซ็ตนาฬิกา
```

เพิ่ม **reset** timer ในบล็อกกดปุ่มด้วย (**หลัง** `current_q += 1`):

```python
                current_q += 1
                start_time = time.time()   # ← เพิ่ม
```

> รันทดสอบ — ลองนั่งว่าง 10+ วินาที ควรไปอัตโนมัติ
