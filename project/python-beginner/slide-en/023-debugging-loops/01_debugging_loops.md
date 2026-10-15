# Debugging Loops ^ fix bugs in Loop

---

# Buug 1: Off-by-one #```python
# ❌ ต้องการ 1–5 แต่ได้แค่ 1–4
for i in range(1, 5):
    print(i)

# ✅ แก้
for i in range(1, 6):
    print(i)
```= 1, 2, 3, 4 = not including 5) *
> Need 1 ^5 ▪

---

♪ Buug 2: Infinite Loop```python
# ❌ ลืมอัปเดต count → วนไม่หยุด!
count = 1
while count <= 5:
    print(count)

# ✅ แก้
count = 1
while count <= 5:
    print(count)
    count = count + 1   # ← ต้องมีบรรทัดนี้
```---

#### Bug 3: Inndent Wrong```python
# ❌ print อยู่นอก loop — พิมพ์แค่ครั้งเดียว
for i in range(3):
    pass
print(i)

# ✅ แก้: indent ให้อยู่ใน loop
for i in range(3):
    print(i)
```---

## Buug 4: Use List instead of variables Walk```python
names = ["Alice", "Bob", "Charlie"]

# ❌ ผิด: ใช้ names แทน name
for name in names:
    print(names)   # แสดง list ทั้งหมดทุกรอบ!

# ✅ ถูก
for name in names:
    print(name)    # แสดงแต่ละชื่อ
```---

#### How Debug Loop

Add temporary values to each value :```python
for i in range(5):
    print(f"[debug] i = {i}")   # ← ลบออกเมื่อเสร็จแล้ว
    total = total + i
```---

# To sum up the guard #

▪ Buug
I'm sorry.
^ Off-by-one ▪
▪ Infinite log
Is that correct?
Wrong name