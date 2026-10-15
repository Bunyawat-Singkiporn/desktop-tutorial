def cart_total(prices):
    total = 0
    for p in prices:
        total += p
    return total

print(cart_total([12, 18, 20]))
