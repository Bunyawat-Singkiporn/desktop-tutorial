def wallet_status(money):
    if money < 50:
        return "Broke"
    elif money < 200:
        return "OK"
    else:
        return "Rich"

print(wallet_status(30))
print(wallet_status(120))
print(wallet_status(500))
