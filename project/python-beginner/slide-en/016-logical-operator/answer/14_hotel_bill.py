nights = int(input())
is_member = int(input())
day = input()
is_holiday = int(input())

stay = 1500 * nights

if nights >= 3 and is_member == 1:
    discount = 300
else:
    discount = 0

if day == "weekend" or is_holiday == 1:
    surcharge = 400
else:
    surcharge = 0

total = stay - discount + surcharge

print("============================")
print("         HOTEL")
print("============================")
print(f"Stay     : {stay}")
print(f"Discount : {discount}")
print(f"Surcharge: {surcharge}")
print(f"Total    : {total}")
print("============================")
