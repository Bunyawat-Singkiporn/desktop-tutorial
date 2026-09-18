age = int(input())
day = input()

if age >= 60:
    base_price = 50
else:
    base_price = 100

if day == "weekend":
    weekend_fee = 20
else:
    weekend_fee = 0

total = base_price + weekend_fee

print("========================")
print("        TICKET")
print("========================")
print(f"Base Price : {base_price}")
print(f"Weekend Fee: {weekend_fee}")
print(f"Total      : {total}")
print("========================")
