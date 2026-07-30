gradebook = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    elif command == "add":
        name = input("Name: ")
        score = int(input("Score: "))
        gradebook[name] = score
    elif command == "update":
        name = input("Name: ")
        score = int(input("Score: "))
        gradebook[name] = score
    elif command == "show":
        for name, score in gradebook.items():
            print(f"{name}: {score}")
    elif command == "top":
        if len(gradebook) == 0:
            print("No students yet")
        else:
            top_name = ""
            top_score = -1
            for name, score in gradebook.items():
                if score > top_score:
                    top_score = score
                    top_name = name
            print(f"Top: {top_name} ({top_score})")
