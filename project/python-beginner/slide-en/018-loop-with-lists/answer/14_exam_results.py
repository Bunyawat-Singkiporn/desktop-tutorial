scores = [45, 70, 50, 39, 88]
passed = 0
failed = 0
print("========================")
print("       RESULTS")
print("========================")
for score in scores:
    if score >= 50:
        print(f"Score: {score} -> Pass")
        passed = passed + 1
    else:
        print(f"Score: {score} -> Fail")
        failed = failed + 1
print("------------------------")
print(f"Pass : {passed}")
print(f"Fail : {failed}")
print("========================")
