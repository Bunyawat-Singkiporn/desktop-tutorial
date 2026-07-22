def is_even(n):
    return n % 2 == 0

for num in [4, 7, 10]:
    if is_even(num):
        print(f"{num} → Even")
    else:
        print(f"{num} → Odd")
