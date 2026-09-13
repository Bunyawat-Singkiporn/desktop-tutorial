# Practice Return Values — Medium: Even/Odd from Input

**Difficulty:** 🟡 Medium

---

## Task

Create `parity(n)` that returns `"Even"` or `"Odd"`.

Read 3 numbers with `input` (use `for`) and print each result.

> Combines: return + input + for loop + if

---

## Example Session

```
Enter number: 4
4 → Even
Enter number: 7
7 → Odd
Enter number: 10
10 → Even
```

---

## Starter Code

```python
def parity(n):
    # Write your code here

for i in range(3):
    n = int(input("Enter number: "))
    print(f"{n} → {parity(n)}")
```
