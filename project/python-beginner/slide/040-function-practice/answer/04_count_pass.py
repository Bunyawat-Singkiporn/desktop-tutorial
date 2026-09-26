def count_pass(scores):
    count = 0
    for s in scores:
        if s >= 50:
            count += 1
    return count

print(count_pass([40, 55, 70, 30, 90]))
