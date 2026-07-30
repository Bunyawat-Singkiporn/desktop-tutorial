checkins = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

total = len(checkins)
unique = set(checkins)

most_name = ""
most_count = 0
for name in unique:
    count = checkins.count(name)
    if count > most_count:
        most_count = count
        most_name = name

print("Total check-ins:", total)
print("Unique students:", len(unique))
print(f"Most check-ins: {most_name} ({most_count} times)")
