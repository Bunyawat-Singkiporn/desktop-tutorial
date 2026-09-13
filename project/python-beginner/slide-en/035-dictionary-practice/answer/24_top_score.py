scores = {"Alice": 85, "Bob": 92, "Cara": 78}

top_name = ""
top_score = -1

for name, score in scores.items():
    if score > top_score:
        top_score = score
        top_name = name

print(f"Top: {top_name} ({top_score})")
