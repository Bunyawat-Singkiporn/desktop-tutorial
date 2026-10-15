size = input()
whip = input()

base = 45

if size == "L":
    size_fee = 15
else:
    size_fee = 0

if whip == "yes":
    whip_fee = 10
else:
    whip_fee = 0

total = base + size_fee + whip_fee

print("========================")
print("        COFFEE")
print("========================")
print(f"Base   : {base}")
print(f"Size   : {size_fee}")
print(f"Whip   : {whip_fee}")
print(f"Total  : {total}")
print("========================")
