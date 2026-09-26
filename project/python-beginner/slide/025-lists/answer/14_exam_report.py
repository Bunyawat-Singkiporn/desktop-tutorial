names = ["Ann", "Ben", "Cara"]
scores = [72, 48, 91]
passed = 0
i = 0
for name in names:
    score = scores[i]
    if score >= 50:
        status = "Pass"
        passed += 1
    else:
        status = "Fail"
    print(f"{name} {score} {status}")
    i += 1
print(f"Passed: {passed}")
