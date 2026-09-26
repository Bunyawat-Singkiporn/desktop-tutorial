cart = {"milk": 20, "bread": 25, "egg": 40}
cart["egg"] = 35
total = 0
for key, value in cart.items():
    print(f"{key}: {value}")
    total += value
print(f"Total: {total}")
