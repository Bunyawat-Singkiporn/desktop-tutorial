# Week 2 - เช็คพอยต์ 3 : ทาย 3 ครั้ง (แบบเขียนซ้ำ)
import random

print("=== GUESS THE NUMBER ===")
print("ฉันแอบคิดเลข 1 ถึง 10 ไว้...")
print("เธอมี 3 ครั้ง!")
print()

secret = random.randint(1, 10)
won = False

# ---- ครั้งที่ 1 ----
guess = int(input("ครั้งที่ 1 - ทายเลข: "))
if guess == secret:
    print("ถูกต้อง! เก่งมาก")
    won = True
elif guess > secret:
    print("มากไป! ลองต่ำกว่านี้")
else:
    print("น้อยไป! ลองสูงกว่านี้")

# ---- ครั้งที่ 2 ----
if not won:
    guess = int(input("ครั้งที่ 2 - ทายเลข: "))
    if guess == secret:
        print("ถูกต้อง! เก่งมาก")
        won = True
    elif guess > secret:
        print("มากไป! ลองต่ำกว่านี้")
    else:
        print("น้อยไป! ลองสูงกว่านี้")

# ---- ครั้งที่ 3 ----
if not won:
    guess = int(input("ครั้งที่ 3 - ทายเลข: "))
    if guess == secret:
        print("ถูกต้อง! เก่งมาก")
        won = True
    else:
        print("หมดโอกาสแล้ว!")

# ---- สรุป ----
if not won:
    print(f"เลขลับคือ {secret}")
