prices = {"apple": 15, "banana": 8, "mango": 25, "kiwi": 35}
total = 0

for item, price in prices.items():
    print(f"{item}: {price} บาท")
    total += price

print(f"Total: {total} บาท")
