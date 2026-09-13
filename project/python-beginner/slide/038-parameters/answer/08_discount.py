def sale_price(price, percent):
    pay = price * (100 - percent) / 100
    print(f"Original: {price}")
    print(f"Discount: {percent}%")
    print(f"Pay: {pay}")

price = float(input())
percent = float(input())
sale_price(price, percent)
