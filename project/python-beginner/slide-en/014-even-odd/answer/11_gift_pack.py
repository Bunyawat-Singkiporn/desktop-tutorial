items = int(input())

if items % 5 == 0:
    status = "Perfect Pack"
else:
    status = "Need More"

print(f"Items  : {items}")
print(f"Status : {status}")
