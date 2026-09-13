def add_money(wallet, amount):
    return wallet + amount

def spend_money(wallet, amount):
    if amount > wallet:
        return wallet
    return wallet - amount

def show_wallet(wallet):
    print(f"Wallet: {wallet} coins")

wallet = 100
action = input()
amount = int(input())

if action == "add":
    wallet = add_money(wallet, amount)
elif action == "spend":
    wallet = spend_money(wallet, amount)

show_wallet(wallet)
