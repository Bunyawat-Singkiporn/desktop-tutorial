round1 = int(input())
round2 = int(input())

round_total = round1 + round2

if round_total % 2 == 0:
    bonus1 = 10
else:
    bonus1 = 5

if round1 % 2 == 0:
    bonus2 = 20
else:
    bonus2 = 0

bonus = bonus1 + bonus2
final_score = round_total + bonus

print("========================")
print("       GAME SCORE")
print("========================")
print(f"Round Total : {round_total}")
print(f"Bonus       : {bonus}")
print(f"Final Score : {final_score}")
print("========================")
