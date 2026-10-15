def average(scores):
    if len(scores) == 0:
        return 0
    else:
        return sum(scores) / len(scores)

print(average([]))
print(average([8, 10]))
