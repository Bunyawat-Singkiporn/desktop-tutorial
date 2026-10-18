def can_withdraw(balance, amount):
    if balance >= amount:
        return True
    else:
        return False

def new_balance(balance, amount):
    if can_withdraw(balance, amount):
        return balance - amount
    else:
        return balance

balance = int(input())
amount = int(input())

if can_withdraw(balance, amount):
    print("Success")
else:
    print("Not enough")
print(new_balance(balance, amount))
