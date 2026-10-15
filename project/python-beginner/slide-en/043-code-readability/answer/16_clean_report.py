PASS_SCORE = 50

def is_pass(score):
    return score >= PASS_SCORE

def report(name, score):
    if is_pass(score):
        print(f"{name}: Pass")
    else:
        print(f"{name}: Fail")

report("Yam", 66)
report("Bee", 40)
