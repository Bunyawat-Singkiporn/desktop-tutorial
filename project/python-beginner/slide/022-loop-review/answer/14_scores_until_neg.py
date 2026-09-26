count = 0
total = 0
while True:
    score = int(input())
    if score == -1:
        break
    count += 1
    total += score
print(f"Count: {count}")
print(f"Total: {total}")
