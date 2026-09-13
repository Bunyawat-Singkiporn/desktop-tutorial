def show_total(price, qty):
    total = price * qty
    print(f"Total: {total}")

price = float(input())
qty = int(input())
show_total(price, qty)
