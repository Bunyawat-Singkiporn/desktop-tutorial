def calc_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def add_vat(total):
    return total * 1.07

n = int(input("How many items? "))
prices = []
for i in range(n):
    price = float(input("Price: "))
    prices.append(price)

total = calc_total(prices)
print(f"Before VAT: {total}")
print(f"After VAT: {add_vat(total)}")
