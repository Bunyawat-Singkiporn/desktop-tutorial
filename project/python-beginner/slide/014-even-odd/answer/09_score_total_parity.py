midterm = int(input())
final = int(input())

total = midterm + final

if total % 2 == 0:
    status = "Even Total"
else:
    status = "Odd Total"

print(f"Total  : {total}")
print(f"Status : {status}")
