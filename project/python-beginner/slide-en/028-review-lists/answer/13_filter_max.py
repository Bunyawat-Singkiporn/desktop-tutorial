scores = [60, 85, 70, 40, 95, 75]
high = []
for score in scores:
    if score >= 70:
        high.append(score)
highest = high[0]
for score in high:
    if score > highest:
        highest = score
print(high)
print(f"Highest: {highest}")
