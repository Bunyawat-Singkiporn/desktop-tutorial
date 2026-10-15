balance = int(input())
withdraw = int(input())
while withdraw <= balance:
    balance = balance - withdraw
    withdraw = int(input())
print(f"Remaining: {balance}")
