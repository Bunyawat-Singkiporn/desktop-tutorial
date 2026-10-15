answers = {"q1": "A", "q2": "C", "q3": "B"}
score = 0
for q in answers:
    user = input(f"{q}: ")
    if user == answers[q]:
        print("Correct")
        score += 1
    else:
        print("Wrong")
print(f"Score: {score}")
