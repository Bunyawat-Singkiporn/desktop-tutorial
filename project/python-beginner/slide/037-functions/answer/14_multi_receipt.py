def bill():
    prices = [45, 60, 30]
    total = 0
    for price in prices:
        print(f"Item: {price}")
        total += price
    print(f"Total: {total}")

bill()
