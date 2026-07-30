def get_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def classify(average):
    if average >= 80:
        return "Excellent"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

students = {
    "Alice": [90, 85, 80],
    "Bob": [70, 55, 61],
    "Charlie": [45, 55, 50]
}

for name, scores in students.items():
    avg = get_average(scores)
    level = classify(avg)
    print(f"{name}: {avg:.1f} → {level}")
