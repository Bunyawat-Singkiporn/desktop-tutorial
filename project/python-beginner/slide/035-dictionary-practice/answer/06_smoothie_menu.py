menu = {"mango": 45, "berry": 50, "banana": 40}
total = 0
for item, price in menu.items():
    print(f"{item}: {price}")
    total += price
print(f"Total: {total}")
