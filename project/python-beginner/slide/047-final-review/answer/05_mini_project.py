def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

def add_student(students, name, score):
    students[name] = score

def show_all(students):
    for name, score in students.items():
        print(f"{name}: {score} ({get_grade(score)})")

def get_stats(students):
    if not students:
        print("No students")
        return
    total = 0
    top_name, top_score = "", -1
    bot_name, bot_score = "", 999
    for name, score in students.items():
        total += score
        if score > top_score:
            top_score, top_name = score, name
        if score < bot_score:
            bot_score, bot_name = score, name
    avg = total / len(students)
    print(f"Average: {avg:.1f}")
    print(f"Top: {top_name} ({top_score})")
    print(f"Bottom: {bot_name} ({bot_score})")

def search_student(students, name):
    if name in students:
        score = students[name]
        print(f"Found: {name} - {score} ({get_grade(score)})")
    else:
        print(f"Not found: {name}")

students = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    elif command == "add":
        name = input("Name: ")
        score = int(input("Score: "))
        add_student(students, name, score)
    elif command == "show":
        show_all(students)
    elif command == "stats":
        get_stats(students)
    elif command == "search":
        name = input("Name: ")
        search_student(students, name)
