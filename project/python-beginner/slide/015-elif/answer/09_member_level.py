points = int(input())

if points >= 1000:
    level = "Gold"
elif points >= 500:
    level = "Silver"
elif points >= 100:
    level = "Bronze"
else:
    level = "Member"

print(f"Points : {points}")
print(f"Level  : {level}")
