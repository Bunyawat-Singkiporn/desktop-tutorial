stock = {"rice": 10, "oil": 3, "temp": 0, "salt": 8}
stock["oil"] = 5
del stock["temp"]
for key, value in stock.items():
    print(f"{key}: {value}")
print(f"Kinds: {len(stock)}")
