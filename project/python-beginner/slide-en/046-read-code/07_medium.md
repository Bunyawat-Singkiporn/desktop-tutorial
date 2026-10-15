# Read code #

difficulty:* ^Medium

---

♪ Task

The largest value in ^3, 7, 2, 9, 4]3 starts at 0 and updates When it comes to values.

---

♪ Input

None

♪ Output

One line.

---

## Example

♪ Output:*

```text
9
```---

¶ Hint ¶

Updating at greater value

---

♪ Starter Code

```python
numbers = [3, 7, 2, 9, 4]
result = 0
for num in numbers:
    if num > result:
        result = num
print(result)
```
