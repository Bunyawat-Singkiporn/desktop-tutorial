def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

scores = [85, 72, 55]
for s in scores:
    grade = get_grade(s)
    print(f"Score {s} → Grade {grade}")
