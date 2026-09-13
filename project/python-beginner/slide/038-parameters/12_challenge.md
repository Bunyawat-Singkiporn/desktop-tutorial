# 🔥 Practice Parameters — Challenge: ตู้ขายตั๋วหนัง

**Difficulty:** 🔴 Hard

---

## โจทย์

ทำตู้ขายตั๋วหนังด้วย **2 functions**:

| Function | หน้าที่ |
|----------|---------|
| `ticket_price(age)` | return ราคา — อายุ < 12 จ่าย `80` นอกนั้น `150` |
| `print_ticket(name, age, price)` | แสดงตั๋ว |

รับชื่อและอายุจาก `input` แล้วเรียกทั้งสอง function

---

## ตัวอย่าง

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

**Input:**
```
Bob
15
```

**Output:**
```
=== Movie Ticket ===
Name: Bob
Age: 15
Price: 150 baht
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
