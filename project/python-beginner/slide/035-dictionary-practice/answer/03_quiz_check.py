answers = {"q1": "A", "q2": "C", "q3": "B"}
score = 0

for question, correct in answers.items():
    user = input(f"{question}: ")
    if user == correct:
        score += 1

print(f"Score: {score}/3")
