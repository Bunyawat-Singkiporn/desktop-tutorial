contact = {
    "name": "Alice",
    "phone": "081-111-1111",
    "city": "Bangkok"
}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    elif command == "show":
        for key, value in contact.items():
            print(f"{key}: {value}")
    elif command == "update":
        key = input("Key: ")
        value = input("Value: ")
        contact[key] = value
    elif command == "delete":
        key = input("Key: ")
        if key in contact:
            del contact[key]
        else:
            print("Key not found:", key)
