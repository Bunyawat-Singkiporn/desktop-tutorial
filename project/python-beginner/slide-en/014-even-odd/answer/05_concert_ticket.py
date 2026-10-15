seat = int(input())
day = input()

if seat % 2 == 0:
    base_price = 800
else:
    base_price = 600

if day == "weekend":
    day_fee = 100
else:
    day_fee = 0

total = base_price + day_fee

print("========================")
print("      CONCERT")
print("========================")
print(f"Base Price : {base_price}")
print(f"Day Fee    : {day_fee}")
print(f"Total      : {total}")
print("========================")
