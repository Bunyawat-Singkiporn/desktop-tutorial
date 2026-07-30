def show_balance(balance):
    print(f"Balance: {balance}")

balance = 1000
transactions = []

while True:
    command = input("Command: ")
    if command == "exit":
        print(f"Transactions: {len(transactions)}")
        break
    elif command == "balance":
        show_balance(balance)
    elif command == "deposit":
        amount = int(input("Amount: "))
        balance += amount
        transactions.append(("deposit", amount))
        print(f"Deposited: {amount}. Balance: {balance}")
    elif command == "withdraw":
        amount = int(input("Amount: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            transactions.append(("withdraw", amount))
            print(f"Withdrawn: {amount}. Balance: {balance}")
