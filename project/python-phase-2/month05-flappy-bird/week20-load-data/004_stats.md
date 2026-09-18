# 3) สถิติจากประวัติการเล่น

## เป้าหมาย
อ่านไฟล์ประวัติมาคำนวณ จำนวนรอบ / คะแนนเฉลี่ย / คะแนนสูงสุด

---

## แนวคิด — อ่าน CSV ทีละบรรทัด

ไฟล์ประวัติหน้าตาแบบนี้

```text
5,ปกติ
12,ยาก
3,ง่าย
```

อ่านมาแล้วเอาเฉพาะตัวเลขข้างหน้า

```python
def load_stats():
    rounds = 0
    total = 0
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            rounds = rounds + 1
            total = total + int(parts[0])
    return rounds, total
```

| โค้ด | ทำอะไร |
|------|--------|
| `line.strip()` | ตัด `\n` |
| `if line == "": continue` | ข้ามบรรทัดว่าง |
| `line.split(",")` | แยกเป็น `["12", "ยาก"]` |
| `parts[0]` | เอาเฉพาะคะแนน |

> `split(",")` คือการ **หั่นข้อความตามตัวคั่น** — เครื่องมือหลักของการอ่านข้อมูล 📊

---

## แนวคิด — ระวังหารด้วยศูนย์

```python
rounds, total = load_stats()

if rounds > 0:
    average = total / rounds
else:
    average = 0
```

> เปิดเกมครั้งแรก `rounds = 0` → `total / 0` = **ZeroDivisionError** 💥
> กฎ: ก่อนหารทุกครั้ง ถามตัวเองว่า "ตัวหารเป็น 0 ได้ไหม"

---

## แนวคิด — แสดงทศนิยมให้พอดี

```python
t = font_sml.render(f"คะแนนเฉลี่ย : {average:.1f}", True, DARK)
```

```text
8.666666666  →  {average:.1f}  →  8.7
```

> `:.1f` = ทศนิยม 1 ตำแหน่ง อ่านง่ายกว่าเลขยาวเป็นพรืด

---

## แนวคิด — อัปเดตสถิติหลังจบเกม

```python
    if state == "gameover":
        save_history()
        rounds, total = load_stats()      # โหลดใหม่ให้ตัวเลขบนจอตรงกับไฟล์
```

> หรือจะบวกในตัวแปรเลยก็ได้ (เร็วกว่า) แต่การโหลดใหม่ **การันตีว่าตรงกับไฟล์จริง** เสมอ

---

## 📝 แก้ `flappy.py`

1. เพิ่ม `load_stats()`
2. เรียกตอนเปิดโปรแกรมและหลังจบเกม
3. ทำหน้าเมนูที่โชว์ สถิติสูงสุด / จำนวนรอบ / คะแนนเฉลี่ย

---

> เล่น 5 รอบ ปิดโปรแกรม เปิดใหม่ — ต้องเห็นว่าเล่นไป 5 รอบ พร้อมคะแนนเฉลี่ย ✅
