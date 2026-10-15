weight = int(input())
destination = input()

base_fee = 30

if weight > 1000:
    weight_fee = 40
else:
    weight_fee = 0

if destination == "upcountry":
    distance_fee = 50
else:
    distance_fee = 0

total = base_fee + weight_fee + distance_fee

print("==========================")
print("        SHIPPING")
print("==========================")
print(f"Base Fee     : {base_fee}")
print(f"Weight Fee   : {weight_fee}")
print(f"Distance Fee : {distance_fee}")
print(f"Total        : {total}")
print("==========================")
