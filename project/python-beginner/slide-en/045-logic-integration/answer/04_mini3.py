prices = {"apple": 15, "banana": 8, "mango": 35, "kiwi": 10, "orange": 22}

for item, price in prices.items():
    if price <= 10:
        print(f"{item}: {price} → Cheap")
    elif price <= 20:
        print(f"{item}: {price} → Fair")
