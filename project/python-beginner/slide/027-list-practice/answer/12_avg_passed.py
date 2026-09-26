scores = [40, 80, 60, 30, 90]
passed = []
for score in scores:
    if score >= 50:
        passed.append(score)
total = 0
for score in passed:
    total += score
average = total / len(passed)
print(f"Average: {average:.1f}")
