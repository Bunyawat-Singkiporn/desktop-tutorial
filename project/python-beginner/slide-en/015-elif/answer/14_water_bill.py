units = int(input())

service = 30

if units >= 50:
    rate = 18
elif units >= 30:
    rate = 14
elif units >= 10:
    rate = 10
else:
    rate = 7

usage = rate * units
total = service + usage

print("==========================")
print("       WATER BILL")
print("==========================")
print(f"Service : {service}")
print(f"Usage   : {usage}")
print(f"Total   : {total}")
print("==========================")
