prices = [20, 75, 40, 90, 15, 60]
cheap = []
for price in prices:
    if price < 50:
        cheap.append(price)
print(cheap)
