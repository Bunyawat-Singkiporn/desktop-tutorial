prices = [45, 120, 80, 200, 99, 150]
count = 0
for price in prices:
    if price >= 100:
        count += 1
print(f"Expensive: {count}")
