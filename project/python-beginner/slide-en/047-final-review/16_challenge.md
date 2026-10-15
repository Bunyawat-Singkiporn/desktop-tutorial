♪ Final Review ♪

difficulty:

---

♪ Task

Take n points. If n is zero, then one decimal mean.

---

♪ Input

See example

♪ Output

One line.

---

## Example

**Input:*

```text
0
```

**Output:**

```text
No scores
```---

¶ Hint ¶

So let's divide by n check.

---

♪ Starter Code

```python
n = int(input())
if n == 0:
    print("No scores")
else:
    total = 0
    for i in range(n):
        total += int(input())
    print(f"{total / n:.1f}")
```
