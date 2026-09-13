bag = {"potion": 2, "sword": 1, "coin": 50}

bag["potion"] = bag["potion"] + 1
bag["shield"] = 1

for item, qty in bag.items():
    print(f"{item} x{qty}")
