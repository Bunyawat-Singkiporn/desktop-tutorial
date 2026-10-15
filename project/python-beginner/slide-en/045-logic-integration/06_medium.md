# Logic Integration × Q6:

difficulty:* ^Medium

---

♪ Task

Take n and read n points and type in the sum.

== sync, corrected by elderman == *

- The first line is n.
- Followed by n lines.

---

♪ Input

See example

♪ Output

One line.

---

## Example

**Input:*

```text
3
40
50
60
```

**Output:**

```text
150
```---

¶ Hint ¶

Create list from pre-input

---

♪ Starter Code

```python
n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))
print(sum(scores))
```
