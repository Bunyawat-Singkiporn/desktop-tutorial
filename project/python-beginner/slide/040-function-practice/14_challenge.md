# 🔥 Practice Function — Challenge: กระเป๋าเงินในเกม

**Difficulty:** 🔴 Hard

---

## โจทย์

ทำระบบเงินในเกมด้วย **3 functions**:

| Function | หน้าที่ |
|----------|---------|
| `add_money(wallet, amount)` | เพิ่มเงิน แล้ว return wallet ใหม่ |
| `spend_money(wallet, amount)` | ถอนเงิน (ถ้าเงินไม่พอ return wallet เดิม) |
| `show_wallet(wallet)` | แสดงยอดเงิน |

เริ่มต้น `wallet = 100`  
รับคำสั่ง `add` หรือ `spend` และจำนวนเงิน 1 ครั้ง แล้วแสดงผล

---

## ตัวอย่าง

**Input:**
```
add
50
```

**Output:**
```
Wallet: 150 coins
```

**Input:**
```
spend
30
```

**Output:**
```
Wallet: 70 coins
```

**Input:**
```
spend
200
```

**Output:**
```
Wallet: 100 coins
```

---

## Starter Code

```python
def add_money(wallet, amount):
    # Write your code here

def spend_money(wallet, amount):
    # Write your code here

def show_wallet(wallet):
    # Write your code here

wallet = 100
action = input()
amount = int(input())

if action == "add":
    wallet = add_money(wallet, amount)
elif action == "spend":
    wallet = spend_money(wallet, amount)

show_wallet(wallet)
```
