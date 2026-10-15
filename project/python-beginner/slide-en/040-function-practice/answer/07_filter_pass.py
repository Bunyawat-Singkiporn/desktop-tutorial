def get_passed(scores):
    result = []
    for s in scores:
        if s >= 60:
            result.append(s)
    return result

print(get_passed([50, 60, 75, 40, 90]))
