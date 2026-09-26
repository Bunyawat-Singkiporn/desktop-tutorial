prices = [80, 150, 120, 40, 200, 95]
picked = []
for price in prices:
    if price >= 100:
        picked.append(price)
picked.sort()
print(picked)
