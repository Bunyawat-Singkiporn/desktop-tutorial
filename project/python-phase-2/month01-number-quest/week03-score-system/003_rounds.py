# Week 3 - เช็คพอยต์ 2 : เล่น 3 ด่าน
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
