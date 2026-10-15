♪ Logic Integration QC: Q5

difficulty:

---

♪ Task

The queue may be repeated. Print the number of names twice.

== sync, corrected by elderman == *

- Get an n and read n names.
- Use set to type

---

♪ Input

See example

♪ Output

One line.

---

## Example

**Input:*

```text
4
Ann
Ben
Ann
Cat
```

**Output:**

```text
3
```---

¶ Hint ¶

& Re-write

---

♪ Starter Code

```python
n = int(input())
names = []
for i in range(n):
    names.append(input())
print(len(set(names)))
```
