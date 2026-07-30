# ⏳ while Loop — Loops according to condition.

---

## What is a while Loop?

`while` loops **as long as the condition is True**

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

Output:
```
1
2
3
4
5
```

---

## while Loop structure

```python
while condition:
    # Repeated code
    # Variables must always be changed!
```

---

## for vs while

| | `for` | `while` |
|--|-------|---------|
|**Use when**|Know the exact number of turns|Cycle until the condition is False.|
|**example**|Count 1–10|Repeat input until correct.|

---

## Example: Countdown

```python
count = 5

while count > 0:
    print(count)
    count = count - 1

print("Blast off! 🚀")
```

Output:
```
5
4
3
2
1
Blast off! 🚀
```

---

## Example: Accept Input until correct

```python
secret = 42
guess = int(input())

while guess != secret:
    print("Wrong! Try again.")
    guess = int(input())

print("Correct!")
```

---

## ⚠️ Watch out: Infinite Loop

```python
# ❌ Never stops — forgot to add count!
count = 1
while count <= 5:
    print(count)
    # No count = count + 1 → Condition is always True.

# ✅ Correct
count = 1
while count <= 5:
    print(count)
    count = count + 1   # ← You must always have this line!
```

> Press **Ctrl + C** to stop the stuck program.
