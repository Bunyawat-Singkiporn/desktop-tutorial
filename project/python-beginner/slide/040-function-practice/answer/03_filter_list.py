def filter_above(numbers, minimum):
    result = []
    for n in numbers:
        if n >= minimum:
            result.append(n)
    return result

print(filter_above([3, 15, 7, 22, 8, 30, 5, 18], 10))
print(filter_above([85, 45, 92, 38, 88], 80))
