def snack_bill():
    price = float(input())
    qty = float(input())
    op = input()
    print("Snack Shop")
    print(f"Price: {price}")
    print(f"Qty: {qty}")
    if op == "*":
        print(f"Total: {price * qty}")
    else:
        print("Please use *")

snack_bill()
