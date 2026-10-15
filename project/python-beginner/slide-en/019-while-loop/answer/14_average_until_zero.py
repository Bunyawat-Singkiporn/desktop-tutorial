total = 0
count = 0
number = int(input())
while number != 0:
    total = total + number
    count = count + 1
    number = int(input())
average = total / count
print("========================")
print("      AVERAGE")
print("========================")
print(f"Count   : {count}")
print(f"Total   : {total}")
print(f"Average : {average:.1f}")
print("========================")
