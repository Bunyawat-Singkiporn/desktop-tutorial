temps = [30, 34, 29, 36, 31, 33]
hot = 0
for t in temps:
    if t > 32:
        hot += 1
print(f"Hot days: {hot}")
