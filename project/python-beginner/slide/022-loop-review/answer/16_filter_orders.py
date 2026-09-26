orders = [50, -10, 30, 0, 20]
count = 0
total = 0
for order in orders:
    if order <= 0:
        continue
    count += 1
    total += order
print(f"Count: {count}")
print(f"Total: {total}")
