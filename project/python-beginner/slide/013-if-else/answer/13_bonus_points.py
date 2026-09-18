amount = int(input())

base = amount // 100

if base >= 5:
    bonus = 10
else:
    bonus = 0

total = base + bonus

print("========================")
print("        POINTS")
print("========================")
print(f"Base Points  : {base}")
print(f"Bonus Points : {bonus}")
print(f"Total Points : {total}")
print("========================")
