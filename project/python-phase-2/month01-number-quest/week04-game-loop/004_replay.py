# Week 4 - เช็คพอยต์ 3 : เล่นหลายด่าน (ลูปซ้อนลูป)
import random

score = 0
rounds = 0
wins = 0
playing = True

while playing:
    rounds += 1
    secret = random.randint(1, 20)
    tries = 0
    won = False

    print()
    print(f"[ ด่าน {rounds} ] ทายเลข 1-20")

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
        points = 10 - (tries - 1) * 2
        score += points
        wins += 1
        print(f"  ถูกต้อง! +{points} คะแนน (รวม {score})")
    else:
        print(f"  แพ้! เลขลับคือ {secret} (รวม {score})")

    answer = input("เล่นด่านต่อไปไหม? (y/n): ")
    if answer != "y":
        playing = False

print()
print(f"เล่นไป {rounds} ด่าน ชนะ {wins} ด่าน คะแนนรวม {score}")
