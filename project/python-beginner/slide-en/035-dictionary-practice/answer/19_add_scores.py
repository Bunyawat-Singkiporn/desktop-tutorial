scores = {"Alice": 80, "Bob": 70}

scores["Cara"] = 90
scores["Bob"] = scores["Bob"] + 10

for name, score in scores.items():
    print(f"{name}: {score}")
