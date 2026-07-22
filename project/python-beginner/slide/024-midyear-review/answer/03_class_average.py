# โจทย์: รับคะแนน n คน แสดงผล Pass/Fail และสรุป

n = int(input())
scores = []
pass_count = 0
fail_count = 0

for i in range(n):
    score = int(input())
    scores.append(score)
    if score >= 60:
        print(f"Student {i+1}: {score} → Pass")
        pass_count += 1
    else:
        print(f"Student {i+1}: {score} → Fail")
        fail_count += 1

print("---")
print(f"Average: {sum(scores)/len(scores):.1f}")
print(f"Pass: {pass_count} | Fail: {fail_count}")
