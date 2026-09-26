def get_total(prices):
    total = 0
    for p in prices:
        total += p
    return total

print(get_total([15, 25, 10]))
