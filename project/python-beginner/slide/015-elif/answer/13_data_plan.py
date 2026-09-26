data_gb = int(input())

if data_gb >= 100:
    plan = "Ultra"
    price = 899
elif data_gb >= 50:
    plan = "Plus"
    price = 599
elif data_gb >= 20:
    plan = "Basic"
    price = 299
else:
    plan = "Lite"
    price = 149

print("========================")
print("      DATA PLAN")
print("========================")
print(f"Need  : {data_gb}")
print(f"Plan  : {plan}")
print(f"Price : {price}")
print("========================")
