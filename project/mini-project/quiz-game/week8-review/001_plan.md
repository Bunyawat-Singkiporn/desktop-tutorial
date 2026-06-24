# Week 8 — Review & Improve

## Recap Week 7

```python
import time

TIME_LIMIT = 10
start_time = time.time()

# ใน game loop (นอก event loop):
elapsed   = time.time() - start_time
time_left = max(0, TIME_LIMIT - elapsed)

# ถ้าหมดเวลา:
if current_q < len(questions) and elapsed > TIME_LIMIT:
    feedback = "Time's up! ..."
    current_q += 1
    start_time = time.time()
```

---

## เป้าหมายวันนี้

1. หา bug จากโค้ดที่มีปัญหา
2. เพิ่ม `random.shuffle()` สลับลำดับคำถาม

---

## ผลลัพธ์ที่จะได้

```
[ลำดับคำถามเปลี่ยนทุกครั้งที่รันเกม]

How many months in a year?     ← ไม่ได้เริ่มที่ข้อเดิมทุกครั้ง
```
