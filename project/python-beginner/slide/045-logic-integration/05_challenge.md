# 🔥 Logic Integration — Question 4: Mini ATM

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างโปรแกรม ATM อย่างง่าย:

**Rules:**
- เริ่มต้นมียอดเงิน 1000 บาท
- Commands: `deposit`, `withdraw`, `balance`, `exit`
- ถอนไม่ได้ถ้าเงินไม่พอ
- แต่ละ transaction บันทึกใน list

**ตัวอย่าง Session:**
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
