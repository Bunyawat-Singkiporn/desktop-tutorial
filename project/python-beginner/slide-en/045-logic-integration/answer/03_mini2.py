def summarize(scores):
    minimum = scores[0]
    maximum = scores[0]
    total = 0

    for score in scores:
        if score < minimum:
            minimum = score
        if score > maximum:
            maximum = score
        total += score

    average = total / len(scores)
    print("Min:", minimum)
    print("Max:", maximum)
    print(f"Average: {average:.1f}")

summarize([85, 45, 92, 68, 95])
