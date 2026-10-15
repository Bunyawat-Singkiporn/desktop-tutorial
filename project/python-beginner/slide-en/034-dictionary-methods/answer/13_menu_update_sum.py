menu = {"soup": 40, "salad": 50, "steak": 120}
menu.update({"soup": 45, "salad": 55})
total = 0
for value in menu.values():
    total += value
print(f"Total: {total}")
