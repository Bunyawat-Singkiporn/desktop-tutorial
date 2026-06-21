# โจทย์: รับคะแนน 5 คน แสดงเกรด และนับ Pass/Fail

pass_count = 0
fail_count = 0

for i in range(5):
    score = int(input())
    if score >= 60:
        print(f"Score {score}: Pass")
        pass_count += 1
    else:
        print(f"Score {score}: Fail")
        fail_count += 1

print("---")
print(f"Pass: {pass_count}")
print(f"Fail: {fail_count}")
