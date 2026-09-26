n = int(input())
if n == 0:
    print("No scores")
else:
    total = 0
    for i in range(n):
        total += int(input())
    print(f"{total / n:.1f}")
