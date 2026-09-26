def add_score(scores, name, score):
    scores[name] = score
    return scores

def get_average(scores):
    total = 0
    for v in scores.values():
        total += v
    return total / len(scores)

scores = {}
scores = add_score(scores, "Alice", 80)
scores = add_score(scores, "Bob", 100)
print(get_average(scores))
