# Practice Function — Medium: Filter Passing Scores

**Difficulty:** 🟡 Medium

---

## Task

Create `pass_scores(scores)` that returns scores >= 50.

Main program reads `n` scores into a list, then prints the passed ones.

> Combines: function + return + input + for + list + if

---

## Example Session

```
How many? 5
Score: 40
Score: 70
Score: 55
Score: 30
Score: 90
Passed: [70, 55, 90]
```

---

## Starter Code

```python
def pass_scores(scores):
    # Write your code here

n = int(input("How many? "))
scores = []
for i in range(n):
    scores.append(int(input("Score: ")))

print(f"Passed: {pass_scores(scores)}")
```
