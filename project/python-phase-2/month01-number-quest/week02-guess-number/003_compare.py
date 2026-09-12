# Week 2 - เช็คพอยต์ 2 : ทาย 1 ครั้ง
import random

print("=== GUESS THE NUMBER ===")
print("ฉันแอบคิดเลข 1 ถึง 10 ไว้...")

secret = random.randint(1, 10)

guess = int(input("ทายเลข: "))

if guess == secret:
    print("ถูกต้อง! เก่งมาก")
elif guess > secret:
    print("มากไป! ลองต่ำกว่านี้")
else:
    print("น้อยไป! ลองสูงกว่านี้")
