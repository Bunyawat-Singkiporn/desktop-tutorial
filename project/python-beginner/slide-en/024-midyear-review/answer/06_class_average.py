scores = [80, 70, 90, 60]
total = 0
for score in scores:
    total = total + score
average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.1f}")
