def ask(question, answer):
    user = input(question)
    return user == answer

def show_result(score, total):
    print(f"Score: {score}/{total}")
    if score == total:
        print("Perfect!")
    elif score >= total / 2:
        print("Good job!")
    else:
        print("Keep practicing!")

score = 0
total = 3

if ask("What is 2 + 2? ", "4"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

if ask("Capital of Thailand? ", "Bangkok"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

if ask("Color of the sky? ", "blue"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("=== Result ===")
show_result(score, total)
