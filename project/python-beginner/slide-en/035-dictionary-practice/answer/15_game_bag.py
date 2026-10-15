bag = {"potion": 2, "coin": 5}
bag["potion"] += 1
bag["gem"] = 3
for key, value in bag.items():
    print(f"{key}: {value}")
