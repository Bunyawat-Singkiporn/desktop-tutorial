scores = [70, 85, 60, 90]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.1f}")
if average >= 70:
    print("Status: Good")
else:
    print("Status: Needs Work")
