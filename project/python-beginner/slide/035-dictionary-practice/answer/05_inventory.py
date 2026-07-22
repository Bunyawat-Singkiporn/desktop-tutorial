inventory = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    elif command == "add":
        name = input("Name: ")
        price = int(input("Price: "))
        inventory[name] = price
    elif command == "update":
        name = input("Name: ")
        if name in inventory:
            price = int(input("New price: "))
            inventory[name] = price
        else:
            print("Not found:", name)
    elif command == "remove":
        name = input("Name: ")
        if name in inventory:
            del inventory[name]
        else:
            print("Not found:", name)
    elif command == "show":
        for name, price in inventory.items():
            print(f"{name}: {price} บาท")
