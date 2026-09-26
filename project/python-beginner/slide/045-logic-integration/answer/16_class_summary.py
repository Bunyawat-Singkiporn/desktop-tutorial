def status(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

scores = [45, 70, 88]
for s in scores:
    print(status(s))
