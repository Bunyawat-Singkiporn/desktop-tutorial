def calc_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def apply_discount(total):
    if total >= 300:
        return total - 50
    else:
        return total

n = int(input())
prices = []
for i in range(n):
    price = int(input())
    prices.append(price)

total = calc_total(prices)
print(total)
print(apply_discount(total))
