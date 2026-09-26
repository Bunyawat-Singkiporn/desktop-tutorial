age = int(input())
score = int(input())

if age >= 18 and score >= 80:
    rank = "Gold"
elif age >= 18 and score >= 60:
    rank = "Silver"
else:
    rank = "Bronze"

print(f"Score : {score}")
print(f"Rank  : {rank}")
