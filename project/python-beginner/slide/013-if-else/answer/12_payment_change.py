price = int(input())
paid = int(input())

print("========================")
print("       PAYMENT")
print("========================")
print(f"Price    : {price}")
print(f"Paid     : {paid}")

if paid >= price:
    print(f"Change   : {paid - price}")
else:
    print(f"Shortage : {price - paid}")

print("========================")
