# d d d d d d d d d d d d d d d d d d

difficulty:

---

♪ Task

Number of products in the class. ▪
- Skip the zero.
- Gather the rest.
- Counting the amount of stuff.
Must have been ^Heelves: 3 . . . . ▪
The code starts counting zeros and wrong collections.

---

♪ Input

No.

♪ Output

Two lines summary.

---

## Example

♪ Output:*```text
Shelves: 3
Items: 14
```---

♪ Hint

Skip zero first and then count the layers and add the numbers.

---

♪ Starter Code```python
stock = [4, 0, 7, 0, 3]
shelves = 0
items = 0
for qty in stock:
    shelves = shelves + 1
    items = qty
print(f"Shelves: {shelves}")
print(f"Items: {items}")
```
