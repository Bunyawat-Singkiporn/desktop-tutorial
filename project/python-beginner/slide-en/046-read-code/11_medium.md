# Read code #

difficulty:* ^Medium

---

♪ Task

Let's say how many in [1, 4, 6, 3]] are greater than 3.

---

♪ Input

None

♪ Output

One line.

---

## Example

♪ Output:*

```text
2
```---

¶ Hint ¶

Count when conditions come true

---

♪ Starter Code

```python
nums = [1, 4, 6, 3]
count = 0
for n in nums:
    if n > 3:
        count += 1
print(count)
```
