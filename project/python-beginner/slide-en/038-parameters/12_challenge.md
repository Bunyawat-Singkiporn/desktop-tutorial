# 🔥 Practice Parameters — Challenge: Movie Ticket Machine

**Difficulty:** 🔴 Hard

---

## Task

Build a movie ticket machine with **2 functions**:

| Function | Job |
|----------|-----|
| `ticket_price(age)` | return price — under 12 pays `80`, else `150` |
| `print_ticket(name, age, price)` | print the ticket |

Read name and age from `input`.

---

## Example

**Input:**
```
Alice
10
```

**Output:**
```
=== Movie Ticket ===
Name: Alice
Age: 10
Price: 80 baht
Enjoy the movie!
```

---

## Starter Code

```python
def ticket_price(age):
    # Write your code here

def print_ticket(name, age, price):
    # Write your code here

name = input()
age = int(input())
price = ticket_price(age)
print_ticket(name, age, price)
```
