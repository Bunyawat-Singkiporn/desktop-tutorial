def print_bill(price, qty):
    print("Food Bill")
    print(f"Price: {price}")
    print(f"Qty: {qty}")
    print(f"Total: {price * qty}")

price = float(input())
qty = int(input())
print_bill(price, qty)
