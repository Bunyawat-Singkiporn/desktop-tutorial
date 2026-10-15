student_scores = {"Alice": [85, 90, 80], "Bob": [70, 75, 65]}
for name, scores in student_scores.items():
    avg = sum(scores) / len(scores)
    print(f"{name}: {avg:.1f}")
