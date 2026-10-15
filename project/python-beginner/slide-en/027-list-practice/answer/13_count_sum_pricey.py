prices = [50, 120, 80, 200, 150]
count = 0
total = 0
for price in prices:
    if price >= 100:
        count += 1
        total += price
print(f"Count: {count}")
print(f"Total: {total}")
