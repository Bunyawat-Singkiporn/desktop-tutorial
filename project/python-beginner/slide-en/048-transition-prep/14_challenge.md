# Check with collection

difficulty:

---

♪ Task

Creates three input entries and types the number of elements with set

---

♪ Input

See example

♪ Output

One line.

---

## Example

**Input:*

```text
a
b
a
```

**Output:**

```text
2
```---

¶ Hint ¶

Re-st

---

♪ Starter Code

```python
vals = []
for i in range(3):
    vals.append(input())
print(len(set(vals)))
```
