# Logic Integration ^Q14: many profiles

difficulty:

---

♪ Task

Create dict from double name-score

== sync, corrected by elderman == *

- Get the n.
- Read it n times a round and score it.
- Print the whole dict.

---

♪ Input

See example

♪ Output

One line.

---

## Example

**Input:*

```text
2
Ada
90
Ben
70
```

**Output:**

```text
{'Ada': 90, 'Ben': 70}
```---

¶ Hint ¶

One key at a time.

---

♪ Starter Code

```python
n = int(input())
profiles = {}
for i in range(n):
    name = input()
    score = int(input())
    profiles[name] = score
print(profiles)
```
