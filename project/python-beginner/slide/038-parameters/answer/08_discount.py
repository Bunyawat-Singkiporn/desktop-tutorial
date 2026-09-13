def apply_discount(price, percent):
    pay = price * (100 - percent) / 100
    print(f"Pay: {pay}")

price = float(input())
percent = float(input())
apply_discount(price, percent)
