def clamp(score):
    if score < 0:
        return 0
    elif score > 100:
        return 100
    else:
        return score

for i in range(3):
    score = int(input("Enter score: "))
    print(clamp(score))
