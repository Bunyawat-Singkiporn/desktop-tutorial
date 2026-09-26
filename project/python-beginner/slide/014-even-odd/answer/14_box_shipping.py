weight = int(input())
box_number = int(input())

base_fee = 25

if weight > 2000:
    weight_fee = 40
else:
    weight_fee = 0

if box_number % 2 == 0:
    box_fee = 15
else:
    box_fee = 0

total = base_fee + weight_fee + box_fee

print("==========================")
print("        SHIPPING")
print("==========================")
print(f"Base Fee  : {base_fee}")
print(f"Weight Fee: {weight_fee}")
print(f"Box Fee   : {box_fee}")
print(f"Total     : {total}")
print("==========================")
