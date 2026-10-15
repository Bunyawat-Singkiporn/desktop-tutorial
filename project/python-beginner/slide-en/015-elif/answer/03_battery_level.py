battery = int(input())

if battery >= 80:
    status = "Full"
elif battery >= 40:
    status = "Medium"
elif battery >= 15:
    status = "Low"
else:
    status = "Critical"

print(f"Battery : {battery}%")
print(f"Status  : {status}")
