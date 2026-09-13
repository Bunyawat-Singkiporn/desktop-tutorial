def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

score = int(input())
grade = get_grade(score)
print(f"Grade: {grade}")
