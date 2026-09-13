def get_price(menu):
    if menu == "pizza":
        return 120
    elif menu == "noodles":
        return 50
    else:
        return 0

def calc_total(price, qty):
    return price * qty

def print_order(menu, qty, total):
    print("=== Food Order ===")
    print(f"Menu: {menu}")
    print(f"Qty: {qty}")
    print(f"Total: {total} baht")

menu = input()
qty = int(input())
price = get_price(menu)
total = calc_total(price, qty)
print_order(menu, qty, total)
