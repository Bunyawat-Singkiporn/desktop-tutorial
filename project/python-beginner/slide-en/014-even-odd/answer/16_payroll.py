employee_id = int(input())
overtime_hours = int(input())

salary = 12000

if employee_id % 2 == 0:
    bonus = 500
else:
    bonus = 200

if overtime_hours > 5:
    overtime = 1000
else:
    overtime = 0

net_pay = salary + bonus + overtime

print("============================")
print("          PAYROLL")
print("============================")
print(f"Salary   : {salary}")
print(f"Bonus    : {bonus}")
print(f"Overtime : {overtime}")
print(f"Net Pay  : {net_pay}")
print("============================")
