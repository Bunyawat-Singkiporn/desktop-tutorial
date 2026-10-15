♪ Logic Integration QC16: rough grade class

difficulty:

---

♪ Task

To sum up the status of the entire room.

== sync, corrected by elderman == *

- Create ^statuscore)
- There's ^scores = [45, 70, 88] ▪
- Print status by line.

---

♪ Input

None

♪ Output

Three lines.

---

## Example

♪ Output:*

```text
Fail
Pass
Pass
```---

¶ Hint ¶

Don't do A/B/C/F.

---

♪ Starter Code

```python
def status(score):
    # return Pass/Fail

scores = [45, 70, 88]
for s in scores:
    print(status(s))
```
