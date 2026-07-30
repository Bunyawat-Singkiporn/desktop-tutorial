def get_average(scores):
    total = 0
    for score in scores.values():
        total += score
    return total / len(scores)

def get_top_student(scores):
    top_name = ""
    top_score = -1
    for name, score in scores.items():
        if score > top_score:
            top_score = score
            top_name = name
    return top_name, top_score

student_scores = {"a": 85, "b": 72, "c": 90, "d": 68}

average = get_average(student_scores)
top_name, top_score = get_top_student(student_scores)

print(f"Average: {average}")
print(f"Top student: {top_name} ({top_score})")
