# Practice Return — Medium: Clamp Score

**Difficulty:** 🟡 Medium

---

## Task

Create `clamp(score)` that keeps a score in 0–100.
Read 3 scores with `input` and print each clamped value.

> Combines: return + input + for + if/elif/else

---

## Example Session

```
Enter score: -5
0
Enter score: 150
100
Enter score: 85
85
```

---

## Starter Code

```python
def clamp(score):
    # Write your code here

for i in range(3):
    score = int(input("Enter score: "))
    print(clamp(score))
```
