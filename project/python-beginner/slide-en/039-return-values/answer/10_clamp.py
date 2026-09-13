def fix_score(score):
    if score < 0:
        return 0
    elif score > 100:
        return 100
    else:
        return score

for i in range(3):
    score = int(input("Raw score: "))
    print(f"Fixed: {fix_score(score)}")
