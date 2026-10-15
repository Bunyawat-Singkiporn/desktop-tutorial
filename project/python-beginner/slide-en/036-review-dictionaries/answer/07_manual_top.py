scores = {"Red": 12, "Blue": 18, "Green": 15}
top_name = ""
top_score = 0
for name, score in scores.items():
    if score > top_score:
        top_score = score
        top_name = name
print(f"Top: {top_name} ({top_score})")
