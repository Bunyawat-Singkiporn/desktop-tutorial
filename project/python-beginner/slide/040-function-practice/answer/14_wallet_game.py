def add_money(wallet, amount):
    wallet["coin"] = wallet["coin"] + amount

def spend_money(wallet, amount):
    wallet["coin"] = wallet["coin"] - amount

def show_wallet(wallet):
    print(f"Coins: {wallet['coin']}")

wallet = {"coin": 100}
add_money(wallet, 50)
spend_money(wallet, 30)
show_wallet(wallet)
