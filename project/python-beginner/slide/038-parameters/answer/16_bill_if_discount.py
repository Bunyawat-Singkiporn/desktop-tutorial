def pay(price):
    if price >= 300:
        print(f"Pay: {price - 50}")
    else:
        print(f"Pay: {price}")

pay(350)
pay(200)
