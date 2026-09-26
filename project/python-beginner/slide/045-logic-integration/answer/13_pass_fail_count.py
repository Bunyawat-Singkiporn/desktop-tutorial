scores = [40, 60, 55, 30, 80]
passed = 0
failed = 0
for s in scores:
    if s >= 50:
        passed += 1
    else:
        failed += 1
print(f"Pass: {passed}")
print(f"Fail: {failed}")
