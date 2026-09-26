def passed(scores):
    result = []
    for s in scores:
        if s >= 60:
            result.append(s)
    return result

print(passed([55, 60, 88, 40]))
