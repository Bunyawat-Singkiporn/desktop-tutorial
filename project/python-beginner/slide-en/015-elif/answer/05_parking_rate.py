hours = int(input())

if hours >= 8:
    rate = 25
elif hours >= 4:
    rate = 30
elif hours >= 2:
    rate = 40
else:
    rate = 50

total = rate * hours

print("========================")
print("       PARKING")
print("========================")
print(f"Hours : {hours}")
print(f"Rate  : {rate}")
print(f"Total : {total}")
print("========================")
