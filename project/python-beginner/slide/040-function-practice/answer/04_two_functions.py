def collect_scores(n):
    scores = []
    for i in range(n):
        score = int(input(f"Enter score {i + 1}: "))
        scores.append(score)
    return scores

def get_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

scores = collect_scores(3)
avg = get_average(scores)
print(f"Average: {avg:.1f}")
