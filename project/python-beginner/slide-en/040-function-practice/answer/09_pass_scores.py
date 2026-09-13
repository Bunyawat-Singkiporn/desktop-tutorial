def get_passed(scores):
    result = []
    for s in scores:
        if s >= 50:
            result.append(s)
    return result

n = int(input("How many scores? "))
scores = []
for i in range(n):
    scores.append(int(input("Score: ")))

print(f"Passed scores: {get_passed(scores)}")
