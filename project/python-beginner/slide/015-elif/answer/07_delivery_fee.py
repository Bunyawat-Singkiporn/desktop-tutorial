weight = int(input())

if weight >= 5000:
    fee = 120
elif weight >= 2000:
    fee = 70
elif weight >= 500:
    fee = 40
else:
    fee = 25

print("========================")
print("      DELIVERY")
print("========================")
print(f"Weight : {weight}")
print(f"Fee    : {fee}")
print("========================")
