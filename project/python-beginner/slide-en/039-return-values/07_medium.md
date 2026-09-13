# Practice Return — Question 6: Lucky Number Game

**Difficulty:** 🟡 Medium

---

## Task

A tiny game: the player enters a number and learns if it is Even or Odd.

Create `lucky(n)` that returns `"Even"` or `"Odd"`. Play 3 rounds.

---

## Example Session

```
Your number: 4
4 is Even
Your number: 7
7 is Odd
Your number: 10
10 is Even
```

---

## Starter Code

```python
def lucky(n):
    # Write your code here

for i in range(3):
    n = int(input("Your number: "))
    print(f"{n} is {lucky(n)}")
```
