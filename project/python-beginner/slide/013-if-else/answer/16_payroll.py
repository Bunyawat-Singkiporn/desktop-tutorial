sales = int(input())
absent_days = int(input())

salary = 15000

if sales >= 50000:
    bonus = 2000
else:
    bonus = 500

if absent_days > 2:
    deduction = 300
else:
    deduction = 0

net_pay = salary + bonus - deduction

print("============================")
print("          PAYROLL")
print("============================")
print(f"Salary    : {salary}")
print(f"Bonus     : {bonus}")
print(f"Deduction : {deduction}")
print(f"Net Pay   : {net_pay}")
print("============================")
