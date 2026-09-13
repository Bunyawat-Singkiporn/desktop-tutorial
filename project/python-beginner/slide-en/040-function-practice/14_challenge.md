# 🔥 Practice Function — Challenge: Game Wallet

**Difficulty:** 🔴 Hard

---

## Task

Build an in-game wallet with **3 functions**:

| Function | Job |
|----------|-----|
| `add_money(wallet, amount)` | add coins, return new wallet |
| `spend_money(wallet, amount)` | spend coins (if not enough, keep old value) |
| `show_wallet(wallet)` | print balance |

Start with `wallet = 100`. Read `add` or `spend` and an amount once.

---

## Example

**Input:**
```
add
50
```

**Output:**
```
Wallet: 150 coins
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
