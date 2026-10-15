scores = {"Ann": 80, "Ben": 40, "Cara": 65}
for name, score in scores.items():
    if score >= 50:
        status = "Pass"
    else:
        status = "Fail"
    print(f"{name} {score} {status}")
