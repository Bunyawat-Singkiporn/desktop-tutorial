def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

def print_report(students):
    print("=== Report ===")
    for name, score in students.items():
        grade = get_grade(score)
        print(f"{name}: {score} → {grade}")

print_report({"Alice": 88, "Bob": 72, "Charlie": 55})
