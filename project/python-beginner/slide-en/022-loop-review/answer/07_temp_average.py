temps = [30, 32, 29, 31, 33]
total = 0
for t in temps:
    total += t
average = total / len(temps)
print(f"Total: {total}")
print(f"Average: {average:.1f}")
