scores = [120, 80, 95]
scores.append(150)
scores.remove(80)
scores[0] = 130
scores.sort(reverse=True)
print(scores)
print(f"Top: {scores[0]}")
