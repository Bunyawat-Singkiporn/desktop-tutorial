TAX = 0.07

def with_tax(amount):
    return amount * (1 + TAX)

print(f"{with_tax(100):.2f}")
