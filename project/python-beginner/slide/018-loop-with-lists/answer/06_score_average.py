scores = [72, 88, 95, 60, 81]
total = 0
for score in scores:
    total = total + score
average = total / len(scores)
print(f"Total  : {total}")
print(f"Average: {average:.1f}")
