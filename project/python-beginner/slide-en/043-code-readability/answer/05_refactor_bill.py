DISCOUNT = 20

def final_price(price):
    return price - DISCOUNT

def show(price):
    print(f"Pay: {final_price(price)}")

show(150)
