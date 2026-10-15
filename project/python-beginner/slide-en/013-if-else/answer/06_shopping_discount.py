total = int(input())

if total >= 500:
    discount = 50
else:
    discount = 0

final_price = total - discount

print("========================")
print("       SHOPPING")
print("========================")
print(f"Total       : {total}")
print(f"Discount    : {discount}")
print(f"Final Price : {final_price}")
print("========================")
