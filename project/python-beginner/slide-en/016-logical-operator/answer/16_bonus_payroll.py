sales = int(input())
rating = int(input())
late_flag = int(input())

salary = 15000

if sales >= 50000 and rating >= 4:
    bonus = 4000
elif sales >= 30000 or rating >= 5:
    bonus = 2000
else:
    bonus = 500

is_late = late_flag == 1

if not is_late:
    on_time = 300
else:
    on_time = 0

net_pay = salary + bonus + on_time

print("============================")
print("          PAYROLL")
print("============================")
print(f"Salary    : {salary}")
print(f"Bonus     : {bonus}")
print(f"On Time   : {on_time}")
print(f"Net Pay   : {net_pay}")
print("============================")
