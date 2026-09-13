def pass_scores(scores):
    result = []
    for s in scores:
        if s >= 50:
            result.append(s)
    return result

n = int(input("How many? "))
scores = []
for i in range(n):
    scores.append(int(input("Score: ")))

print(f"Passed: {pass_scores(scores)}")
