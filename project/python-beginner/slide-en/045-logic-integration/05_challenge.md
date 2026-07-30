# 🔥 Logic Integration — Question 4: Mini ATM

**Difficulty:** 🔴 Hard

---

## Problem

Create a simple ATM program.

**Rules:**
- Start with a balance of 1,000 baht.
- Commands: `deposit`, `withdraw`, `balance`, `exit`
- Do not allow a withdrawal when the balance is insufficient.
- Record each transaction in a list.

**Example Session:**
```
Command: balance
Balance: 1000
Command: deposit
Amount: 500
Deposited: 500. Balance: 1500
Command: withdraw
Amount: 200
Withdrawn: 200. Balance: 1300
Command: withdraw
Amount: 2000
Insufficient funds
Command: balance
Balance: 1300
Command: exit
Transactions: 2
```

---

## Starter Code

```python
def show_balance(balance):
    print(f"Balance: {balance}")

balance = 1000
transactions = []

while True:
    command = input("Command: ")
    if command == "exit":
        print(f"Transactions: {len(transactions)}")
        break
    # Write your code here
```
