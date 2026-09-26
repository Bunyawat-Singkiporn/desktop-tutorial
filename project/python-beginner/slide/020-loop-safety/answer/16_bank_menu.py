balance = 1000
while True:
    cmd = input()
    if cmd == "quit":
        print("========================")
        print(f"Balance: {balance}")
        print("========================")
        break
    elif cmd == "deposit":
        amount = int(input())
        balance = balance + amount
    elif cmd == "withdraw":
        amount = int(input())
        if amount > balance:
            print("Denied")
            continue
        balance = balance - amount
    else:
        print("Unknown")
        continue
