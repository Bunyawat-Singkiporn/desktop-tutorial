# Trace Table:
# รอบ | item | item>5? | count | total
#  1  |  3   | False   |   0   |   0
#  2  |  8   | True    |   1   |   8
#  3  |  2   | False   |   1   |   8
#  4  |  9   | True    |   2   |  17
#  5  |  5   | False   |   2   |  17
#  6  |  7   | True    |   3   |  24
# Output: (24, 3)

def mystery(items):
    count = 0
    total = 0
    for item in items:
        if item > 5:
            count += 1
            total += item
    return total, count

result = mystery([3, 8, 2, 9, 5, 7])
print(result)
