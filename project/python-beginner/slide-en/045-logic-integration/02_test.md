# Logic Integration ^Q2:

difficulty:

---

♪ Task

Get three names on the list. Then type it in by name.

== sync, corrected by elderman == *

- Use the loop three times.

---

♪ Input

See example

♪ Output

Three lines.

---

## Example

**Input:*

```text
Ann
Ben
Cat
```

**Output:**

```text
Ann
Ben
Cat
```


---

## Starter Code

```python
names = []
for i in range(3):
    names.append(input())

for name in names:
    print(name)
```
