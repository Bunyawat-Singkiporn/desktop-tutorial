# 2) เล่น 3 ด่าน เก็บคะแนน

## เป้าหมาย
แต่ละด่านสุ่มเลข 1-5 ทายถูก +10 คะแนน

---

## แนวคิด — ตัวแปร 2 ตัวทำงานคู่กัน

```python
score = 0      # คะแนน (ถูก 1 ข้อ = 10)
correct = 0    # จำนวนข้อที่ถูก (ถูก 1 ข้อ = 1)
```

ทำไมต้องมี 2 ตัว? เพราะเราอยากรู้ทั้ง **คะแนน** และ **สัดส่วนความแม่น**

---

## โครงของ 1 ด่าน

```python
print()
print("[ ด่าน 1 ]")
secret = random.randint(1, 5)
guess = int(input("ทายเลข 1-5: "))

if guess == secret:
    score += 10
    correct += 1
    print(f"ถูกต้อง! +10   คะแนนตอนนี้ = {score}")
else:
    print(f"ผิด! เลขคือ {secret}   คะแนนตอนนี้ = {score}")
```

> ด่าน 2 และ 3 = **โค้ดชุดเดียวกัน** แค่เปลี่ยนเลขด่าน
> (ใช่แล้ว ยังต้อง copy อยู่ — Week 4 เราจะใช้ `while` แก้ปัญหานี้ 🔁)

---

## 📝 เขียน `score.py` ใหม่ทั้งไฟล์

```python
import random

print("=== NUMBER QUEST : SCORE MODE ===")

score = 0
correct = 0
print("คะแนนเริ่มต้น:", score)

# ---- ด่าน 1 ----
print()
print("[ ด่าน 1 ]")
secret = random.randint(1, 5)
guess = int(input("ทายเลข 1-5: "))
if guess == secret:
    score += 10
    correct += 1
    print(f"ถูกต้อง! +10   คะแนนตอนนี้ = {score}")
else:
    print(f"ผิด! เลขคือ {secret}   คะแนนตอนนี้ = {score}")

# ---- ด่าน 2 ----
print()
print("[ ด่าน 2 ]")
secret = random.randint(1, 5)
guess = int(input("ทายเลข 1-5: "))
if guess == secret:
    score += 10
    correct += 1
    print(f"ถูกต้อง! +10   คะแนนตอนนี้ = {score}")
else:
    print(f"ผิด! เลขคือ {secret}   คะแนนตอนนี้ = {score}")

# ---- ด่าน 3 ----
print()
print("[ ด่าน 3 ]")
secret = random.randint(1, 5)
guess = int(input("ทายเลข 1-5: "))
if guess == secret:
    score += 10
    correct += 1
    print(f"ถูกต้อง! +10   คะแนนตอนนี้ = {score}")
else:
    print(f"ผิด! เลขคือ {secret}   คะแนนตอนนี้ = {score}")

print()
print("คะแนนรวม:", score)
```

---

> รันดู — คะแนนต้องสะสมข้ามด่าน ✅
> **ห้าม** เขียน `score = 0` ซ้ำระหว่างด่าน ไม่งั้นคะแนนจะถูกล้างทิ้ง!
