all_scores = [85, 72, 91, 85, 60, 72, 95, 88]
class_info = ("Grade 9/1", "2025")
grades_given = set()

total = 0
top = all_scores[0]

for score in all_scores:
    total += score
    if score > top:
        top = score
    if score >= 80:
        grades_given.add("A")
    elif score >= 70:
        grades_given.add("B")
    elif score >= 60:
        grades_given.add("C")
    else:
        grades_given.add("F")

average = total / len(all_scores)

print(f"Class: {class_info[0]} ({class_info[1]})")
print("Scores:", all_scores)
print(f"Average: {average:.1f}")
print("Grades given:", grades_given)
print("Top score:", top)
