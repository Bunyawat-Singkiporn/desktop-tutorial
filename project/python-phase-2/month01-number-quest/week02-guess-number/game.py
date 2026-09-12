# ============================================================
# Week 2 - Number Quest : GUESS THE NUMBER  (เฉลย)
# แนวคิด: random + if/elif/else + ตัวแปรจำสถานะ (True/False)
# รัน: python game.py
# ============================================================
import random

print("=" * 30)
print("   GUESS THE NUMBER")
print("=" * 30)
print("ฉันแอบคิดเลข 1 ถึง 10 ไว้...")
print("เธอมี 3 ครั้ง!")
print()

secret = random.randint(1, 10)
won = False


# ---------- ครั้งที่ 1 ----------
guess = int(input("ครั้งที่ 1 - ทายเลข: "))
if guess == secret:
    print("ถูกต้อง! เก่งมาก 🎉")
    won = True
elif guess > secret:
    print("มากไป! ลองต่ำกว่านี้")
else:
    print("น้อยไป! ลองสูงกว่านี้")

# ---------- ครั้งที่ 2 ----------
if not won:
    print()
    guess = int(input("ครั้งที่ 2 - ทายเลข: "))
    if guess == secret:
        print("ถูกต้อง! เก่งมาก 🎉")
        won = True
    elif guess > secret:
        print("มากไป! ลองต่ำกว่านี้")
    else:
        print("น้อยไป! ลองสูงกว่านี้")

# ---------- ครั้งที่ 3 (ครั้งสุดท้าย) ----------
if not won:
    print()
    guess = int(input("ครั้งที่ 3 - ทายเลข: "))
    if guess == secret:
        print("ถูกต้อง! เก่งมาก 🎉")
        won = True
    else:
        print("หมดโอกาสแล้ว!")

# ---------- สรุปผล ----------
print()
print("-" * 30)
if won:
    print("  ผลลัพธ์: ชนะ")
else:
    print("  ผลลัพธ์: แพ้")
    print(f"  เลขลับคือ {secret}")
print("-" * 30)
