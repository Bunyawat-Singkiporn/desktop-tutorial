points = {"Ann": 9, "Ben": 4, "Cara": 7}
low_name = ""
low_score = 999
for name, score in points.items():
    if score < low_score:
        low_score = score
        low_name = name
print(f"Low: {low_name} ({low_score})")
