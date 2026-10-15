scores = [42, 55, 60, 38, 71, 49]
passed = 0
for score in scores:
    if score >= 50:
        passed = passed + 1
print(f"Passed: {passed}")
