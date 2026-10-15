prices = {"pen": 10, "book": 45, "glue": 20}
total = 0
for key in prices:
    print(f"{key}: {prices[key]}")
    total += prices[key]
print(f"Total: {total}")
