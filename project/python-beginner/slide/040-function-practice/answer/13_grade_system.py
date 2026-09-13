def read_scores(n):
    scores = []
    for i in range(n):
        scores.append(int(input("Score: ")))
    return scores

def average(scores):
    total = 0
    for s in scores:
        total += s
    return total / len(scores)

def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

def report(name, avg, g):
    print(f"{name} | avg={avg:.1f} | grade={g}")

name = input("Name: ")
n = int(input("Subjects: "))
scores = read_scores(n)
avg = average(scores)
g = grade(avg)
report(name, avg, g)
