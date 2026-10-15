budget = 500
prices = [120, 80, 150, 90]
need = 0
for price in prices:
    need = need + price
print("========================")
print("       BUDGET")
print("========================")
print(f"Budget : {budget}")
print(f"Need   : {need}")
if need <= budget:
    print("Status : OK")
else:
    print("Status : Over Budget")
print("========================")
