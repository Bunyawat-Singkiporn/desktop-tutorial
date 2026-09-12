# Week 4 - เช็คพอยต์ 2 : ทายจนกว่าจะถูก
import random

secret = random.randint(1, 20)
tries = 0
won = False

print("[ ด่าน 1 ] ทายเลข 1-20")
while tries < 3:
    tries += 1
    guess = int(input(f"  ครั้งที่ {tries}: "))
    if guess == secret:
        won = True
        break
    elif guess > secret:
        print("  มากไป")
    else:
        print("  น้อยไป")

if won:
    print("  ถูกต้อง! ชนะด่านนี้")
else:
    print(f"  แพ้! เลขลับคือ {secret}")
