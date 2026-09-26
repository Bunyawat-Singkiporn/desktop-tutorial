department = input()
sales = int(input())

if department == "sales":
    salary = 18000
elif department == "support":
    salary = 15000
else:
    salary = 12000

if sales >= 100000:
    bonus = 5000
elif sales >= 50000:
    bonus = 2000
else:
    bonus = 500

net_pay = salary + bonus

print("============================")
print("          PAYROLL")
print("============================")
print(f"Salary  : {salary}")
print(f"Bonus   : {bonus}")
print(f"Net Pay : {net_pay}")
print("============================")
