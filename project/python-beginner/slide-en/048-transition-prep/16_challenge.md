♪ Transition Prep QC16: final problem

difficulty:

---

♪ Task

Get n students and read their names and scores, make their dict, and print out those who get the highest marks.

== sync, corrected by elderman == *

- Print ^Top:

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
Ann
80
Bee
95
Cat
70
```

**Output:**

```text
Top: Bee 95
```---

¶ Hint ¶

Keep in dict and compare

---

♪ Starter Code

```python
n = int(input())
data = {}
for i in range(n):
    name = input()
    score = int(input())
    data[name] = score

best_name = ""
best_score = -1
for name, score in data.items():
    if score > best_score:
        best_score = score
        best_name = name
print(f"Top: {best_name} {best_score}")
```
