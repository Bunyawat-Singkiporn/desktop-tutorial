# 1) อ่านไฟล์ครั้งแรก

## เป้าหมาย
อ่านข้อมูลจากไฟล์กลับมาใช้ในโปรแกรม

---

## แนวคิด — อ่านทั้งไฟล์

```python
with open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)
```

> `f.read()` ได้ **ข้อความก้อนเดียว** รวม `\n` มาด้วย

---

## แนวคิด — อ่านทีละบรรทัด

```python
with open("scores.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)
```

```text
['5\n', '12\n', '3\n']
```

> ได้ **list ของข้อความ** แต่ละตัวมี `\n` ติดมาด้วย 😖

---

## แนวคิด — `strip()` ตัดขยะท้ายบรรทัด

```python
line = "12\n"
clean = line.strip()      # "12"
number = int(clean)       # 12
```

```text
"12\n"  --strip()-->  "12"  --int()-->  12
ข้อความ                ข้อความ           ตัวเลข
```

> ลืม `strip()` แล้วใช้ `int("12\n")` → **ValueError** ทันที
> นี่คือบั๊กอันดับ 1 ของการอ่านไฟล์ 🐞

---

## แนวคิด — เช็กก่อนว่ามีไฟล์

```python
import os

if os.path.exists("scores.txt"):
    print("มีไฟล์")
else:
    print("ยังไม่มีไฟล์")
```

---

## 📝 สร้างไฟล์ `read_test.py`

```python
import os

FILE = "scores.txt"

# สร้างไฟล์ทดสอบก่อน
with open(FILE, "w", encoding="utf-8") as f:
    f.write("5\n")
    f.write("12\n")
    f.write("3\n")

# อ่านกลับมา
if os.path.exists(FILE):
    with open(FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        number = int(line.strip())
        print("อ่านได้:", number)
        total = total + number

    print("รวม:", total)
    print("เฉลี่ย:", total / len(lines))
else:
    print("ยังไม่มีไฟล์")
```

---

> รันดู — ต้องได้ 5, 12, 3 รวม 20 เฉลี่ย 6.666... ✅
> ลองลบไฟล์ `scores.txt` แล้วแก้บรรทัดสร้างไฟล์ออก แล้วรันใหม่ ต้องขึ้น "ยังไม่มีไฟล์" ไม่ใช่ error
