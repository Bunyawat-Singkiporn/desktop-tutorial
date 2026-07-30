n = int(input())

for i in range(1, n + 1):
    if i == 10:
        print("10 → Stop")
        break
    if i == 5:
        continue
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")
