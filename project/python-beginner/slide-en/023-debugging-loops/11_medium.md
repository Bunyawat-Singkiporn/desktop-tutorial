# d d d d d d d d d d d d d d d d d d d d d

difficulty:* ^Medium

---

♪ Task

I want two rows of star tables, four rows of them, but the loops are used. ▪

---

♪ Input

No.

♪ Output

Two star rows four.

---

## Example

♪ Output:*```text
****
****
```---

♪ Hint

The width is constant, not tied to the number. Row

---

♪ Starter Code```python
for row in range(2):
    for col in range(row):  # ← แก้
        print("*", end="")
    print()
```
