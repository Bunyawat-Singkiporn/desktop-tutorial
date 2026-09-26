scores = [40, 70, 70, 90, 40, 55]
passed = []
for score in scores:
    if score >= 50:
        passed.append(score)
unique = list(set(passed))
unique.sort()
print(unique)
