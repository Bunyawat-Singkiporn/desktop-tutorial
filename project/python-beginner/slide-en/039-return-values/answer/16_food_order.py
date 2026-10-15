def subtotal(a, b):
    return a + b

def with_vat(amount):
    return amount * 1.07

print(f"{with_vat(subtotal(100, 50)):.2f}")
