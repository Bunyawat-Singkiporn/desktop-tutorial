prices = [200, 150, 50]
total = 0
for price in prices:
    with_vat = price * 1.07
    print(f"{with_vat:.2f}")
    total = total + with_vat
print(f"Grand Total: {total:.2f}")
