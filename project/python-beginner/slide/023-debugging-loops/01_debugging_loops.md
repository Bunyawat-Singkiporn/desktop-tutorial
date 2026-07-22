# 🐛 Debugging Loops — แก้บั๊กใน Loop

---

## Bug 1: Off-by-One Error

```python
# ❌ ต้องการ 1–5 แต่ได้แค่ 1–4
for i in range(1, 5):
    print(i)

# ✅ แก้
for i in range(1, 6):
    print(i)
```

> `range(1, 5)` = 1, 2, 3, 4 — **ไม่รวม 5**
> ต้องการ 1–5 ต้องใช้ `range(1, 6)`

---

## Bug 2: Infinite Loop

```python
# ❌ ลืมอัปเดต count → วนไม่หยุด!
count = 1
while count <= 5:
    print(count)

# ✅ แก้
count = 1
while count <= 5:
    print(count)
    count = count + 1   # ← ต้องมีบรรทัดนี้
```

---

## Bug 3: Indent ผิด

```python
# ❌ print อยู่นอก loop — พิมพ์แค่ครั้งเดียว
for i in range(3):
    pass
print(i)

# ✅ แก้: indent ให้อยู่ใน loop
for i in range(3):
    print(i)
```

---

## Bug 4: ใช้ชื่อ List แทนตัวแปรวน

```python
names = ["Alice", "Bob", "Charlie"]

# ❌ ผิด: ใช้ names แทน name
for name in names:
    print(names)   # แสดง list ทั้งหมดทุกรอบ!

# ✅ ถูก
for name in names:
    print(name)    # แสดงแต่ละชื่อ
```

---

## วิธี Debug Loop

เพิ่ม `print` ชั่วคราวดูค่าในแต่ละรอบ:

```python
for i in range(5):
    print(f"[debug] i = {i}")   # ← ลบออกเมื่อเสร็จแล้ว
    total = total + i
```

---

## สรุป Bug ที่ต้องระวัง

| Bug | สัญญาณ | วิธีแก้ |
|-----|--------|--------|
| Off-by-one | ได้ผลน้อย/มากกว่า 1 รอบ | ตรวจค่าใน `range()` |
| Infinite loop | โปรแกรมค้าง | ตรวจว่ามีการเปลี่ยนตัวแปร |
| Indent ผิด | โค้ดทำงานแปลก | ตรวจ space นำหน้า |
| ชื่อผิด | Output แปลก | ตรวจชื่อตัวแปร |
