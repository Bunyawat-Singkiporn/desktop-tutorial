items = int(input())

if items >= 300:
    shipping = 0
else:
    shipping = 40

payable = items + shipping

print("========================")
print("        ORDER")
print("========================")
print(f"Items    : {items}")
print(f"Shipping : {shipping}")
print(f"Payable  : {payable}")
print("========================")
