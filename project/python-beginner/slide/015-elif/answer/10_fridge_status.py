temp = int(input())

if temp <= -10:
    status = "Deep Freeze"
elif temp <= 0:
    status = "Freezing"
elif temp <= 5:
    status = "Chilled"
else:
    status = "Too Warm"

print(f"Temp   : {temp}")
print(f"Status : {status}")
