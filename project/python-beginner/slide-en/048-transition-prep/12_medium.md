# ^ Transition Prep □ Q12: Mix list+if

difficulty:* ^Medium

---

♪ Task

From ^2, 5, 8, 1] Only even.

---

♪ Input

None

♪ Output

Two lines.

---

## Example

♪ Output:*

```text
2
8
```---

¶ Hint ¶

Use %

---

♪ Starter Code

```python
nums = [2, 5, 8, 1]
for n in nums:
    if n % 2 == 0:
        print(n)
```
