cabin = input()
baggage = int(input())

if cabin == "first":
    base_price = 12000
elif cabin == "business":
    base_price = 7000
else:
    base_price = 2500

if baggage >= 30:
    bag_fee = 800
elif baggage >= 20:
    bag_fee = 400
else:
    bag_fee = 0

total = base_price + bag_fee

print("==========================")
print("         FLIGHT")
print("==========================")
print(f"Base Price : {base_price}")
print(f"Bag Fee  : {bag_fee}")
print(f"Total      : {total}")
print("==========================")
