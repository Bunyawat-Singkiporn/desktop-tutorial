# 🔥 Practice Function — Question 4: Score System

**Difficulty:** 🔴 Hard

---

## Problem

Create a score system with separate functions:

| Function | Responsibility |
|----------|----------------|
| `add_score(scores, name, score)` | Adds a score to the dictionary |
| `get_average(scores)` | Returns the average of all values in the dictionary |
| `get_top(scores)` | Returns the name and score of the highest-scoring student |
| `show_all(scores)` | Displays every student and score |

**Example Output:**
```
Alice: 85
Bob: 92
Charlie: 78
Average: 85.0
Top: Bob (92)
```

---

## Starter Code

```python
def add_score(scores, name, score):
    # Write your code here

def get_average(scores):
    # Write your code here

def get_top(scores):
    # Write your code here

def show_all(scores):
    # Write your code here

scores = {}
add_score(scores, "Alice", 85)
add_score(scores, "Bob", 92)
add_score(scores, "Charlie", 78)

show_all(scores)
print(f"Average: {get_average(scores):.1f}")
top_name, top_score = get_top(scores)
print(f"Top: {top_name} ({top_score})")
```
