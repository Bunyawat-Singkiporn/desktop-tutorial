menu = {"rice": 40, "soup": 35, "salad": 45}
total = 0
for key, value in menu.items():
    print(f"{key}: {value}")
    total += value
print(f"Total: {total}")
