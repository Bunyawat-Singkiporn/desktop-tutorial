prices = [120, 80, 200, 50]
total = 0
print("========================")
print("        CART")
print("========================")
for price in prices:
    print(price)
    total = total + price
print("------------------------")
print(f"Items   : {len(prices)}")
print(f"Total   : {total}")
print(f"Average : {total / len(prices):.1f}")
print("========================")
