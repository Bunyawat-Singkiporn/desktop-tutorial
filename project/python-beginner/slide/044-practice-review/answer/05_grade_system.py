def add_student(db, name, score):
    db[name] = score

def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

def show_all(db):
    for name, score in db.items():
        print(f"{name}: {score} ({get_grade(score)})")

def get_average(db):
    total = 0
    for score in db.values():
        total += score
    return total / len(db)

def get_top(db):
    top_name = ""
    top_score = -1
    for name, score in db.items():
        if score > top_score:
            top_score = score
            top_name = name
    return top_name, top_score

db = {}
while True:
    command = input("Command: ")
    if command == "exit":
        break
    elif command == "add":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(db, name, score)
    elif command == "show":
        show_all(db)
    elif command == "average":
        print(f"Average: {get_average(db):.1f}")
    elif command == "top":
        top_name, top_score = get_top(db)
        print(f"Top: {top_name} ({top_score})")
