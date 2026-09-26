board = {"Nida": 70, "Ohm": 95, "Pim": 88}
top_name = ""
top_score = 0
for name, score in board.items():
    print(f"{name}: {score}")
    if score > top_score:
        top_score = score
        top_name = name
print(f"Top: {top_name} ({top_score})")
