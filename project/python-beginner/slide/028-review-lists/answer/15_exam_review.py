names = ["Ann", "Ben", "Cara"]
scores = [45, 80, 70]
passed = 0
total = 0
for i in range(len(names)):
    total += scores[i]
    if scores[i] >= 50:
        print(f"{names[i]} Pass")
        passed += 1
    else:
        print(f"{names[i]} Fail")
average = total / len(scores)
print(f"Passed : {passed}")
print(f"Average: {average:.1f}")
