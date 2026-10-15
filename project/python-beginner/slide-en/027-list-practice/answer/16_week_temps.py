temps = [28, 33, 30, 35, 29, 34, 31]
hot = 0
highest = temps[0]
total = 0
for t in temps:
    total += t
    if t > 32:
        hot += 1
    if t > highest:
        highest = t
average = total / len(temps)
print(f"Hot   : {hot}")
print(f"Highest: {highest}")
print(f"Average: {average:.1f}")
