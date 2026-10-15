drinks = ["Latte", "Mocha", "Tea"]
prices = [55, 60, 40]
for drink in drinks:
    print(drink)
total = 0
for price in prices:
    total += price
print(f"Menus: {len(drinks)}")
print(f"Total: {total}")
