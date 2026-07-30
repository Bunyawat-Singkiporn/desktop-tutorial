def add_score(scores, name, score):
    scores[name] = score

def get_average(scores):
    total = 0
    for score in scores.values():
        total += score
    return total / len(scores)

def get_top(scores):
    top_name = ""
    top_score = -1
    for name, score in scores.items():
        if score > top_score:
            top_score = score
            top_name = name
    return top_name, top_score

def show_all(scores):
    for name, score in scores.items():
        print(f"{name}: {score}")

scores = {}
add_score(scores, "Alice", 85)
add_score(scores, "Bob", 92)
add_score(scores, "Charlie", 78)

show_all(scores)
print(f"Average: {get_average(scores):.1f}")
top_name, top_score = get_top(scores)
print(f"Top: {top_name} ({top_score})")
