def lucky(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(3):
    n = int(input("Your number: "))
    print(f"{n} is {lucky(n)}")
