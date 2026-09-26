spot = int(input())

if spot % 2 == 0:
    zone = "A"
    rate = 30
else:
    zone = "B"
    rate = 50

print("========================")
print("       PARKING")
print("========================")
print(f"Spot : {spot}")
print(f"Zone : {zone}")
print(f"Rate : {rate}")
print("========================")
