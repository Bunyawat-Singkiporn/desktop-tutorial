height = int(input())
age = int(input())
is_vip = int(input())
day = input()

if height >= 120 and age >= 12:
    base_price = 900
else:
    base_price = 500

if is_vip == 1 or day == "weekend":
    fast_pass = 200
else:
    fast_pass = 0

total = base_price + fast_pass

print("==========================")
print("       THEME PARK")
print("==========================")
print(f"Base Price : {base_price}")
print(f"Fast Pass  : {fast_pass}")
print(f"Total      : {total}")
print("==========================")
