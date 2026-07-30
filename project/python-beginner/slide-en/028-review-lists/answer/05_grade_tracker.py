scores = [78, 85, 92, 70, 88]
total = 0

for i in range(len(scores)):
    print(f"{i + 1}. {scores[i]}")
    total += scores[i]

average = total / len(scores)
print("Total:", total)
print(f"Average: {average:.1f}")

if average >= 70:
    print("Result: Pass")
else:
    print("Result: Fail")
