menu = {"mango": 40, "strawberry": 45, "orange": 35}

drink = input()
if drink in menu:
    print("=== Order ===")
    print(f"Drink: {drink}")
    print(f"Price: {menu[drink]} baht")
else:
    print("Sorry, not on the menu")
