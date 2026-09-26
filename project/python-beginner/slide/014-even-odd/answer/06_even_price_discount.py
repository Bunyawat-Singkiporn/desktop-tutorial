price = int(input())

if price % 2 == 0:
    discount = 20
else:
    discount = 0

final_price = price - discount

print("========================")
print("       TOY SHOP")
print("========================")
print(f"Price       : {price}")
print(f"Discount    : {discount}")
print(f"Final Price : {final_price}")
print("========================")
