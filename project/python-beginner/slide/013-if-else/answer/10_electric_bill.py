units = int(input())

if units <= 50:
    rate = 3
else:
    rate = 4

amount = units * rate

print("==========================")
print("      ELECTRIC BILL")
print("==========================")
print(f"Units      : {units}")
print(f"Rate       : {rate}")
print(f"Amount Due : {amount}")
print("==========================")
