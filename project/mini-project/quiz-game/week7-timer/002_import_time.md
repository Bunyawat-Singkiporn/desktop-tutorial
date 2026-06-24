## เป้าหมาย

นำ `time` module มาจับเวลา

---

## แนวคิด

`time.time()` คืนค่าเวลาปัจจุบัน (วินาที)

```
start_time = time.time()    ← บันทึกเวลาเริ่ม
...
elapsed = time.time() - start_time  ← เวลาที่ใช้ไป
time_left = TIME_LIMIT - elapsed    ← เวลาที่เหลือ
```

---

## 📝 เพิ่มใน quiz.py

**1.** เพิ่มบรรทัดแรก:

```python
import time
```

**2.** เพิ่มหลัง `feedback = ""`:

```python
TIME_LIMIT = 10
start_time = time.time()
```
