distance = int(input())

if distance >= 300:
    price = 450
elif distance >= 150:
    price = 250
elif distance >= 50:
    price = 120
else:
    price = 60

print("========================")
print("       TRAIN")
print("========================")
print(f"Distance : {distance}")
print(f"Price    : {price}")
print("========================")
