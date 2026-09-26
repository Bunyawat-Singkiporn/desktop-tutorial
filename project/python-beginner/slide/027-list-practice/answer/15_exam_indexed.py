scores = [72, 40, 88, 55]
passed = 0
for i in range(len(scores)):
    score = scores[i]
    if score >= 50:
        status = "Pass"
        passed += 1
    else:
        status = "Fail"
    print(f"{i + 1}) {score} {status}")
print(f"Passed: {passed}")
