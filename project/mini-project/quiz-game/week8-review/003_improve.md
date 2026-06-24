## เป้าหมาย

สลับลำดับคำถามทุกครั้งที่เล่น ด้วย `random.shuffle()`

---

## แนวคิด

ต้องจับ `questions`, `choices`, `answers` เป็นคู่ก่อน ไม่งั้น index จะไม่ตรงกัน

```python
pairs = list(zip(questions, choices, answers))
random.shuffle(pairs)
questions = [p[0] for p in pairs]
choices   = [p[1] for p in pairs]
answers   = [p[2] for p in pairs]
```

`zip()` จับคู่ 3 lists พร้อมกัน  
`shuffle()` สลับลำดับ  
แล้วแยกกลับออกมาทีละ list

---

## 📝 เพิ่มใน quiz.py

**1.** เพิ่ม `import random` ใต้ `import time`

**2.** เพิ่ม **หลัง** `answers = [...]` ก่อน `current_q = 0`:

```python
pairs = list(zip(questions, choices, answers))
random.shuffle(pairs)
questions = [p[0] for p in pairs]
choices   = [p[1] for p in pairs]
answers   = [p[2] for p in pairs]
```

> รันหลายรอบ — ลำดับคำถามควรเปลี่ยนทุกครั้ง
