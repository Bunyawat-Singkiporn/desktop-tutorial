def parity(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(3):
    n = int(input("Enter number: "))
    print(f"{n} → {parity(n)}")
