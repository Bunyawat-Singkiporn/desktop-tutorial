prices = [45, 90, 30, 120, 60, 75]
cart = []
for price in prices:
    if price < 80:
        cart.append(price)
cart.sort()
total = 0
for price in cart:
    total += price
print(cart)
print(f"Items: {len(cart)}")
print(f"Total: {total}")
