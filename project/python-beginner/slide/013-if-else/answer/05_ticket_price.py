age = int(input())
day = input()

if age >= 60:
    price = 50
else:
    price = 100

if day == "weekend":
    price = price + 20

print(price)
