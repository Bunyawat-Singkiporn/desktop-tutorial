# ⏳ while Loop — วนซ้ำตามเงื่อนไข

---

## while Loop คืออะไร?

`while` วนซ้ำ **ตราบเท่าที่เงื่อนไขยังเป็น True**

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

ผลลัพธ์:
```
1
2
3
4
5
```

---

## โครงสร้าง while Loop

```python
while เงื่อนไข:
    # โค้ดที่ทำซ้ำ
    # ต้องมีการเปลี่ยนแปลงตัวแปรเสมอ!
```

---

## for vs while

| | `for` | `while` |
|--|-------|---------|
| **ใช้เมื่อ** | รู้จำนวนรอบแน่นอน | วนจนเงื่อนไขเป็น False |
| **ตัวอย่าง** | นับ 1–10 | รับ input ซ้ำจนถูก |

---

## ตัวอย่าง: Countdown

```python
count = 5

while count > 0:
    print(count)
    count = count - 1

print("Blast off! 🚀")
```

ผลลัพธ์:
```
5
4
3
2
1
Blast off! 🚀
```

---

## ตัวอย่าง: รับ Input จนกว่าจะถูก

```python
secret = 42
guess = int(input())

while guess != secret:
    print("Wrong! Try again.")
    guess = int(input())

print("Correct!")
```

---

## ⚠️ ระวัง: Infinite Loop

```python
# ❌ วนไม่หยุด — ลืมเพิ่ม count!
count = 1
while count <= 5:
    print(count)
    # ไม่มี count = count + 1 → เงื่อนไขเป็น True ตลอด

# ✅ ถูกต้อง
count = 1
while count <= 5:
    print(count)
    count = count + 1   # ← ต้องมีบรรทัดนี้เสมอ!
```

> กด **Ctrl + C** เพื่อหยุดโปรแกรมที่ค้าง
