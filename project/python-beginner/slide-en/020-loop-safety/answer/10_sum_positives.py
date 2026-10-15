total = 0
while True:
    number = int(input())
    if number == 0:
        break
    if number < 0:
        continue
    total = total + number
print(f"Total: {total}")
