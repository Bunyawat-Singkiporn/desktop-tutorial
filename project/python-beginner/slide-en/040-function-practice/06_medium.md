# Practice Function — Medium: Shopping Bill from Input

**Difficulty:** 🟡 Medium

---

## Task

Create 2 functions:

| Function | Job |
|----------|-----|
| `calc_total(prices)` | return sum of price list |
| `add_vat(total)` | return total after 7% VAT (`total * 1.07`) |

Main program:
1. Ask how many items `n`
2. Read `n` prices into a list
3. Print before VAT and after VAT

> Combines: function + return + input + for + list + float

---

## Example Session

```
How many items? 3
Price: 100
Price: 50
Price: 25
Before VAT: 175.0
After VAT: 187.25
```

---

## Starter Code

```python
def calc_total(prices):
    # Write your code here

def add_vat(total):
    # Write your code here

n = int(input("How many items? "))
prices = []
for i in range(n):
    price = float(input("Price: "))
    prices.append(price)

total = calc_total(prices)
print(f"Before VAT: {total}")
print(f"After VAT: {add_vat(total)}")
```
