students = [("Alice", 85), ("Bob", 42), ("Charlie", 73)]

for student in students:
    name = student[0]
    score = student[1]
    if score >= 50:
        result = "Pass"
    else:
        result = "Fail"
    print(f"{name}: {score} → {result}")
