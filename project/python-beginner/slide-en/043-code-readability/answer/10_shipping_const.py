SHIPPING_FEE = 40
FREE_MIN = 300
total = int(input())
if total >= FREE_MIN:
    print("Shipping: 0")
else:
    print(f"Shipping: {SHIPPING_FEE}")
