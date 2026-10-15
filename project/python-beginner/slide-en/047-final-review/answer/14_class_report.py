room = {"A": [10, 20], "B": [30, 5]}
for name, scores in room.items():
    print(f"{name}: {sum(scores)}")
