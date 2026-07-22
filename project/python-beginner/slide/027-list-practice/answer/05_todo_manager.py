todos = []

while True:
    command = input("Command: ")

    if command == "exit":
        print("Done!")
        break
    elif command == "add":
        item = input("Item: ")
        todos.append(item)
    elif command == "remove":
        item = input("Item: ")
        if item in todos:
            todos.remove(item)
        else:
            print("Not found:", item)
    elif command == "show":
        for i in range(len(todos)):
            print(f"{i + 1}. {todos[i]}")
