# 🔲 Nested Loops — Loop ซ้อน Loop

---

## Nested Loop คืออะไร?

**Nested Loop** คือ loop ที่อยู่ภายใน loop อีกอัน

```python
for i in range(3):        # Loop นอก — วน 3 รอบ
    for j in range(3):    # Loop ใน — วน 3 รอบ ทุกครั้ง
        print(i, j)
```

ผลลัพธ์:
```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

> Loop ใน **วนครบทุกรอบ** ก่อนที่ loop นอกจะไปรอบถัดไป

---

## จำนวนรอบรวม

```
Loop นอก 3 รอบ × Loop ใน 4 รอบ = 12 ครั้งรวม
```

```python
for row in range(3):
    for col in range(4):
        print("*", end="")
    print()    # ขึ้นบรรทัดใหม่
```

ผลลัพธ์:
```
****
****
****
```

---

## ตัวอย่าง: Pattern สามเหลี่ยม

```python
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()
```

ผลลัพธ์:
```
*
**
***
****
*****
```

> `range(row)` — loop ใน วนตาม row ปัจจุบัน

---

## ตัวอย่าง: ตารางสูตรคูณ

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
```

ผลลัพธ์:
```
1	2	3	
2	4	6	
3	6	9	
```

---

## สรุป

| เรื่อง | ตัวอย่าง |
|-------|---------|
| Loop นอก | วน N รอบ |
| Loop ใน | วน M รอบ ทุกครั้งที่ loop นอกวน |
| รวม | N × M ครั้ง |
| `end=""` | พิมพ์ในบรรทัดเดียว |
| `print()` ว่าง | ขึ้นบรรทัดใหม่ |
