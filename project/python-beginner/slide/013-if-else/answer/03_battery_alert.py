battery = int(input())

if battery < 20:
    status = "Low Battery"
else:
    status = "Battery OK"

print(f"Battery : {battery}%")
print(f"Status  : {status}")
