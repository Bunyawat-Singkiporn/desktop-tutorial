# 🛡️ Loop Safety — Control your Loop safely.

---

## break — Stops the Loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:
```
0
1
2
3
4
```

> `break` exits the loop immediately and does not complete the remaining cycles.

---

## continue — skip this round

```python
for i in range(6):
    if i == 3:
        continue
    print(i)
```

Output:
```
0
1
2
4
5
```

> `continue` skips this cycle and proceeds to the next cycle (does not exit the loop).

---

## break vs continue

| Command | Effect |
|---------|--------|
| `break` |Stop the loop immediately — exit.|
| `continue` |Skip this round — continue on to the next round.|

---

## while True + break

Repeat input until user types `"quit"`:

```python
while True:
    word = input()
    if word == "quit":
        break
    print("You typed:", word)

print("Goodbye!")
```

```
hello → You typed: hello
world → You typed: world
quit  → Goodbye!
```

---

## continue — filter values

Show only odd numbers:

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue     # skip even numbers
    print(i)
```

Output:
```
1
3
5
7
9
```

---

## Loop Safety Checklist

- [ ] `while` must have a variable that changes value every cycle.
- [ ] Use `break` when you want to stop halfway.
- [ ] Use `continue` when you want to skip some rounds.
- [ ] Test with multiple input values.
