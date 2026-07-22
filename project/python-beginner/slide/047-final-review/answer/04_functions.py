def analyze(scores):
    total = 0
    passed = 0

    for score in scores:
        total += score
        if score >= 50:
            passed += 1

    average = total / len(scores)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    return {
        "total": total,
        "average": round(average, 1),
        "passed": passed,
        "grade": grade
    }

result = analyze([78, 85, 92, 70, 88])
for key, value in result.items():
    print(f"{key}: {value}")
