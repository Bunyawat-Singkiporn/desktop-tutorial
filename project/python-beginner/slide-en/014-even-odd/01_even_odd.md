# 🔢 Even / Odd — Even and odd numbers.

---

## % What is?

The symbol `%` is called **Modulo**.

> Used to find **remainder from division**

|Expression|meaning|result|
|--------|----------|---------|
| `7 % 2` |7 divided by 2 leaves a remainder.| `1` |
| `10 % 2` |10 divided by 2 leaves a remainder.| `0` |
| `9 % 2` |9 divided by 2 leaves a remainder.| `1` |

---

## Inspection principles

|condition|meaning|
|----------|----------|
| `number % 2 == 0` |➜ Number**Even** (Even)|
| `number % 2 != 0` |➜ Number**Odd** (Odd)|

---

## Program example

```python
number = int(input())

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Sample Input / Output

| Input | Output |
|-------|--------|
| `8` | `Even` |
| `7` | `Odd` |