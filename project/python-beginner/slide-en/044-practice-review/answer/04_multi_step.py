records = []

for i in range(3):
    name = input("Name: ")
    score = int(input("Score: "))
    records.append((name, score))

print("=== Results ===")
total = 0
for name, score in records:
    print(f"{name}: {score}")
    total += score

average = total / len(records)
print(f"Average: {average:.1f}")
