total = 0

def sell(price):
    global total
    total += price

def show_total():
    print(f"Total: {total}")

sell(30)
sell(45)
show_total()
