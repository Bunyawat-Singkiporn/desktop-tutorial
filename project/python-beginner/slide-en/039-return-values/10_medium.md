# Practice Return — Question 9: Fix Game Scores

**Difficulty:** 🟡 Medium

---

## Task

In your game, scores must stay between 0 and 100.

Create `fix_score(score)`:
- below 0 → `0`
- above 100 → `100`
- otherwise keep the value

Fix 3 raw scores from input.

---

## Example Session

```
Raw score: -5
Fixed: 0
Raw score: 150
Fixed: 100
Raw score: 85
Fixed: 85
```

---

## Starter Code

```python
def fix_score(score):
    # Write your code here

for i in range(3):
    score = int(input("Raw score: "))
    print(f"Fixed: {fix_score(score)}")
```
