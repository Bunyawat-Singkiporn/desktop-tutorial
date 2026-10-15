prices = [100, 250, 80]
total = 0
for price in prices:
    new_price = price + 10
    print(new_price)
    total = total + new_price
print(f"New Total: {total}")
