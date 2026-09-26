n = int(input())
hot = 0
for i in range(n):
    temp = int(input())
    if temp >= 30:
        hot = hot + 1
print(f"Hot Days: {hot}")
