scores = [45, 80, 60, 30]
passed = 0
for score in scores:
    if score >= 50:
        print("Pass")
        passed += 1
    else:
        print("Fail")
print(f"Passed: {passed}")
