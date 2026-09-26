def safe_avg(scores):
    if len(scores) == 0:
        return 0
    else:
        return sum(scores) / len(scores)

print(safe_avg([]))
print(safe_avg([10, 20]))
