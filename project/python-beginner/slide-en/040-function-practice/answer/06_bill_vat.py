def calc_total(prices):
    total = 0
    for p in prices:
        total += p
    return total

def add_vat(total):
    return total * 1.07

print(f"{add_vat(calc_total([100, 50])):.2f}")
