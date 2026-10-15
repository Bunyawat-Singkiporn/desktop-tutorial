points = int(input())

if points % 2 == 0:
    action = "Doubled"
    after = points * 2
else:
    action = "Tripled"
    after = points * 3

print("========================")
print("         SCORE")
print("========================")
print(f"Before : {points}")
print(f"Action : {action}")
print(f"After  : {after}")
print("========================")
