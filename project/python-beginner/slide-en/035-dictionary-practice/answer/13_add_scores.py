scores = {"Ann": 10, "Ben": 8}
bonus = {"Ann": 5, "Ben": 2}
for name in bonus:
    scores[name] += bonus[name]
for name, score in scores.items():
    print(f"{name}: {score}")
