scores = [55, 80, 42, 70, 90, 58]
passed = 0
for score in scores:
    if score >= 60:
        passed += 1
print(f"Passed: {passed}")
