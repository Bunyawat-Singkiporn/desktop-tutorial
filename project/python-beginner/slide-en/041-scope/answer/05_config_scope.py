TAX_RATE = 0.07

def calculate_price(base_price):
    tax_amount = base_price * TAX_RATE   # local variable
    final_price = base_price + tax_amount
    return final_price

def show_receipt(item, price):
    print(f"{item}: {price:.1f} บาท")

print("=== Receipt ===")
coffee_price = calculate_price(30)
cake_price = calculate_price(80)
show_receipt("Coffee", coffee_price)
show_receipt("Cake", cake_price)
print(f"Total: {coffee_price + cake_price:.1f} บาท")
