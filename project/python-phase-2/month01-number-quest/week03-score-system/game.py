# ============================================================
# Week 3 - Number Quest : SCORE MODE  (เฉลย)
# แนวคิด: ตัวแปรสะสม (score += / correct +=) + จัดอันดับด้วย if
# รัน: python game.py
# ============================================================
import random

print("=" * 34)
print("   NUMBER QUEST : SCORE MODE")
print("=" * 34)

# ---------- ตัวแปรของเกม ----------
score = 0        # คะแนนสะสม
correct = 0      # จำนวนด่านที่ตอบถูก
print("คะแนนเริ่มต้น:", score)

# ---------- ด่าน 1 ----------
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

# ---------- ด่าน 2 ----------
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

# ---------- ด่าน 3 ----------
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

# ---------- สรุปผล + เหรียญ ----------
if score >= 30:
    medal = "GOLD"
elif score >= 20:
    medal = "SILVER"
elif score >= 10:
    medal = "BRONZE"
else:
    medal = "ไม่มีเหรียญ"

print()
print("-" * 34)
print(f"  คะแนนรวม : {score} / 30")
print(f"  ตอบถูก   : {correct} / 3 ด่าน")
print(f"  เหรียญ   : {medal}")
print("-" * 34)
