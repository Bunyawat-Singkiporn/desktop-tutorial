# 🛡️ Loop Safety — ควบคุม Loop ให้ปลอดภัย

---

## break — หยุด Loop ทันที

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

ผลลัพธ์:
```
0
1
2
3
4
```

> `break` ออกจาก loop ทันที ไม่ทำรอบที่เหลือ

---

## continue — ข้ามรอบนี้

```python
for i in range(6):
    if i == 3:
        continue
    print(i)
```

ผลลัพธ์:
```
0
1
2
4
5
```

> `continue` ข้ามรอบนี้แล้วไปรอบถัดไป (ไม่ออกจาก loop)

---

## break vs continue

| คำสั่ง | ผล |
|--------|-----|
| `break` | หยุด loop ทันที — ออกเลย |
| `continue` | ข้ามรอบนี้ — วนต่อรอบหน้า |

---

## while True + break

รับ Input ซ้ำจนผู้ใช้พิมพ์ `"quit"`:

```python
while True:
    word = input()
    if word == "quit":
        break
    print("You typed:", word)

print("Goodbye!")
```

```
hello → You typed: hello
world → You typed: world
quit  → Goodbye!
```

---

## continue — กรองค่า

แสดงเฉพาะเลขคี่:

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue     # ข้ามเลขคู่
    print(i)
```

ผลลัพธ์:
```
1
3
5
7
9
```

---

## Loop Safety Checklist

- [ ] `while` ต้องมีตัวแปรเปลี่ยนค่าในทุกรอบ
- [ ] ใช้ `break` เมื่อต้องการหยุดกลางคัน
- [ ] ใช้ `continue` เมื่อต้องการข้ามบางรอบ
- [ ] ทดสอบด้วย input หลายค่า
