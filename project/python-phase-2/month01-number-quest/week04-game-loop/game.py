# ============================================================
# Week 4 - NUMBER QUEST v1.0  (เฉลย / เกมสมบูรณ์ของเดือน 1)
# แนวคิด: while loop + break + ลูปซ้อนลูป + ตัวแปรสะสม
# รัน: python game.py
# ============================================================
import random

print("=" * 28)
print("      NUMBER QUEST v1.0")
print("=" * 28)
print("ทายเลข 1-20 ให้ถูกภายใน 3 ครั้ง")
print("ทายไวได้คะแนนเยอะ: 10 / 8 / 6")

# ---------- ตัวแปรสะสมทั้งเกม (นอกลูป) ----------
score = 0
rounds = 0
wins = 0
playing = True

# ---------- ลูปนอก : ด่าน ----------
while playing:
    rounds += 1

    # ตัวแปรของด่านนี้ (รีเซ็ตทุกด่าน)
    secret = random.randint(1, 20)
    tries = 0
    won = False

    print()
    print(f"[ ด่าน {rounds} ]  ทายเลข 1-20")

    # ---------- ลูปใน : การทาย ----------
    while tries < 3:
        tries += 1
        guess = int(input(f"  ครั้งที่ {tries}: "))

        if guess == secret:
            won = True
            break                      # ถูกแล้ว ออกจากลูปทันที
        elif guess > secret:
            print("  -> มากไป")
        else:
            print("  -> น้อยไป")

    # ---------- สรุปด่าน ----------
    if won:
        points = 10 - (tries - 1) * 2  # 10 / 8 / 6
        score += points
        wins += 1
        print(f"  -> ถูกต้อง! +{points} คะแนน   (คะแนนรวม {score})")
    else:
        print(f"  -> หมดโอกาส! เลขลับคือ {secret}   (คะแนนรวม {score})")

    # ---------- ถามเล่นต่อ ----------
    answer = input("เล่นด่านต่อไปไหม? (y/n): ")
    if answer != "y":
        playing = False

# ---------- สรุปรวมทั้งเกม ----------
if score >= 25:
    medal = "GOLD"
elif score >= 15:
    medal = "SILVER"
elif score >= 5:
    medal = "BRONZE"
else:
    medal = "ไม่มีเหรียญ"

print()
print("-" * 28)
print(f"  ด่านที่เล่น : {rounds}")
print(f"  ชนะ        : {wins}")
print(f"  คะแนนรวม   : {score}")
print(f"  เหรียญ     : {medal}")
print("-" * 28)
print("ขอบคุณที่เล่น NUMBER QUEST!")
