scores = [55, 80, 40, 90, 70]
passed = 0
total = 0
for score in scores:
    if score < 50:
        continue
    print(f"Pass: {score}")
    passed = passed + 1
    total = total + score
print("==============")
print(f"Passed : {passed}")
print(f"SumPass: {total}")
print("==============")
